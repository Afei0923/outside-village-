# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Repository Overview

A small, Chinese-language ("村外" / outside village) project that currently contains two unrelated artifacts:

- `index.html` — a self-contained static webpage interpreting the Ningbo "科创甬江2035" 2026 R&D program application notice, branded for 宁波知宁技术服务有限公司. All CSS is inlined; no build step, no JS framework.
- `greeting.py` — a standalone Python module exposing a single `greet(name=None)` function that returns a Chinese greeting.
- `assets/logo.svg` — logo referenced by `index.html`.

There is no package manifest, build system, test suite, or linter configured. Treat each file as independent.

## Running things

```bash
# Preview the webpage locally
python3 -m http.server 8000
# then open http://localhost:8000/index.html

# Run the greeting module
python3 greeting.py
```

## Branch & PR workflow

- Feature branches follow `claude/<task-slug>-<shortid>` (e.g. `claude/add-chinese-greeting-MyrwC`, `claude/add-claude-documentation-j2oiV`).
- Work is merged into `main` via GitHub PR (PR #1 added the webpage, PR #3 added this CLAUDE.md).
- Never push directly to `main`.

## Editing notes

- `index.html` is a single self-contained file. When modifying styles or content, edit in place rather than extracting CSS/JS — the project's design is explicitly "no build tooling".
- Content is Chinese; preserve existing language unless the task explicitly asks for translation.
- When adding new top-level artifacts (e.g. another page or script), follow the same "single-file, no dependencies" pattern already established here.
