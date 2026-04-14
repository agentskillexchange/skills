---
title: "Convert browser HAR captures into reusable k6 load tests with har-to-k6"
description: "Use har-to-k6 when an agent has recorded browser traffic and needs to turn it into a repeatable k6 script instead of hand-writing one from scratch. The skill is about transforming captured sessions into a starter load-test artifact with validation and export, not about listing k6 or Grafana as products."
verification: security_reviewed
source: "https://github.com/grafana/har-to-k6"
category:
  - "Templates &amp; Workflows"
---

# Convert browser HAR captures into reusable k6 load tests with har-to-k6

Use har-to-k6 when an agent has recorded browser traffic and needs to turn it into a repeatable k6 script instead of hand-writing one from scratch. The skill is about transforming captured sessions into a starter load-test artifact with validation and export, not about listing k6 or Grafana as products.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/convert-browser-har-captures-into-reusable-k6-load-tests-with-har-to-k6/)
