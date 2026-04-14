---
title: "Test API authorization flows with Hadrian"
description: "Lets an agent exercise REST, GraphQL, and gRPC authorization paths with YAML-defined role tests so BOLA, BFLA, broken authentication, and related API flaws are caught before release."
verification: listed
source: "https://github.com/praetorian-inc/hadrian"
category:
  - "Security &amp; Verification"
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

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hadrian-api-authorization-security-testing/)
