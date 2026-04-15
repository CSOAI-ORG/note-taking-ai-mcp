# Note Taking AI

> By [MEOK AI Labs](https://meok.ai) — Note management with search, summarization, and Markdown export

## Installation

```bash
pip install note-taking-ai-mcp
```

## Usage

```bash
python server.py
```

## Tools

### `create_note`
Create a new note with title, content, optional comma-separated tags and category.

**Parameters:**
- `title` (str): Note title
- `content` (str): Note content
- `tags` (str): Comma-separated tags
- `category` (str): Category (default: "general")

### `search_notes`
Search notes by keyword in title, content, or tags.

**Parameters:**
- `query` (str): Search query
- `search_in` (str): Search scope: all, title, content, tags (default: "all")

### `summarize_notes`
Summarize notes by extracting key sentences.

**Parameters:**
- `note_ids` (str): Comma-separated note IDs (empty for all)
- `max_sentences` (int): Max sentences per summary (default: 3)

### `export_markdown`
Export notes as formatted Markdown with optional metadata.

**Parameters:**
- `note_ids` (str): Comma-separated note IDs (empty for all)
- `include_metadata` (bool): Include ID, category, date, tags (default: True)

## Authentication

Free tier: 15 calls/day. Upgrade at [meok.ai/pricing](https://meok.ai/pricing) for unlimited access.

## License

MIT — MEOK AI Labs
