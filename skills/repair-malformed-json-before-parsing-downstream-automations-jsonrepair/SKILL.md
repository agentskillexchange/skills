---
title: "Repair malformed JSON before parsing downstream automations with jsonrepair"
slug: "repair-malformed-json-before-parsing-downstream-automations-jsonrepair"
verification: security_reviewed
source: "https://github.com/josdejong/jsonrepair"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "josdejong/jsonrepair"
  github_stars: 2297
---
# Repair malformed JSON before parsing downstream automations with jsonrepair

Use jsonrepair when an agent receives JSON-like output that is almost valid but still breaks parsers, such as trailing commas, missing quotes, or concatenated fragments. The agent’s role is to normalize the payload before validation or routing, not to replace real schema design.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/repair-malformed-json-before-parsing-downstream-automations-jsonrepair/)
