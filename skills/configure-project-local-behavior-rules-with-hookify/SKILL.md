---
name: "Configure project-local behavior rules from operator corrections with Hookify"
slug: "configure-project-local-behavior-rules-with-hookify"
description: "Turn repeated Claude Code corrections into operator-confirmed local rules, with specific event matchers, warning or blocking actions, and reviewable Markdown configuration."
verification: "security_reviewed"
source: "https://github.com/anthropics/claude-plugins-official/tree/main/plugins/hookify"
author: "Anthropic"
publisher_type: "organization"
category: "Developer Tools"
framework: "Claude Code"
---

# Configure project-local behavior rules from operator corrections with Hookify

Turn repeated Claude Code corrections into operator-confirmed local rules, with specific event matchers, warning or blocking actions, and reviewable Markdown configuration.

## Prerequisites

Claude Code; Python 3.7+; Hookify plugin; project-local .claude directory

## Installation

Install or set up from the source-backed instructions:

In Claude Code, run /plugin install hookify@claude-plugins-official using the official marketplace. Ensure Python 3.7+ is available. In the target project invoke /hookify with the behavior to address, confirm the selected patterns and warn/block action, then review the generated .claude/hookify.{rule-name}.local.md files. Use /hookify:list and /hookify:configure to inspect and toggle rules. No installation or invocation was executed during discovery.

- Source: https://github.com/anthropics/claude-plugins-official/tree/main/plugins/hookify

## Documentation

- https://github.com/anthropics/claude-plugins-official/blob/main/plugins/hookify/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/configure-project-local-behavior-rules-with-hookify/)
