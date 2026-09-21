from pathlib import Path

from codex_workspace_bootstrap.cli import main


def test_init_agents_creates_file(tmp_path: Path) -> None:
    code = main(["init-agents", str(tmp_path)])
    assert code == 0
    assert (tmp_path / "AGENTS.md").exists()


def test_init_agents_does_not_overwrite_without_force(tmp_path: Path) -> None:
    target = tmp_path / "AGENTS.md"
    target.write_text("keep me", encoding="utf-8")
    code = main(["init-agents", str(tmp_path)])
    assert code == 1
    assert target.read_text(encoding="utf-8") == "keep me"


def test_audit_writes_json(tmp_path: Path) -> None:
    report = tmp_path / "report.json"
    code = main(["audit", str(tmp_path), "--json", str(report)])
    assert code == 0
    assert report.exists()
