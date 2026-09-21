# codex-workspace-bootstrap 日本語ガイド

Windows上の既存リポジトリを、Codexで扱いやすい状態に診断・初期化するための小さなCLIです。

## 主な機能

- Git / Python / Node.js / npm / PowerShell / WSL / Codex の利用可否を確認
- README、LICENSE、.gitignore、AGENTS.md、主要マニフェストを確認
- .env、秘密鍵、credential系ファイル名を検出して警告
- Codex向けのスターター `AGENTS.md` を安全に生成
- JSON形式の監査結果を出力
- GitHub ActionsなどCIから利用可能

## Windowsでの導入

PowerShellで以下を実行します。

```powershell
git clone https://github.com/kohli217/codex-workspace-bootstrap.git
cd codex-workspace-bootstrap
py -m pip install -e .
```

監査:

```powershell
codex-workspace-bootstrap audit .
```

AGENTS.md生成:

```powershell
codex-workspace-bootstrap init-agents .
```

既存のAGENTS.mdは、`--force` を指定しない限り上書きしません。

## セキュリティ上の考え方

初期版の秘密情報チェックはファイル名ベースです。ファイルの中身を表示したり、外部へ送信したりしません。

ただし、監査結果がPASSでも「安全性が保証された」という意味ではありません。公開前には必ず差分を目視確認してください。

## Codexと一緒に使う流れ

1. `audit` で現状を確認
2. 警告内容を確認
3. 必要なら `init-agents` でCodex向け指示を生成
4. CodexにIssue単位で作業を依頼
5. テストを実行
6. 再度audit
7. git diffを確認してからコミット/PR

## ライセンス

MIT License
