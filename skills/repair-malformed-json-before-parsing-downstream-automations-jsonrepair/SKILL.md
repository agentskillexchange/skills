---
title: "Repair malformed JSON before parsing downstream automations with jsonrepair"
slug: "repair-malformed-json-before-parsing-downstream-automations-jsonrepair"
description: "Use jsonrepair when an agent receives JSON-like output that is almost valid but still breaks parsers, such as trailing commas, missing quotes, or concatenated fragments. The agent’s role is to normalize the payload before validation or routing, not to replace real schema design."
category: "Developer Tools"
framework: "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/josdejong/jsonrepair"
---

# Repair malformed JSON before parsing downstream automations with jsonrepair

Use jsonrepair when an agent receives JSON-like output that is almost valid but still breaks parsers, such as trailing commas, missing quotes, or concatenated fragments. The agent’s role is to normalize the payload before validation or routing, not to replace real schema design.

## Installation

Choose the setup path that fits your environment:

1. Clone or download this skill into your skills directory.
2. Install it through your agent platform's skill manager if supported.
3. Add it as a Git submodule or vendored folder in your repo.
4. Copy the files into a local custom skills/workspace directory.
5. Pull it from the Agent Skill Exchange catalog or this GitHub repo.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/repair-malformed-json-before-parsing-downstream-automations-jsonrepair/)
