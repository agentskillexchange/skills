---
name: "Convert browser HAR captures into reusable k6 load tests with har-to-k6"
slug: "convert-browser-har-captures-into-reusable-k6-load-tests-with-har-to-k6"
description: "Use har-to-k6 when an agent has recorded browser traffic and needs to turn it into a repeatable k6 script instead of hand-writing one from scratch. The skill is about transforming captured sessions into a starter load-test artifact with validation and export, not about listing k6 or Grafana as products."
github_stars: 159
verification: "security_reviewed"
source: "https://github.com/grafana/har-to-k6"
author: "Grafana Labs"
publisher_type: "Company"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "grafana/har-to-k6"
  github_stars: 159
---

# Convert browser HAR captures into reusable k6 load tests with har-to-k6

Use har-to-k6 when an agent has recorded browser traffic and needs to turn it into a repeatable k6 script instead of hand-writing one from scratch. The skill is about transforming captured sessions into a starter load-test artifact with validation and export, not about listing k6 or Grafana as products.

## Prerequisites

Node.js or Docker, a HAR or LI-HAR capture, and k6 for running the generated script

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
npm install --save-dev har-to-k6
```

## Documentation

- https://github.com/grafana/har-to-k6#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-browser-har-captures-into-reusable-k6-load-tests-with-har-to-k6/)
