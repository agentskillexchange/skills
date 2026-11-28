---
name: "Complete website tasks in Comma’s native desktop browser"
slug: "complete-website-tasks-in-comma-native-desktop-browser"
description: "Invoke Comma’s browser-use skill for a bounded website task on the initiating desktop, with action receipts, user handoffs and tab cleanup."
verification: "security_reviewed"
source: "https://github.com/AFK-surf/Comma/tree/c138b5cc767f211d162af7a04ba8ee544bf6a54a/resources/salix-system-files/skills/browser-use"
author: "AFK AI, Inc."
publisher_type: "open_source"
category: "Browser Automation"
framework: "Custom Agents"
---

# Complete website tasks in Comma’s native desktop browser

Invoke Comma’s browser-use skill for a bounded website task on the initiating desktop, with action receipts, user handoffs and tab cleanup.

## Prerequisites

Comma desktop app and connected Salix runtime; device.list, device.get, env.exec and the runtime-provided comma in-app-browser commands. User participation for site authentication and confirmations.

## Installation

Install or set up from the source-backed instructions:

Install and configure the Comma desktop app using https://comma.surf/download and connect its desktop environment. Comma ships browser-use as a read-only built-in skill; no separate npm package or MCP server is required. In a Comma conversation tag /browser-use and specify one website task. Confirm availability with comma describe in-app-browser inside the resolved desktop environment. The source link pins the reviewed instructions; an installed app may ship a different revision, so inspect its live schema before use. Source self-hosting instructions are in https://github.com/AFK-surf/Comma/blob/c138b5cc767f211d162af7a04ba8ee544bf6a54a/README.md; a self-hosted backend alone does not replace the required desktop app.

- Source: https://github.com/AFK-surf/Comma/tree/c138b5cc767f211d162af7a04ba8ee544bf6a54a/resources/salix-system-files/skills/browser-use

## Documentation

- https://github.com/AFK-surf/Comma/tree/c138b5cc767f211d162af7a04ba8ee544bf6a54a/resources/salix-system-files/skills/browser-use/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/complete-website-tasks-in-comma-native-desktop-browser/)
