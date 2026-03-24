---
name: "Playwright Test Report to Slack"
description: "Parses Playwright HTML and JSON test reports and posts structured summaries to Slack using the Slack Web API. Reads test results from the playwright-report directory, extracts pass/fail/flaky counts using the @playwright/test reporter API, and posts rich Block Kit messages with test suite breakdowns via chat.postMessage."
category: "CI/CD Integrations"
framework: "ChatGPT Agents"
verification: security_reviewed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/playwright-test-report-to-slack/"
tool_ecosystem:
  tool: "playwright"
  github_stars: 84874
  npm_weekly_downloads: 39806814
  github_repo: "microsoft/playwright"
  license: "Apache-2.0"
  maintained: true
---

# Playwright Test Report to Slack

Parses Playwright HTML and JSON test reports and posts structured summaries to Slack using the Slack Web API. Reads test results from the playwright-report directory, extracts pass/fail/flaky counts using the @playwright/test reporter API, and posts rich Block Kit messages with test suite breakdowns via chat.postMessage.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill playwright-test-report-to-slack
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill playwright-test-report-to-slack -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill playwright-test-report-to-slack -a cursor
```

### OpenClaw
```bash
clawhub install playwright-test-report-to-slack
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill playwright-test-report-to-slack -a codex
```

## Details

| | |
|---|---|
| **Category** | CI/CD Integrations |
| **Framework** | ChatGPT Agents |
| **Verification** | 🛡️ Security Reviewed |
| **Tool** | [playwright](https://github.com/microsoft/playwright) — ⭐ 84.9k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/playwright-test-report-to-slack/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
