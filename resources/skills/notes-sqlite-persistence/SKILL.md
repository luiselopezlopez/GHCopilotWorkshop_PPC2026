---
name: notes-sqlite-persistence
description: "Use when the workshop notes app needs local SQLite file persistence added as an incremental feature."
---

# Notes SQLite Persistence Skill

Use this skill when the notes app currently stores data in memory and you want to add file-based SQLite persistence without redesigning the monolith.

## Procedure

1. Read `backend/tests/test_notes_page.py`, `backend/app/routes/notes.py` and `backend/app/services/note_service.py` to understand the current flow.
2. Preserve the existing user-facing routes and HTML unless the feature explicitly requires a change.
3. Introduce persistence behind a small service or repository boundary instead of scattering SQL across routes.
4. Keep schema creation explicit and use parameterized SQL queries.
5. Prefer a small, teachable migration path from in-memory notes to SQLite-backed notes.
6. Validate first with one narrow command, then suggest one follow-up test for persistence behavior.

## Exit criteria

- The notes app still renders the main page.
- Creating a note writes it to a local SQLite file.
- The implementation is small enough to explain live.
