---
title: "Broker API credentials to AI agents without exposing raw keys using OneCLI"
description: "Store credentials once, then inject them into outbound agent requests at runtime so agents can call services without receiving raw secrets."
verification: "security_reviewed"
source: "https://github.com/onecli/onecli"
author: "onecli"
publisher_type: "open_source_project"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "onecli/onecli"
  github_stars: 1859
---

# Broker API credentials to AI agents without exposing raw keys using OneCLI

Store credentials once, then inject them into outbound agent requests at runtime so agents can call services without receiving raw secrets.

## Prerequisites

OneCLI gateway and dashboard, stored service credentials, AI agents making HTTP calls through the gateway

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
curl -fsSL https://onecli.sh/install | sh
```

## Documentation

- https://onecli.sh/docs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/broker-api-credentials-to-ai-agents-without-exposing-raw-keys-using-onecli/)
