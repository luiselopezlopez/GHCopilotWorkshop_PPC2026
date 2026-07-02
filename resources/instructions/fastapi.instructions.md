---
applyTo: "backend/**/*.py"
description: "Use when editing FastAPI files in this workshop repository."
---

When you edit FastAPI files in this repo:

- preserve the teaching-friendly structure,
- keep dependencies explicit and close to the route,
- for new features, keep route handlers thin and push persistence logic down into a dedicated service or repository boundary,
- prefer response models over free-form dictionaries,
- prefer simple server-rendered flows over unnecessary client-side complexity,
- if you add SQLite persistence, keep schema initialization explicit and use parameterized SQL queries,
- keep all processing local to the monolith unless the task explicitly requires something else,
- add or update one focused validation step when behavior changes,
- avoid broad refactors that make the diff harder to explain live.
