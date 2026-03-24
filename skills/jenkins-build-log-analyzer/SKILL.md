---
name: "Jenkins Build Log Analyzer"
description: "Parses Jenkins build console logs via the Jenkins Remote Access API to extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics and the Jenkins Test Results API to correlate failures with specific changes. Outputs a triage report ranked by recurrence frequency."
category: "Runbooks & Diagnostics"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 4.9
reviews: 30
creator: "Mia Zhang"
creator_handle: "@miazhang"
creator_verified: true
source: "https://agentskillexchange.com/skills/jenkins-build-log-analyzer/"
---
# Jenkins Build Log Analyzer

Parses Jenkins build console logs via the Jenkins Remote Access API to extract failure patterns, stack traces, and flaky test signatures. Uses regex heuristics and the Jenkins Test Results API to correlate failures with specific changes. Outputs a triage report ranked by recurrence frequency.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | Runbooks & Diagnostics |
| Framework | ChatGPT Agents |
| Verification | Security Reviewed |
| Rating | 4.9/5 (30 reviews) |

## Creator

**Mia Zhang** (Verified Creator ✓)
- Profile: [@miazhang](https://agentskillexchange.com/browse-skills/?creator=miazhang)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-build-log-analyzer/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
