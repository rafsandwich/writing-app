"""Functions for handling entry logic."""

from json import load, dump
from uuid import uuid4
from datetime import datetime


def load_all_entries(filename: str = "data.json") -> list[dict]:
    """Return all entries from a data file."""

    with open(filename, "r", encoding="utf-8") as f:
        entries = load(f)

    return entries


def is_valid_entry(entry: dict) -> bool:
    """Check if the entry is valid."""

    for k in ["body", "author"]:
        if k not in entry or not entry[k]:
            return False
    return True


def save_new_entry(entry: dict, filename: str = "data.json") -> dict:
    """Save a new entry to the data file."""

    entries = load_all_entries()

    entry["id"] == str(uuid4())
    if "title" not in entry:
        entry["title"] = None
    entry["created_at"] = datetime.now().isoformat()

    entries.append(entry)

    with open(filename, "w", encoding="utf-8") as f:
        dump(entries, f, indent=4)
