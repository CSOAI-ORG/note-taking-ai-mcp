<div align="center">

# Note Taking Ai MCP

**Note Taking AI MCP Server — Note management tools.**

[![PyPI](https://img.shields.io/pypi/v/meok-note-taking-ai-mcp)](https://pypi.org/project/meok-note-taking-ai-mcp/)
[![License: MIT](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)
[![MEOK AI Labs](https://img.shields.io/badge/MEOK_AI_Labs-MCP_Server-purple)](https://meok.ai)

</div>

## Overview

Note Taking AI MCP Server — Note management tools.

## Tools

| Tool | Description |
|------|-------------|
| `create_note` | Create a new note with title, content, optional comma-separated tags and categor |
| `search_notes` | Search notes by keyword. search_in: all, title, content, tags. |
| `summarize_notes` | Summarize notes. note_ids: comma-separated IDs or empty for all. Extracts key se |
| `export_markdown` | Export notes as Markdown. note_ids: comma-separated or empty for all. |

## Installation

```bash
pip install meok-note-taking-ai-mcp
```

## Usage with Claude Desktop

Add to your Claude Desktop MCP config (`claude_desktop_config.json`):

```json
{
  "mcpServers": {
    "note-taking-ai": {
      "command": "python",
      "args": ["-m", "meok_note_taking_ai_mcp.server"]
    }
  }
}
```

## Usage with FastMCP

```python
from mcp.server.fastmcp import FastMCP

# This server exposes 4 tool(s) via MCP
# See server.py for full implementation
```

## License

MIT © [MEOK AI Labs](https://meok.ai)
