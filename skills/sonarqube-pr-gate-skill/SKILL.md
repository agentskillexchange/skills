---
name: "SonarQube PR Gate"
description: "Integrates SonarQube quality gates into pull request workflows via the SonarQube Web API /api/qualitygates/project_status. Blocks merges when code smells, duplications, or coverage thresholds fail and posts inline annotations using the GitHub Checks API."
category: "Code Quality & Review"
framework: "Codex"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sonarqube-pr-gate-skill/"
tool_ecosystem:
  tool: "sonarqube"
  github_stars: 10357
  npm_weekly_downloads: 0
  github_repo: "SonarSource/sonarqube"
  license: "LGPL-3.0"
  maintained: true
---

# SonarQube PR Gate

Integrates SonarQube quality gates into pull request workflows via the SonarQube Web API /api/qualitygates/project_status. Blocks merges when code smells, duplications, or coverage thresholds fail and posts inline annotations using the GitHub Checks API.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill sonarqube-pr-gate-skill
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill sonarqube-pr-gate-skill -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill sonarqube-pr-gate-skill -a cursor
```

### OpenClaw
```bash
clawhub install sonarqube-pr-gate-skill
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill sonarqube-pr-gate-skill -a codex
```

## Details

| | |
|---|---|
| **Category** | Code Quality & Review |
| **Framework** | Codex |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [sonarqube](https://github.com/SonarSource/sonarqube) — ⭐ 10.4k · LGPL-3.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-pr-gate-skill/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
