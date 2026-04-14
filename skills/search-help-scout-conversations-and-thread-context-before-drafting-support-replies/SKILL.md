---
title: "Search Help Scout conversations and thread context before drafting support replies"
description: "Lets an MCP-compatible agent search Help Scout inboxes, customers, organizations, and full thread history so support replies start with the right account and ticket context."
verification: security_reviewed
source: "https://github.com/drewburchfield/help-scout-mcp-server"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "drewburchfield/help-scout-mcp-server"
  github_stars: 36
  npm_package: "help-scout-mcp-server"
  npm_weekly_downloads: 184
---

# Search Help Scout conversations and thread context before drafting support replies

Use Help Scout MCP Server when an agent is assisting support work and needs prior conversations, ticket history, customer records, organization context, or full thread contents before summarizing a case or drafting a reply. It is especially useful when the value comes from gathering the right Help Scout context first, rather than having the agent guess from a single message.

This is skill-shaped because the scope stays inside a repeatable support-context retrieval workflow. It does not replace Help Scout itself, a general helpdesk platform, or outbound support automation. Invoke it when the agent needs to search and assemble Help Scout context before answering, escalating, or summarizing.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-help-scout-conversations-and-thread-context-before-drafting-support-replies/)
