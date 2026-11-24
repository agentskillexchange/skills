---
name: "Inspect and recover a blocked coding-agent terminal through Facade MCP"
slug: "inspect-recover-blocked-coding-agent-terminal-facade-mcp"
description: "Diagnose one blocked Facade agent from its terminal evidence, perform an explicitly authorized response, and verify the observed recovery without duplicating work."
github_stars: 535
verification: "security_reviewed"
source: "https://github.com/y5ez3g/facadecode"
author: "y5ez3g"
publisher_type: "individual"
category: "Runbooks & Diagnostics"
framework: "MCP"
tool_ecosystem:
  github_repo: "y5ez3g/facadecode"
  github_stars: 535
---

# Inspect and recover a blocked coding-agent terminal through Facade MCP

Diagnose one blocked Facade agent from its terminal evidence, perform an explicitly authorized response, and verify the observed recovery without duplicating work.

## Prerequisites

Existing Facade Orchestrator and facade-mcp connection; list_agents and read_screen; type_text, press_keys or send_message only for authorized intervention

## Installation

Install or set up from the source-backed instructions:

Install the official Facade Code VS Code extension with code --install-extension facade.facadecode, or use the upstream supported installation guide. Configure at least one supported signed-in coding CLI where the workspace runs. Use the existing Orchestrator and its documented facade-mcp entry point in a compatible MCP client; confirm list_agents and read_screen are available. Review the documented YOLO default and native CLI permission behavior before starting workers. This workflow operates an existing worker and does not install software, start workers or alter permissions during invocation. See https://github.com/y5ez3g/facadecode/blob/5c2008e65d691687438cd5781ba2dffadf97dfe3/extension/README.md and https://github.com/y5ez3g/facadecode/blob/5c2008e65d691687438cd5781ba2dffadf97dfe3/docs/PRODUCT.md#mcp.

- Source: https://github.com/y5ez3g/facadecode

## Documentation

- https://github.com/y5ez3g/facadecode/blob/5c2008e65d691687438cd5781ba2dffadf97dfe3/framework/crates/base/src/texts/skill.rs

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-recover-blocked-coding-agent-terminal-facade-mcp/)
