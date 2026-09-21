# codex-workspace-bootstrap

Make Windows repositories **Codex-ready** with automated environment checks, project instructions, safety audits, and maintainer workflows.

## Why this exists

Codex works best when a repository is explicit about its toolchain, commands, constraints, and contribution workflow. On Windows, those details are often scattered across README files, local shell history, and machine-specific assumptions.

`codex-workspace-bootstrap` turns that setup into a repeatable CLI:

- checks common developer tools such as Git, Python, Node.js, npm, PowerShell, WSL, and Codex
- audits a repository for Codex-friendly project instructions
- detects common secret-bearing files before they are accidentally committed
- generates a starter `AGENTS.md`
- generates a machine-readable audit report
- provides a `--strict` mode suitable for CI
- is dependency-light and designed to work well on Windows

## Status

Early public release. The project is intentionally small, auditable, and easy to extend.

## Quick start

### Option A: run from source

```powershell
git clone https://github.com/kohli217/codex-workspace-bootstrap.git
cd codex-workspace-bootstrap
py -m pip install -e .
codex-workspace-bootstrap audit .
```

### Option B: without installing

```powershell
py -m codex_workspace_bootstrap audit .
```

## Commands

### Audit the current repository

```powershell
codex-workspace-bootstrap audit .
```

### Write JSON output

```powershell
codex-workspace-bootstrap audit . --json report.json
```

### Fail CI when blocking issues are found

```powershell
codex-workspace-bootstrap audit . --strict
```

### Generate a starter AGENTS.md

```powershell
codex-workspace-bootstrap init-agents .
```

The command never overwrites an existing `AGENTS.md` unless `--force` is supplied.

## What the audit checks

The first release checks:

1. repository basics: Git metadata, README, license, ignore rules
2. Codex guidance: `AGENTS.md`
3. local toolchain: Git, Python, Node.js, npm, PowerShell, WSL, Codex
4. secret-risk filenames such as `.env`, private keys, and credential files
5. common project manifests such as `pyproject.toml`, `package.json`, and `requirements.txt`

The output is intentionally factual. It reports what is present, missing, or potentially risky without modifying the repository.

## Example output

```text
Repository: C:\work\my-project
[PASS] Git repository detected
[PASS] README detected
[WARN] AGENTS.md not found
[PASS] .gitignore detected
[PASS] git available
[PASS] python available
[WARN] codex command not found
Summary: 5 passed, 2 warnings, 0 blocking
```

## Codex workflow

A practical workflow is:

1. run `audit`
2. fix blocking issues
3. generate or review `AGENTS.md`
4. ask Codex to work on a scoped issue
5. run tests and the audit again
6. review the diff before merge

See [AGENTS.md](AGENTS.md) for the instructions used when Codex works on this repository.

## Design goals

- **Safe by default**: never overwrite project files without an explicit flag.
- **Useful on Windows**: PowerShell-first examples and checks for Windows tooling.
- **CI-friendly**: deterministic exit codes and JSON output.
- **No telemetry**: the CLI does not send repository contents anywhere.
- **Easy to audit**: standard-library implementation for the core command path.

## Roadmap

- richer language/toolchain detection
- GitHub Actions workflow generation
- project-specific AGENTS.md templates
- optional OpenAI API-assisted instruction drafting
- Windows environment repair suggestions
- repository security checks suitable for OSS maintainers

## Contributing

Issues and pull requests are welcome. See [CONTRIBUTING.md](CONTRIBUTING.md).

## Security

Please do not disclose credentials or private repository data in public issues. See [SECURITY.md](SECURITY.md).

## License

MIT. See [LICENSE](LICENSE).
