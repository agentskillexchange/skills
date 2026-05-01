---
title: "Test API authorization flows with Hadrian"
description: "Lets an agent exercise REST, GraphQL, and gRPC authorization paths with YAML-defined role tests so BOLA, BFLA, broken authentication, and related API flaws are caught before release."
verification: "listed"
source: "https://github.com/praetorian-inc/hadrian"
author: "Praetorian"
publisher_type: "company"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "praetorian-inc/hadrian"
  github_stars: 38
---

# Test API authorization flows with Hadrian

Lets an agent exercise REST, GraphQL, and gRPC authorization paths with YAML-defined role tests so BOLA, BFLA, broken authentication, and related API flaws are caught before release.

## Prerequisites

Go or a prebuilt Hadrian binary, plus a target API definition or endpoint and role/auth configuration files such as roles.yaml and auth.yaml.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
<p>Install from source with <code>go install github.com/praetorian-inc/hadrian/cmd/hadrian@latest</code>, or download a prebuilt binary from the repository releases. Supply the target API plus <code>roles.yaml</code> and <code>auth.yaml</code>, then run <code>hadrian test rest</code>, <code>hadrian test graphql</code>, or <code>hadrian test grpc</code> for the protocol you need to verify.</p>
```

## Documentation

- https://github.com/praetorian-inc/hadrian#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hadrian-api-authorization-security-testing/)
