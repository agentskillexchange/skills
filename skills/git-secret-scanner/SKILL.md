---
name: "Git Secret Scanner"
description: "Detects leaked secrets in Git repositories using pattern-based scanning with Gitleaks rule definitions and the GitHub Secret Scanning API. Identifies exposed API keys, tokens, and credentials across full commit history using git log –all -p analysis."
category: "Security & Verification"
framework: "Claude Agents"
verification: security_reviewed
rating: 4.3
reviews: 56
creator: David Kim
creator_handle: dkim
creator_verified: false
source: https://agentskillexchange.com/skill/git-secret-scanner/
---

# Git Secret Scanner

Detects leaked secrets in Git repositories using pattern-based scanning with Gitleaks rule definitions and the GitHub Secret Scanning API. Identifies exposed API keys, tokens, and credentials across full commit history using git log –all -p analysis.

## Installation

### Any agent (npx skills)

```bash
npx skills add agentskillexchange/skills --skill git-secret-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill git-secret-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill git-secret-scanner -a cursor
```

### OpenClaw

```bash
clawhub install git-secret-scanner
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill git-secret-scanner -a codex
```

## Details

| Field | Value |
|-------|-------|
| Category | Security & Verification |
| Framework | Claude Agents |
| Verification | Security Reviewed |
| Rating | 4.3/5 (56 reviews) |

## Creator

**David Kim**
- Profile: [@dkim](https://agentskillexchange.com/browse-skills/?creator=dkim)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/git-secret-scanner/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
