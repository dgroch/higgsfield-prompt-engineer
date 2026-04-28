# MCP Setup — Higgsfield Seedance 2.0

The eval harness and Claude Code skills both rely on Higgsfield's MCP server
to submit prompts and retrieve rendered video. There are two ways to wire
this up.

## Option A — Official Higgsfield MCP (recommended)

Higgsfield publishes a hosted MCP server authenticated via your Higgsfield
account. No API keys to manage; auth is OAuth-based and refreshes
automatically.

### Setup in Claude Code

1. Sign in to <https://higgsfield.ai>.
2. Open your account settings; copy the MCP server URL shown for your
   workspace (it is account-scoped).
3. Add it to your Claude Code MCP config:

   ```bash
   claude mcp add higgsfield <YOUR-HIGGSFIELD-MCP-URL>
   ```

4. Run `claude mcp list` to confirm the connection. Claude Code will prompt
   for OAuth authentication on first use.

### Setup for the Anthropic API (used by the eval harness)

The harness uses Anthropic's MCP connector — Claude calls remote MCP servers
directly via the API. Set two env vars:

```bash
export HIGGSFIELD_MCP_URL="<YOUR-HIGGSFIELD-MCP-URL>"
export HIGGSFIELD_OAUTH_TOKEN="<YOUR-OAUTH-BEARER-TOKEN>"
```

To obtain the OAuth bearer token, complete the OAuth flow in your Higgsfield
account; the token is shown in your developer settings. Tokens refresh
periodically — re-export when expired (the harness reports a clear error on
401).

The harness passes these into `messages.create` like so:

```python
client.beta.messages.create(
    model="claude-opus-4-7",
    betas=["mcp-client-2025-11-20"],
    mcp_servers=[{
        "type": "url",
        "name": "higgsfield",
        "url": os.environ["HIGGSFIELD_MCP_URL"],
        "authorization_token": os.environ["HIGGSFIELD_OAUTH_TOKEN"],
    }],
    ...
)
```

## Option B — Community local MCP (fallback)

If the official MCP is not yet enabled on your account, the community
MCP at <https://github.com/geopopos/higgsfield_ai_mcp> provides equivalent
coverage as a local stdio server.

```bash
git clone https://github.com/geopopos/higgsfield_ai_mcp.git /opt/higgsfield-mcp
cd /opt/higgsfield-mcp
pip install -e .
export HF_API_KEY="<from https://cloud.higgsfield.ai/api-keys>"
export HF_SECRET="<from https://cloud.higgsfield.ai/api-keys>"
```

To use with Claude Code, add to your MCP config:

```json
{
  "mcpServers": {
    "higgsfield": {
      "command": "python",
      "args": ["-m", "higgsfield_mcp.server"],
      "env": {
        "HF_API_KEY": "${HF_API_KEY}",
        "HF_SECRET": "${HF_SECRET}"
      }
    }
  }
}
```

The eval harness can also drive the local MCP via the Anthropic SDK's MCP
helpers (`anthropic[mcp]`). Set `HIGGSFIELD_MCP_MODE=local` and the harness
will spawn the stdio server automatically.

> **Note on tool surface.** The community MCP exposes the older Higgsfield
> API (Soul model for images, motion presets for video) — not Seedance 2.0
> directly. Tool names are `generate_image`, `generate_video`,
> `get_generation_status`, `list_characters`, `create_character`. The
> harness adapts to either tool surface.

## Which tools the harness expects

The harness needs at least one tool that:

1. Accepts a prompt string and returns a job identifier.
2. Lets us poll for completion and retrieve a video URL or file.

The harness's MCP client tries these names in order:

| Preferred | Fallback (community MCP) |
| --------- | ------------------------ |
| `seedance_render`, `video_generate` | `generate_video` |
| `render_status`, `get_status`       | `get_generation_status` |

If your MCP exposes different names, edit `eval/mcp_client.py` —
`PREFERRED_RENDER_TOOLS` and `PREFERRED_STATUS_TOOLS` are at the top of the
file.

## Verifying the connection

Once configured, run:

```bash
python -m eval.cli check-mcp
```

This sends a minimal "list tools" call through the MCP connector and prints
the tool names + schemas it discovers. If this fails, fix the connection
before running an eval.
