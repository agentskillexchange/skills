---
name: "Jenkins Build Log Analyzer"
description: "Parses Jenkins build console logs via the Jenkins Remote Access API to extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics and the Jenkins Test Results API to correlate failures with specific changes. Outputs a triage report ranked by recurrence frequency."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/jenkins-build-log-analyzer/"
tool_ecosystem:
  tool: "jenkins"
  github_stars: 25122
  npm_weekly_downloads: 0
  github_repo: "jenkinsci/jenkins"
  license: "MIT"
  maintained: true
---

# Jenkins Build Log Analyzer

Parses Jenkins build console logs via the Jenkins Remote Access API to extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics and the Jenkins Test Results API to correlate failures with specific changes. Outputs a triage report ranked by recurrence frequency.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill jenkins-build-log-analyzer
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill jenkins-build-log-analyzer -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill jenkins-build-log-analyzer -a cursor
```

### OpenClaw
```bash
clawhub install jenkins-build-log-analyzer
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill jenkins-build-log-analyzer -a codex
```

## Details

| | |
|---|---|
| **Category** | Runbooks & Diagnostics |
| **Framework** | ChatGPT Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [jenkins](https://github.com/jenkinsci/jenkins) — ⭐ 25.1k · MIT |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-build-log-analyzer/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
