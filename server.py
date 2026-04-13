"""Note Taking AI MCP Server — Note management tools."""
import hashlib
import json
import re
import time
from datetime import datetime
from typing import Any
from mcp.server.fastmcp import FastMCP

mcp = FastMCP("note-taking-ai-mcp")
_calls: dict[str, list[float]] = {}
DAILY_LIMIT = 50
_notes: list[dict] = []

def _rate_check(tool: str) -> bool:
    now = time.time()
    _calls.setdefault(tool, [])
    _calls[tool] = [t for t in _calls[tool] if t > now - 86400]
    if len(_calls[tool]) >= DAILY_LIMIT:
        return False
    _calls[tool].append(now)
    return True

@mcp.tool()
def create_note(title: str, content: str, tags: str = "", category: str = "general") -> dict[str, Any]:
    """Create a new note with title, content, optional comma-separated tags and category."""
    if not _rate_check("create_note"):
        return {"error": "Rate limit exceeded (50/day)"}
    tag_list = [t.strip() for t in tags.split(",") if t.strip()] if tags else []
    note_id = hashlib.md5(f"{title}{time.time()}".encode()).hexdigest()[:8]
    note = {
        "id": note_id, "title": title, "content": content,
        "tags": tag_list, "category": category,
        "word_count": len(content.split()),
        "created_at": datetime.utcnow().isoformat()
    }
    _notes.append(note)
    return {"note": note, "total_notes": len(_notes)}

@mcp.tool()
def search_notes(query: str, search_in: str = "all") -> dict[str, Any]:
    """Search notes by keyword. search_in: all, title, content, tags."""
    if not _rate_check("search_notes"):
        return {"error": "Rate limit exceeded (50/day)"}
    q = query.lower()
    results = []
    for note in _notes:
        match = False
        if search_in in ("all", "title") and q in note["title"].lower():
            match = True
        if search_in in ("all", "content") and q in note["content"].lower():
            match = True
        if search_in in ("all", "tags") and any(q in t.lower() for t in note["tags"]):
            match = True
        if match:
            results.append(note)
    return {"query": query, "results": results, "count": len(results)}

@mcp.tool()
def summarize_notes(note_ids: str = "", max_sentences: int = 3) -> dict[str, Any]:
    """Summarize notes. note_ids: comma-separated IDs or empty for all. Extracts key sentences."""
    if not _rate_check("summarize_notes"):
        return {"error": "Rate limit exceeded (50/day)"}
    ids = [i.strip() for i in note_ids.split(",") if i.strip()] if note_ids else None
    target = [n for n in _notes if ids is None or n["id"] in ids] if _notes else []
    if not target:
        return {"error": "No notes found"}
    summaries = []
    for note in target:
        sentences = re.split(r'[.!?]+', note["content"])
        sentences = [s.strip() for s in sentences if s.strip()]
        key = sentences[:max_sentences]
        summaries.append({
            "id": note["id"], "title": note["title"],
            "summary": ". ".join(key) + ("." if key else ""),
            "total_sentences": len(sentences), "shown": len(key)
        })
    return {"summaries": summaries, "notes_processed": len(summaries)}

@mcp.tool()
def export_markdown(note_ids: str = "", include_metadata: bool = True) -> dict[str, Any]:
    """Export notes as Markdown. note_ids: comma-separated or empty for all."""
    if not _rate_check("export_markdown"):
        return {"error": "Rate limit exceeded (50/day)"}
    ids = [i.strip() for i in note_ids.split(",") if i.strip()] if note_ids else None
    target = [n for n in _notes if ids is None or n["id"] in ids] if _notes else []
    if not target:
        return {"error": "No notes found"}
    parts = []
    for note in target:
        md = f"# {note['title']}\n\n"
        if include_metadata:
            md += f"**ID:** {note['id']} | **Category:** {note['category']} | **Created:** {note['created_at']}\n"
            if note["tags"]:
                md += f"**Tags:** {', '.join(note['tags'])}\n"
            md += "\n---\n\n"
        md += note["content"]
        parts.append(md)
    return {"markdown": "\n\n---\n\n".join(parts), "notes_exported": len(parts)}

if __name__ == "__main__":
    mcp.run()
