---
name: "npm Audit Dependency Report Generator"
description: "Generates comprehensive vulnerability reports from npm audit JSON output and the OSV (Open Source Vulnerabilities) API. Parses npm audit –json results, enriches each CVE with CVSS scores from the NVD REST API, and groups findings by severity. Produces SARIF output compatible with GitHub Advanced Security."
category: "CI/CD Integrations"
framework: "Claude Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/npm-audit-dependency-report-generator/"
tool_ecosystem:
  tool: "jira"
  github_stars: 0
  npm_weekly_downloads: 0
  github_repo: ""
  license: ""
  maintained: false
---

# npm Audit Dependency Report Generator

Generates comprehensive vulnerability reports from npm audit JSON output and the OSV (Open Source Vulnerabilities) API. Parses npm audit –json results, enriches each CVE with CVSS scores from the NVD REST API, and groups findings by severity. Produces SARIF output compatible with GitHub Advanced Security.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill npm-audit-dependency-report-generator
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill npm-audit-dependency-report-generator -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill npm-audit-dependency-report-generator -a cursor
```

### OpenClaw
```bash
clawhub install npm-audit-dependency-report-generator
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill npm-audit-dependency-report-generator -a codex
```

## Details

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | Claude Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | jira |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/npm-audit-dependency-report-generator/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
