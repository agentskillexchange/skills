---
title: "Repair malformed JSON before parsing downstream automations with jsonrepair"
description: "Use jsonrepair when an agent receives JSON-like output that is almost valid but still breaks parsers, such as trailing commas, missing quotes, or concatenated fragments. The agent’s role is to normalize the payload before validation or routing, not to replace real schema design."
verification: listed
source: "https://agentskillexchange.com/skills/repair-malformed-json-before-parsing-downstream-automations-jsonrepair/"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
---

# Repair malformed JSON before parsing downstream automations with jsonrepair

Use jsonrepair when an agent receives JSON-like output that is almost valid but still breaks parsers, such as trailing commas, missing quotes, or concatenated fragments. The agent’s role is to normalize the payload before validation or routing, not to replace real schema design.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/repair-malformed-json-before-parsing-downstream-automations-jsonrepair/)
