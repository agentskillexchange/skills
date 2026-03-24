---
name: "Secrets Scanner for Git Repositories"
description: "Wraps Gitleaks and TruffleHog in a unified scan pipeline targeting both commit history and working tree. Deduplicates findings across tools, enriches each result with committer identity and timestamp, and suppresses known false positives via allowlist. Outputs SARIF-compatible JSON for GitHub Advanced Security."
category: "Security & Verification"
framework: "ChatGPT Agents"
verification: listed
rating: 4.5
reviews: 44
creator: "Leo Park"
creator_handle: "@leopark"
creator_verified: true
source: "https://agentskillexchange.com/skills/secrets-scanner-git-repositories/"
---
# Secrets Scanner for Git Repositories

Wraps Gitleaks and TruffleHog in a unified scan pipeline targeting both commit history and working tree. Deduplicates findings across tools, enriches each result with committer identity and timestamp, and suppresses known false positives via allowlist. Outputs SARIF-compatible JSON for GitHub Advanced Security.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill secrets-scanner-git-repositories
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill secrets-scanner-git-repositories -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill secrets-scanner-git-repositories -a cursor
```

### OpenClaw

```bash
clawhub install secrets-scanner-git-repositories
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill secrets-scanner-git-repositories -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Security & Verification |
| Framework | ChatGPT Agents |
| Verification | Listed |
| Rating | 4.5/5 (44 reviews) |

## Creator

**Leo Park** (Verified Creator ✓)
- Profile: [@leopark](https://agentskillexchange.com/browse-skills/?creator=leopark)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/secrets-scanner-git-repositories/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
