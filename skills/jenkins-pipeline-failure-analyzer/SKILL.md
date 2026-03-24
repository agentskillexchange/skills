---
name: "Jenkins Pipeline Failure Analyzer"
description: "Queries the Jenkins REST API /job/{name}/lastFailedBuild/api/json and /consoleText to diagnose pipeline failures. Parses Blue Ocean API /blue/rest/organizations for stage-level timing and error classification."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jenkins-pipeline-failure-analyzer/"
tool_ecosystem:
  tool: "jenkins"
  github_stars: 25122
  npm_weekly_downloads: 0
  github_repo: "jenkinsci/jenkins"
  license: "MIT"
  maintained: true
---

# Jenkins Pipeline Failure Analyzer

Queries the Jenkins REST API /job/{name}/lastFailedBuild/api/json and /consoleText to diagnose pipeline failures. Parses Blue Ocean API /blue/rest/organizations for stage-level timing and error classification.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-failure-analyzer
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-failure-analyzer -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-failure-analyzer -a cursor
```

### OpenClaw
```bash
clawhub install jenkins-pipeline-failure-analyzer
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill jenkins-pipeline-failure-analyzer -a codex
```

## Details

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | Claude Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [jenkins](https://github.com/jenkinsci/jenkins) — ⭐ 25.1k · MIT |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-failure-analyzer/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
