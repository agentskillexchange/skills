---
name: "Unified AI System Gateway"
slug: "unified-ai-gateway"
description: "Turn plain-language requests into structured, reviewable prompts and inspect a self-hosted MCP gateway with provider-free defaults."
verification: "listed"
source: "https://github.com/happy520ai/unified-ai-system/tree/master/skills/unified-ai-gateway"
category: "Developer Tools"
framework: "Codex"
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

Treat this catalog entry as a discovery document, not as authorization to pull
an image, create a container, or modify Codex configuration. The upstream
official skill classifies the integration as `risk: critical` and defines the
required review and approval sequence:

- Official skill and guarded setup procedure:
  https://github.com/happy520ai/unified-ai-system/tree/master/skills/unified-ai-gateway
- Reviewed immutable image identity and residual risks:
  https://github.com/happy520ai/unified-ai-system/blob/master/docs/security/mcp-image-review-0.4.9.md
- MCP behavior and provider-free verification guide:
  https://github.com/happy520ai/unified-ai-system/blob/master/packages/mcp-server/README.md

Follow that procedure exactly. Keep image download and non-executing content
inspection under one explicit approval, then obtain separate approval before
MCP registration or activation. Do not replace the reviewed digest with a
mutable tag, enable container networking, mount host paths, pass credentials,
or activate an unreviewed platform.

After an approved installation, restart Codex, inspect the server with
`/mcp verbose`, and call `gateway_health` followed by `gateway_readiness`
before using chat. Keep the fake-provider mode for the first run, and do not
infer production readiness, L5 autonomy, or AGI from a successful handshake.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/happy520ai/unified-ai-system/tree/master/skills/unified-ai-gateway
