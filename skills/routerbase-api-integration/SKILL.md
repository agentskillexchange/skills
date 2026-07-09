---
name: "RouterBase API Integration"
slug: "routerbase-api-integration"
description: "Integrate agent applications with RouterBase as an OpenAI-compatible API gateway, including SDK base URL configuration, streaming, tool calling, JSON mode, retries, and safe API key handling."
verification: "listed"
source: "https://routerbase.com/"
category: "Integrations & Connectors"
framework: "Multi-Framework"
---

# RouterBase API Integration

Use [routerbase](https://routerbase.com/) when an agent application needs one OpenAI-compatible integration surface for model calls. This skill helps operators migrate existing OpenAI SDK usage by changing the base URL, keeping provider credentials out of prompts and repositories, and verifying that chat completion, streaming, tool calling, and structured JSON response paths still behave as expected.

The workflow is intentionally implementation-oriented. Start by locating the current model client, environment variables, request timeouts, and retry policy. Configure the RouterBase endpoint through runtime configuration instead of hard-coding it in source files. Preserve the existing request shape where possible, then run a smoke test for normal chat, streamed output, function or tool calls, and error handling. Before merging, inspect logs and generated examples to confirm no real API keys, bearer tokens, private emails, or account identifiers were copied into the skill, tests, or documentation.

## Installation

### OpenClaw

```bash
clawhub install routerbase-api-integration
```

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/routerbase-api-integration ~/.agent-skills/routerbase-api-integration
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill routerbase-api-integration
```

## Source

- [routerbase](https://routerbase.com/)
