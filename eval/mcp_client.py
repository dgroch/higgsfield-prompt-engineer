"""MCP client wrapper: drives Claude to call the Higgsfield MCP and return
a video URL.

The eval harness deliberately leaves the MCP tool surface abstract — it
asks Claude (with MCP access) to "render this prompt and return the result
URL", letting Claude figure out which tool to call (e.g. seedance_render,
generate_video) and how to poll for completion. This way the harness works
with the official Higgsfield MCP, the community geopopos MCP, or any future
variant, without code changes.
"""

from __future__ import annotations

import json
import os
import re
from dataclasses import dataclass

import anthropic

MODEL = "claude-opus-4-7"

# Names the harness would prefer to see if the MCP exposes them. The
# orchestrator prompt lists these as hints, but Claude is free to pick the
# closest match if the actual tool surface differs.
PREFERRED_RENDER_TOOLS = ("seedance_render", "video_generate", "generate_video")
PREFERRED_STATUS_TOOLS = ("render_status", "get_status", "get_generation_status")


@dataclass
class RenderResult:
    video_url: str
    job_id: str | None
    raw_response: dict | None


def _mcp_servers_config() -> list[dict]:
    """Build the mcp_servers parameter for the Anthropic API."""
    url = os.environ.get("HIGGSFIELD_MCP_URL")
    if not url:
        raise RuntimeError(
            "HIGGSFIELD_MCP_URL is not set. See mcp/README.md for setup."
        )

    server: dict = {
        "type": "url",
        "name": "higgsfield",
        "url": url,
    }
    token = os.environ.get("HIGGSFIELD_OAUTH_TOKEN")
    if token:
        server["authorization_token"] = token

    return [server]


_ORCHESTRATOR_SYSTEM = (
    "You are a render orchestrator. Your job is to take a Higgsfield "
    "Seedance 2.0 prompt and produce a rendered video URL.\n\n"
    "Procedure:\n"
    "1. Call the MCP video-generation tool with the prompt. Likely names: "
    f"{', '.join(PREFERRED_RENDER_TOOLS)}.\n"
    "2. If the tool returns a job ID rather than a URL, poll the status "
    f"tool (likely names: {', '.join(PREFERRED_STATUS_TOOLS)}) until the "
    "job is complete. Wait 5–15 seconds between polls.\n"
    "3. Once you have a video URL, return it as JSON in this exact shape:\n"
    '   {"video_url": "https://...", "job_id": "...", "status": "complete"}\n'
    "4. If rendering fails or times out, return:\n"
    '   {"video_url": null, "job_id": "...", "status": "failed", '
    '"error": "..."}\n\n'
    "Return only the JSON object. No prose, no markdown."
)

_RESULT_SCHEMA = {
    "type": "object",
    "properties": {
        "video_url": {"type": ["string", "null"]},
        "job_id": {"type": ["string", "null"]},
        "status": {"type": "string", "enum": ["complete", "failed"]},
        "error": {"type": ["string", "null"]},
    },
    "required": ["video_url", "status"],
    "additionalProperties": True,
}


def render(
    prompt: str,
    *,
    duration_seconds: int = 8,
    aspect_ratio: str = "16:9",
    timeout_seconds: int = 600,
    client: anthropic.Anthropic | None = None,
) -> RenderResult:
    """Submit prompt to Higgsfield via MCP and return the video URL.

    The MCP loop runs server-side via Anthropic's MCP connector — Claude
    calls the tools, polls until done, and returns the URL.
    """
    client = client or anthropic.Anthropic()

    user_msg = (
        f"Render this prompt at {duration_seconds}s, {aspect_ratio}, 720p. "
        f"Return the video URL.\n\nPROMPT:\n{prompt}"
    )

    response = client.beta.messages.create(
        model=MODEL,
        max_tokens=8192,
        betas=["mcp-client-2025-11-20"],
        mcp_servers=_mcp_servers_config(),
        thinking={"type": "adaptive"},
        output_config={
            "effort": "medium",
            "format": {"type": "json_schema", "schema": _RESULT_SCHEMA},
            "task_budget": {"type": "tokens", "total": 64000},
        },
        system=_ORCHESTRATOR_SYSTEM,
        messages=[{"role": "user", "content": user_msg}],
    )

    text = next((b.text for b in response.content if b.type == "text"), None)
    if not text:
        raise RuntimeError(
            "MCP orchestrator returned no text. "
            f"stop_reason={response.stop_reason!r}"
        )

    try:
        result = json.loads(text)
    except json.JSONDecodeError:
        match = re.search(r"\{.*\}", text, flags=re.DOTALL)
        if not match:
            raise RuntimeError(f"Could not parse JSON from orchestrator: {text!r}")
        result = json.loads(match.group(0))

    if result.get("status") != "complete" or not result.get("video_url"):
        raise RuntimeError(
            f"Render failed: {result.get('error') or result}"
        )

    return RenderResult(
        video_url=result["video_url"],
        job_id=result.get("job_id"),
        raw_response=result,
    )


def list_tools(*, client: anthropic.Anthropic | None = None) -> list[dict]:
    """Diagnostic: ask Claude to list the MCP tools the server exposes."""
    client = client or anthropic.Anthropic()

    response = client.beta.messages.create(
        model=MODEL,
        max_tokens=2048,
        betas=["mcp-client-2025-11-20"],
        mcp_servers=_mcp_servers_config(),
        output_config={
            "effort": "low",
            "format": {
                "type": "json_schema",
                "schema": {
                    "type": "object",
                    "properties": {
                        "tools": {
                            "type": "array",
                            "items": {
                                "type": "object",
                                "properties": {
                                    "name": {"type": "string"},
                                    "description": {"type": "string"},
                                },
                                "required": ["name"],
                            },
                        }
                    },
                    "required": ["tools"],
                },
            },
        },
        messages=[{
            "role": "user",
            "content": (
                "List the MCP tools this server exposes. Return JSON: "
                '{"tools": [{"name": "...", "description": "..."}, ...]}'
            ),
        }],
    )
    text = next((b.text for b in response.content if b.type == "text"), "{}")
    return json.loads(text).get("tools", [])
