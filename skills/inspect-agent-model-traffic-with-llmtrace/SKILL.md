---
title: "Inspect agent model traffic with LLMTrace"
slug: "inspect-agent-model-traffic-with-llmtrace"
description: "Proxy OpenAI-compatible model traffic so operators can inspect prompts, detect risks, and enforce budget or policy controls."
github_stars: 46
verification: "security_reviewed"
source: "https://github.com/epappas/llmtrace"
author: "epappas"
publisher_type: "individual"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "epappas/llmtrace"
  github_stars: 46
---

# Inspect agent model traffic with LLMTrace

Proxy OpenAI-compatible model traffic so operators can inspect prompts, detect risks, and enforce budget or policy controls.

## Prerequisites

Rust or Docker runtime, OpenAI-compatible client or SDK

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `curl -sS https://raw.githubusercontent.com/epappas/llmtrace/main/scripts/install.sh | bash` or `cargo install llmtrace`, run `llmtrace-proxy --config config.yaml`, then point your OpenAI-compatible client at the local proxy base URL.
```

## Documentation

- https://github.com/epappas/llmtrace/tree/main/docs/getting-started

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-agent-model-traffic-with-llmtrace/)
