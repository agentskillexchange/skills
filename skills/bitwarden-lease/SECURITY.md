# Security policy

## Reporting a vulnerability

Please report vulnerabilities through GitHub's private vulnerability reporting
for this repository. Do not open a public issue containing credentials, vault
metadata, session material, private paths, or exploit details.

## Security invariants

Changes must preserve the contract in
[`references/security-contract.md`](references/security-contract.md). In
particular, the broker must never persist or return the master password,
`BW_SESSION`, or retrieved secrets; broaden its command allowlist; or weaken
owner-only permissions without an explicit security-design review.

The project is pre-1.0. Security fixes are made on the latest release line.
