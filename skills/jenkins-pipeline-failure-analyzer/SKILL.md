---
name: "Jenkins Pipeline Failure Analyzer"
description: "Queries the Jenkins REST API /job/{name}/lastFailedBuild/api/json and /consoleText to diagnose pipeline failures. Parses Blue Ocean API /blue/rest/organizations for stage-level timing and error classification."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: "security_reviewed"
rating: 4.4
reviews: 72
creator: "Community"
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skill/jenkins-pipeline-failure-analyzer/"
---

# Jenkins Pipeline Failure Analyzer

Queries the Jenkins REST API /job/{name}/lastFailedBuild/api/json and /consoleText to diagnose pipeline failures. Parses Blue Ocean API /blue/rest/organizations for stage-level timing and error classification.

## Installation

Install this skill across different agents:

### Any AI Agent (npx)
```bash
npx @anthropic/skills install jenkins-pipeline-failure-analyzer
```

### Claude Code
```bash
claude skills install jenkins-pipeline-failure-analyzer
```

### Cursor
Add to `.cursor/skills.json`:
```json
{
  "skills": ["jenkins-pipeline-failure-analyzer"]
}
```

### OpenClaw
```bash
clawhub install jenkins-pipeline-failure-analyzer
```

### Codex
```bash
codex skills install jenkins-pipeline-failure-analyzer
```

## Details

| Field | Value |
|-------|-------|
| **Category** | CI/CD Integrations |
| **Framework** | Claude Agents |
| **Verification** | 🔒 Security Reviewed |
| **Rating** | ⭐⭐⭐⭐ 4.4/5 (72 reviews) |

## Creator

**Community**



## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skill/jenkins-pipeline-failure-analyzer/)
- [Browse All Skills](https://agentskillexchange.com/)
