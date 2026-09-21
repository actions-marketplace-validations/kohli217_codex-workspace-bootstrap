# Security Policy

## Supported versions

The latest release and the default branch receive security fixes.

## Reporting a vulnerability

Do not post credentials, tokens, private repository contents, or exploit details in a public issue.

For ordinary security hardening suggestions that do not disclose a vulnerability, open a GitHub issue with a minimal reproducible description.

For vulnerabilities that would expose user data or credentials, use GitHub's private vulnerability reporting feature when it is enabled for this repository.

## Scope

The CLI performs local repository and toolchain inspection. The core audit path is designed not to transmit repository contents over the network.

Secret-risk detection is filename-based in the initial release. A passing result is not a security guarantee.
