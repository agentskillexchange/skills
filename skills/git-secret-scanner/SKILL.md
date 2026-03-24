---
name: "Git Secret Scanner"
description: "Detects leaked secrets in Git repositories using pattern-based scanning with Gitleaks rule definitions and the GitHub Secret Scanning API. Identifies exposed API keys, tokens, and credentials across full commit history using git log –all -p analysis."
category: "Security & Verification"
framework: "Claude Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/git-secret-scanner/"
tool_ecosystem:
  tool: "stripe"
  github_stars: 4377
  npm_weekly_downloads: 8442269
  github_repo: "stripe/stripe-node"
  license: "MIT"
  maintained: true
---

# Git Secret Scanner

Detects leaked secrets in Git repositories using pattern-based scanning with Gitleaks rule definitions and the GitHub Secret Scanning API. Identifies exposed API keys, tokens, and credentials across full commit history using git log –all -p analysis.

## Installation

### Any Agent (npx)
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

| | |
|---|---|
| **Category** | Security & Verification |
| **Framework** | Claude Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [stripe](https://github.com/stripe/stripe-node) — ⭐ 4.4k · MIT |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/git-secret-scanner/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
