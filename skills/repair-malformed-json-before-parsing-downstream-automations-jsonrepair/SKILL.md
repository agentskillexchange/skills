---
name: "repair-malformed-json-before-parsing-downstream-automations-jsonrepair"
title: "Repair malformed JSON before parsing downstream automations with jsonrepair"
description: "Use jsonrepair when an agent receives JSON-like output that is almost valid but still breaks parsers, such as trailing commas, missing quotes, or concatenated fragments. The agent’s role is to normalize the payload before validation or routing, not to replace real schema design."
category: "Developer Tools"
framework: "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/josdejong/jsonrepair"
tool_ecosystem:
  github_repo: "josdejong/jsonrepair"
  github_stars: 2296
---

# Repair malformed JSON before parsing downstream automations with jsonrepair

Use jsonrepair when an agent receives JSON-like output that is almost valid but still breaks parsers, such as trailing commas, missing quotes, or concatenated fragments. The agent’s role is to normalize the payload before validation or routing, not to replace real schema design.

## Installation

You can install this skill using any of these methods:

1. OpenClaw skill installer
2. ClawHub CLI
3. Git clone into your skills directory
4. Download and extract the skill folder manually
5. Copy the skill folder from a local checkout

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/repair-malformed-json-before-parsing-downstream-automations-jsonrepair/)
