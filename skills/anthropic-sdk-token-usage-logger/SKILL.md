---
name: "Anthropic SDK Token Usage Logger"
description: "Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient."
category: "Library & API Reference"
framework: "Claude Code"
verification: verified_metadata
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/"
tool_ecosystem:
  tool: "aws"
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: "aws/aws-sdk-js-v3"
  license: "Apache-2.0"
  maintained: true
---

# Anthropic SDK Token Usage Logger

Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient.

## Installation

### Any Agent (npx)
```bash
npx skills add agentskillexchange/skills --skill anthropic-sdk-token-usage-logger
```

### Claude Code
```bash
npx skills add agentskillexchange/skills --skill anthropic-sdk-token-usage-logger -a claude-code
```

### Cursor
```bash
npx skills add agentskillexchange/skills --skill anthropic-sdk-token-usage-logger -a cursor
```

### OpenClaw
```bash
clawhub install anthropic-sdk-token-usage-logger
```

### Codex
```bash
npx skills add agentskillexchange/skills --skill anthropic-sdk-token-usage-logger -a codex
```

## Details

| | |
|---|---|
| **Category** | Library & API Reference |
| **Framework** | Claude Code |
| **Verification** | ✅ Verified Metadata |
| **Tool** | [aws](https://github.com/aws/aws-sdk-js-v3) — ⭐ 3.6k · Apache-2.0 |

---

*[View on Agent Skill Exchange](https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/) · [Browse all skills](https://agentskillexchange.com/browse-skills/)*
