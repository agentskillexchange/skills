---
name: "SonarQube Gate Enforcer"
description: "Enforces SonarQube quality gate conditions in CI pipelines using the SonarQube Web API /api/qualitygates/project_status endpoint. Blocks merges when coverage drops, duplications exceed thresholds, or new bugs are introduced."
category: "Code Quality & Review"
framework: "Cursor"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sonarqube-gate-enforcer/"
tool_ecosystem:
  tool: "sonarqube"
  github_stars: 10357
  npm_weekly_downloads: 0
  github_repo: "SonarSource/sonarqube"
  license: "LGPL-3.0"
  maintained: true
---

# SonarQube Gate Enforcer

Enforces SonarQube quality gate conditions in CI pipelines using the SonarQube Web API /api/qualitygates/project_status endpoint. Blocks merges when coverage drops, duplications exceed thresholds, or new bugs are introduced.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill sonarqube-gate-enforcer
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill sonarqube-gate-enforcer -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill sonarqube-gate-enforcer -a cursor
```

### OpenClaw
```bash
clawhub install sonarqube-gate-enforcer
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill sonarqube-gate-enforcer -a codex
```

## Details

| | |
|---|---|
| **Category** | Code Quality & Review |
| **Framework** | Cursor |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [sonarqube](https://github.com/SonarSource/sonarqube) — ⭐ 10.4k · LGPL-3.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-gate-enforcer/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
