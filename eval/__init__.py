"""Higgsfield prompt-engineering eval harness.

Iteratively refines prompts for Higgsfield Seedance 2.0 by:
  1. Generating a prompt via a Claude Skill.
  2. Submitting it to the Higgsfield MCP for rendering.
  3. Extracting frames from the rendered video.
  4. Scoring prompt + frames against a rubric (Claude as judge).
  5. Looping with critique until the score crosses a threshold or the
     iteration cap is hit.
"""

__version__ = "0.1.0"
