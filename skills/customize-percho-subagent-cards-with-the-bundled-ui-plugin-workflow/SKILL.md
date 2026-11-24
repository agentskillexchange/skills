---
name: "Customize Percho subagent cards with the bundled UI plugin workflow"
slug: "customize-percho-subagent-cards-with-the-bundled-ui-plugin-workflow"
description: "Generate a TSX replacement for Percho subagent run cards, check host build feedback and themes, then hand off manual plugin enablement."
verification: "security_reviewed"
source: "https://github.com/Jaxton07/percho/blob/e45824bd8974043fc573c9fcc219bf97756936cc/packages/desktop/resources/ui-plugins/skills/percho-ui-plugin/SKILL.md"
author: "Jaxton07"
publisher_type: "individual"
category: "Developer Tools"
framework: "Custom Agents"
---

# Customize Percho subagent cards with the bundled UI plugin workflow

Generate a TSX replacement for Percho subagent run cards, check host build feedback and themes, then hand off manual plugin enablement.

## Prerequisites

Installed Percho desktop application with bundled UI plugin skill, SPEC.md and percho-ui.d.ts; local TypeScript/TSX editing; operator access to UI Plugins settings.

## Installation

Install or set up from the source-backed instructions:

Install the appropriate desktop build from Percho releases. Use the bundled UI plugin skill inside the Percho agent environment. Read the installed specification and types, then scaffold ~/.percho/ui-plugins//plugin.json and src/index.tsx. The host builds saved source. The operator must enable the UI Plugins switch and the individual plugin and confirm workspace trust; do not automate that confirmation.

- Source: https://github.com/Jaxton07/percho/blob/e45824bd8974043fc573c9fcc219bf97756936cc/packages/desktop/resources/ui-plugins/skills/percho-ui-plugin/SKILL.md

## Documentation

- https://github.com/Jaxton07/percho/blob/e45824bd8974043fc573c9fcc219bf97756936cc/packages/desktop/resources/ui-plugins/SPEC.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/customize-percho-subagent-cards-with-the-bundled-ui-plugin-workflow/)
