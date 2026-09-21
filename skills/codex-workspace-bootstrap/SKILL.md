---
name: codex-workspace-bootstrap
description: Audit a repository for Codex-readiness on Windows and generate safe starter project instructions.
---

# Codex Workspace Bootstrap

Use this skill when a user wants to prepare an existing repository for Codex-assisted development, especially on Windows.

## Workflow

1. Inspect the repository before editing.
2. Run:
   `python -m codex_workspace_bootstrap audit .`
3. Summarize factual warnings without claiming the repository is secure.
4. If `AGENTS.md` is missing, propose:
   `python -m codex_workspace_bootstrap init-agents .`
5. Never overwrite an existing `AGENTS.md` without explicit approval.
6. Never print or commit the contents of files suspected to contain secrets.
7. After changes, run tests and audit again.
8. Inspect the diff before proposing completion.

## Windows notes

Prefer PowerShell examples. Do not assume WSL is installed. Treat WSL, Node.js, and Codex as optional unless the repository requires them.
