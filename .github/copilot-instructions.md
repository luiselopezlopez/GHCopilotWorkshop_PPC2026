# GitHub Copilot Instructions

This repository supports a practical workshop. Optimize for teaching value over completeness.

## Project context

- `backend/` is a monolithic FastAPI notes app that renders HTML and keeps all processing local.
- `docs/` contains the lab guides. Prefer aligning code changes with the corresponding guide.
- Lab 2 focuses on adding local SQLite file persistence as an incremental feature, not on redesigning the app.

## Coding rules

- Keep changes small and easy to explain live.
- For FastAPI work, prefer explicit request and response models.
- For new features, prefer an incremental service or persistence boundary over route-level shortcuts.
- Keep SQLite access centralized and explicit instead of scattering SQL across routes and templates.
- Validate with the narrowest possible check first.
- When a file contains workshop TODO markers, preserve them unless the task explicitly resolves them.

## Teaching rules

- Prefer code that is readable in a live session over clever abstractions.
- If there is a tradeoff, choose the version that is easier for students to inspect and modify.
