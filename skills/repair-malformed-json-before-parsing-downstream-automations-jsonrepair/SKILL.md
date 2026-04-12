---
title: "Repair malformed JSON before parsing downstream automations with jsonrepair"
slug: "repair-malformed-json-before-parsing-downstream-automations-jsonrepair"
description: "Use jsonrepair when an agent receives JSON-like output that is almost valid but still breaks parsers, such as trailing commas, missing quotes, or concatenated fragments. The agent’s role is to normalize the payload before validation or routing, not to replace real schema design."
verification: security_reviewed
source: "https://github.com/josdejong/jsonrepair"
category:
  - "Developer Tools"
tool_ecosystem:
  github_repo: "https://github.com/josdejong/jsonrepair"
  github_stars: 2296
---

# Repair malformed JSON before parsing downstream automations with jsonrepair

Use jsonrepair when an agent receives JSON-like output that is almost valid but still breaks parsers, such as trailing commas, missing quotes, or concatenated fragments. The agent’s role is to normalize the payload before validation or routing, not to replace real schema design.

## Installation

Choose the setup path that fits your environment:

1. Install from the Agent Skill Exchange UI
2. Clone or download this skill into your skills directory
3. Install with your agent platform's skill manager, if supported
4. Vendor the skill into your workspace or repo
5. Copy the skill files manually for local customization

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/repair-malformed-json-before-parsing-downstream-automations-jsonrepair/)
