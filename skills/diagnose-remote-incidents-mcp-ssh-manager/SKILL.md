---
name: "Diagnose remote server incidents with MCP SSH Manager before changing services"
slug: "diagnose-remote-incidents-mcp-ssh-manager"
description: "Collect host health, service status, bounded logs and process evidence through SSH tools before proposing a scoped repair."
verification: "security_reviewed"
source: "https://github.com/bvisible/mcp-ssh-manager/blob/main/skills/ssh-incident/SKILL.md"
author: "MCP SSH Manager Contributors"
publisher_type: "Open Source Project"
category: "Runbooks & Diagnostics"
framework: "MCP"
---

# Diagnose remote server incidents with MCP SSH Manager before changing services

Collect host health, service status, bounded logs and process evidence through SSH tools before proposing a scoped repair.

## Prerequisites

Node.js 18+, npm, an MCP client, authorized SSH host credentials and MCP SSH Manager

## Installation

Install or set up from the source-backed instructions:

npm install -g mcp-ssh-manager ssh-manager server add Register command mcp-ssh-manager in your MCP client; the upstream Claude Code example is: claude mcp add ssh-manager mcp-ssh-manager Load skills/ssh-incident/SKILL.md from the upstream repository. Configure per-server approval in the control interface if required.

- Source: https://github.com/bvisible/mcp-ssh-manager/blob/main/skills/ssh-incident/SKILL.md

## Documentation

- https://github.com/bvisible/mcp-ssh-manager/blob/main/skills/ssh-incident/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/diagnose-remote-incidents-mcp-ssh-manager/)
