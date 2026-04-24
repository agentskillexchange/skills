---
title: "Repair malformed JSON before parsing downstream automations with jsonrepair"
description: "Use jsonrepair when an agent receives JSON-like output that is almost valid but still breaks parsers, such as trailing commas, missing quotes, or concatenated fragments. The agent’s role is to normalize the payload before validation or routing, not to replace real schema design."
verification: "security_reviewed"
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

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/repair-malformed-json-before-parsing-downstream-automations-jsonrepair/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/repair-malformed-json-before-parsing-downstream-automations-jsonrepair
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/repair-malformed-json-before-parsing-downstream-automations-jsonrepair`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/repair-malformed-json-before-parsing-downstream-automations-jsonrepair/)
