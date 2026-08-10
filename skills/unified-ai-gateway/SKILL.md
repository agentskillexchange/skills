---
name: "Unified AI System Gateway"
slug: "unified-ai-gateway"
description: "Turn plain-language requests into structured, reviewable prompts and inspect a self-hosted MCP gateway with provider-free defaults."
category: "Developer Tools"
framework: "Codex"
verification: listed
source: "https://github.com/happy520ai/unified-ai-system"
---

# Unified AI System Gateway

Use this skill when a Codex workflow needs a self-hosted MCP gateway that makes
ordinary language more precise before an agent acts. Unified AI System keeps
the original request visible, compiles execution requirements, output
constraints, clarification questions, and completion criteria, then exposes
the result through a provider-free local path.

## What it provides

- A published MCP stdio server with nine bounded tools.
- Deterministic prompt enhancement through `gateway_prompt_enhance`.
- Health and readiness checks before chat or workflow operations.
- A local fake-provider default that requires no provider key or account.
- Explicit evidence fields such as `providerCalled`, `deterministic`, detected
  signals, and compiled sections.

## Safe first run

Install the published MCP server only after reviewing the command and asking
for approval to change the local Codex configuration:

```bash
codex mcp add unified-ai-system -- docker run --rm -i ghcr.io/happy520ai/unified-ai-system/mcp-server:0.4.8
```

Restart Codex, inspect the server with `/mcp verbose`, and call
`gateway_health` followed by `gateway_readiness` before using chat. Keep the
fake-provider mode for the first run. Never add provider keys to a public
configuration, and do not infer production readiness, L5 autonomy, or AGI
from a successful MCP handshake.

Project documentation and the provider-free verification workflow are available
at https://github.com/happy520ai/unified-ai-system.
