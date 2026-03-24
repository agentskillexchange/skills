---
name: "Anthropic SDK Token Usage Logger"
description: "Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient."
category: "Library & API Reference"
framework: "Claude Code"
verification: verified_metadata
rating: 4.9
reviews: 83
creator: "Priya Sharma"
creator_handle: "@priyasharma"
creator_verified: true
source: "https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/"
---
# Anthropic SDK Token Usage Logger

Instruments Anthropic API calls to log token usage, latency, and cost per request using the Anthropic TypeScript SDK. Wraps the anthropic.messages.create method to capture usage.input_tokens, usage.output_tokens, and timing from the API response. Writes structured logs to CloudWatch Logs via the AWS SDK v3 CloudWatchLogsClient.

## Installation

### Any agent (npx skills)

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

| Field | Value |
|-------|-------|
| Category | Library & API Reference |
| Framework | Claude Code |
| Verification | Verified Metadata |
| Rating | 4.9/5 (83 reviews) |

## Creator

**Priya Sharma** (Verified Creator ✓)
- Profile: [@priyasharma](https://agentskillexchange.com/browse-skills/?creator=priyasharma)

## Links

- [View on Agent Skill Exchange](https://agentskillexchange.com/skills/anthropic-sdk-token-usage-logger/)
- [Browse all skills](https://agentskillexchange.com/browse-skills/)
