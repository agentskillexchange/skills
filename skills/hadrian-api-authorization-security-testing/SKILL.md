---
title: "Test API authorization flows with Hadrian"
description: "Use Hadrian when an agent needs to test API authorization behavior instead of merely calling endpoints. It fits review and release workflows where the agent should replay requests as different roles, compare allowed versus denied actions, and surface OWASP API Top 10 issues such as broken object-level authorization, broken function-level authorization, and broken authentication across REST, GraphQL, and gRPC services. This is skill-shaped because the workflow is narrow and operational: validate access-control boundaries with template-driven API tests and mutation-style verification. It is not a generic pentest platform, full DAST suite, or catch-all security product listing. Invoke it when the agent needs to verify role boundaries and authorization logic inside an API workflow."
source: "https://github.com/praetorian-inc/hadrian"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "praetorian-inc/hadrian"
  github_stars: 38
---

# Test API authorization flows with Hadrian

Use Hadrian when an agent needs to test API authorization behavior instead of merely calling endpoints. It fits review and release workflows where the agent should replay requests as different roles, compare allowed versus denied actions, and surface OWASP API Top 10 issues such as broken object-level authorization, broken function-level authorization, and broken authentication across REST, GraphQL, and gRPC services. This is skill-shaped because the workflow is narrow and operational: validate access-control boundaries with template-driven API tests and mutation-style verification. It is not a generic pentest platform, full DAST suite, or catch-all security product listing. Invoke it when the agent needs to verify role boundaries and authorization logic inside an API workflow.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hadrian-api-authorization-security-testing/)
