---
title: "Test API authorization flows with Hadrian"
description: "Use Hadrian when an agent needs to test API authorization behavior instead of merely calling endpoints. It fits review and release workflows where the agent should replay requests as different roles, compare allowed versus denied actions, and surface OWASP API Top 10 issues such as broken object-level authorization, broken function-level authorization, and broken authentication across REST, GraphQL, and gRPC services.\nThis is skill-shaped because the workflow is narrow and operational: validate access-control boundaries with template-driven API tests and mutation-style verification. It is not a generic pentest platform, full DAST suite, or catch-all security product listing. Invoke it when the agent needs to verify role boundaries and authorization logic inside an API workflow."
verification: listed
source: "https://github.com/praetorian-inc/hadrian"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/hadrian-api-authorization-security-testing
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/hadrian-api-authorization-security-testing` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/hadrian-api-authorization-security-testing/)
