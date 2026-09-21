from __future__ import annotations

import argparse
import json
from pathlib import Path
import sys

from .audit import audit_repository, summary


AGENTS_TEMPLATE = """# AGENTS.md

## Purpose
This repository is maintained with assistance from Codex.

## Working rules
- Read README.md and existing project files before editing.
- Keep changes scoped to the requested issue.
- Do not add secrets, credentials, tokens, or private data.
- Prefer deterministic, scriptable commands over manual steps.
- Preserve Windows compatibility unless an issue explicitly changes platform support.
- Run the relevant tests before proposing completion.
- Explain any behavior change in the pull request or commit summary.

## Validation
Before finishing a change:
1. run the project test suite;
2. run `codex-workspace-bootstrap audit . --strict` when available;
3. inspect `git diff` for accidental files or secrets.
"""


def _parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        prog="codex-workspace-bootstrap",
        description="Audit and bootstrap repositories for reliable Codex workflows.",
    )
    sub = parser.add_subparsers(dest="command", required=True)

    audit = sub.add_parser("audit", help="Audit a repository and local toolchain")
    audit.add_argument("path", nargs="?", default=".")
    audit.add_argument("--json", dest="json_path", help="Write the complete report to a JSON file")
    audit.add_argument(
        "--strict",
        action="store_true",
        help="Return a non-zero exit code if blocking checks are present",
    )

    init_agents = sub.add_parser("init-agents", help="Create a starter AGENTS.md")
    init_agents.add_argument("path", nargs="?", default=".")
    init_agents.add_argument("--force", action="store_true", help="Overwrite an existing AGENTS.md")

    return parser


def _run_audit(path: str, json_path: str | None, strict: bool) -> int:
    root = Path(path).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(f"error: repository path does not exist or is not a directory: {root}", file=sys.stderr)
        return 2

    checks = audit_repository(root)
    totals = summary(checks)

    print(f"Repository: {root}")
    for check in checks:
        tag = "PASS" if check.status == "pass" else "WARN"
        print(f"[{tag}] {check.name}: {check.message}")

    print(
        f"Summary: {totals['passed']} passed, "
        f"{totals['warnings']} warnings, {totals['blocking']} blocking"
    )

    if json_path:
        payload = {
            "repository": str(root),
            "checks": [c.to_dict() for c in checks],
            "summary": totals,
        }
        output = Path(json_path).expanduser().resolve()
        output.parent.mkdir(parents=True, exist_ok=True)
        output.write_text(json.dumps(payload, indent=2), encoding="utf-8")
        print(f"JSON report written to: {output}")

    if strict and totals["blocking"]:
        return 1
    return 0


def _run_init_agents(path: str, force: bool) -> int:
    root = Path(path).expanduser().resolve()
    if not root.exists() or not root.is_dir():
        print(f"error: path does not exist or is not a directory: {root}", file=sys.stderr)
        return 2

    target = root / "AGENTS.md"
    if target.exists() and not force:
        print(f"error: {target} already exists; use --force to overwrite", file=sys.stderr)
        return 1

    target.write_text(AGENTS_TEMPLATE, encoding="utf-8")
    print(f"Created {target}")
    return 0


def main(argv: list[str] | None = None) -> int:
    args = _parser().parse_args(argv)
    if args.command == "audit":
        return _run_audit(args.path, args.json_path, args.strict)
    if args.command == "init-agents":
        return _run_init_agents(args.path, args.force)
    return 2
