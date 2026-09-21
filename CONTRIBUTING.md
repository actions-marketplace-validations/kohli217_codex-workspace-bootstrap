# Contributing

Thank you for considering a contribution.

## Development setup

On Windows PowerShell:

```powershell
git clone https://github.com/kohli217/codex-workspace-bootstrap.git
cd codex-workspace-bootstrap
py -m venv .venv
.\.venv\Scripts\Activate.ps1
python -m pip install -e .
```

For tests:

```powershell
python -m pip install pytest
pytest
```

## Pull requests

- keep the change focused;
- add tests for behavior changes;
- preserve Python 3.10+ compatibility;
- preserve Windows behavior;
- do not include credentials, private repository data, or generated environment files;
- update documentation when user-facing behavior changes.

## Good first contributions

Useful early contributions include additional toolchain checks, improved Windows diagnostics, and project-specific `AGENTS.md` templates.

## AI-assisted contributions

AI-assisted contributions are welcome. Contributors remain responsible for reviewing generated code, tests, licenses, security implications, and final diffs before submission.
