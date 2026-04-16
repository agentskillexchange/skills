---
title: "Test API authorization flows with Hadrian"
description: "Lets an agent exercise REST, GraphQL, and gRPC authorization paths with YAML-defined role tests so BOLA, BFLA, broken authentication, and related API flaws are caught before release."
verification: "listed"
source: "https://github.com/praetorian-inc/hadrian"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "praetorian-inc/hadrian"
  github_stars: 38
---

# Test API authorization flows with Hadrian

Use Hadrian when an agent needs to test API authorization behavior instead of merely calling endpoints. It fits review and release workflows where the agent should replay requests as different roles, compare allowed versus denied actions, and surface OWASP API Top 10 issues such as broken object-level authorization, broken function-level authorization, and broken authentication across REST, GraphQL, and gRPC services.


This is skill-shaped because the workflow is narrow and operational: validate access-control boundaries with template-driven API tests and mutation-style verification. It is not a generic pentest platform, full DAST suite, or catch-all security product listing. Invoke it when the agent needs to verify role boundaries and authorization logic inside an API workflow.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hadrian-api-authorization-security-testing/)
