---
name: "SonarQube Scanner Skill"
description: "Integrates SonarQube static analysis via the sonar-scanner CLI and SonarQube Web API. Fetches quality gate results from api/qualitygates/project_status, parses issues via api/issues/search, and maps findings to source lines for inline code review annotations."
category: "Code Quality & Review"
framework: "Claude Code"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sonarqube-scanner-skill/"
tool_ecosystem:
  tool: "sonarqube"
  github_stars: 10357
  npm_weekly_downloads: 0
  github_repo: "SonarSource/sonarqube"
  license: "LGPL-3.0"
  maintained: true
---

# SonarQube Scanner Skill

Integrates SonarQube static analysis via the sonar-scanner CLI and SonarQube Web API. Fetches quality gate results from api/qualitygates/project_status, parses issues via api/issues/search, and maps findings to source lines for inline code review annotations.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill sonarqube-scanner-skill
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill sonarqube-scanner-skill -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill sonarqube-scanner-skill -a cursor
```

### OpenClaw
```bash
clawhub install sonarqube-scanner-skill
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill sonarqube-scanner-skill -a codex
```

## Details

| | |
|---|---|
| **Category** | Code Quality & Review |
| **Framework** | Claude Code |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [sonarqube](https://github.com/SonarSource/sonarqube) — ⭐ 10.4k · LGPL-3.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/sonarqube-scanner-skill/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
