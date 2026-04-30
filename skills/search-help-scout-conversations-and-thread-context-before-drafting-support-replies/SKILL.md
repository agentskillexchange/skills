---
title: "Search Help Scout conversations and thread context before drafting support replies"
description: "Lets an MCP-compatible agent search Help Scout inboxes, customers, organizations, and full thread history so support replies start with the right account and ticket context."
verification: "security_reviewed"
source: "https://github.com/drewburchfield/help-scout-mcp-server"
author: "drewburchfield"
publisher_type: "individual"
category:
  - "Calendar, Email & Productivity"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "drewburchfield/help-scout-mcp-server"
  github_stars: 36
  npm_package: "help-scout-mcp-server"
  npm_weekly_downloads: 184
---

# Search Help Scout conversations and thread context before drafting support replies

Lets an MCP-compatible agent search Help Scout inboxes, customers, organizations, and full thread history so support replies start with the right account and ticket context.

## Prerequisites

MCP-compatible client and Help Scout private app credentials with read access to Mailboxes, Conversations, Customers, and Organizations. Optional Docker or Claude Desktop/Claude Code plugin install.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
<p>Add the server to your MCP client with <code>npx help-scout-mcp-server</code>, set <code>HELPSCOUT_APP_ID</code> and <code>HELPSCOUT_APP_SECRET</code>, and grant the Help Scout private app read access to Mailboxes, Conversations, Customers, and Organizations. If you want the packaged navigator guidance, install the project’s Claude/Desktop plugin from the repository releases or marketplace instructions.</p>
```

## Documentation

- https://github.com/drewburchfield/help-scout-mcp-server

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-help-scout-conversations-and-thread-context-before-drafting-support-replies/)
