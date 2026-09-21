from pathlib import Path

from codex_workspace_bootstrap.audit import audit_repository, summary


def test_audit_detects_basic_repository_files(tmp_path: Path) -> None:
    (tmp_path / ".git").mkdir()
    (tmp_path / "README.md").write_text("# demo\n", encoding="utf-8")
    (tmp_path / "LICENSE").write_text("MIT\n", encoding="utf-8")
    (tmp_path / ".gitignore").write_text(".env\n", encoding="utf-8")
    (tmp_path / "AGENTS.md").write_text("# agents\n", encoding="utf-8")
    (tmp_path / "pyproject.toml").write_text("[project]\nname='demo'\n", encoding="utf-8")

    checks = audit_repository(tmp_path)
    by_name = {c.name: c for c in checks}

    assert by_name["git-repository"].status == "pass"
    assert by_name["readme"].status == "pass"
    assert by_name["license"].status == "pass"
    assert by_name["gitignore"].status == "pass"
    assert by_name["agents"].status == "pass"
    assert by_name["project-manifest"].status == "pass"


def test_audit_warns_on_secret_risk_filename(tmp_path: Path) -> None:
    (tmp_path / ".env").write_text("EXAMPLE=not-a-secret\n", encoding="utf-8")
    checks = audit_repository(tmp_path)
    by_name = {c.name: c for c in checks}
    assert by_name["secret-risk-files"].status == "warn"


def test_summary_counts_statuses(tmp_path: Path) -> None:
    checks = audit_repository(tmp_path)
    totals = summary(checks)
    assert totals["passed"] + totals["warnings"] == len(checks)
    assert totals["blocking"] == 0
