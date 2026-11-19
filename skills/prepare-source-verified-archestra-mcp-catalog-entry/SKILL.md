---
name: "Prepare a source-verified Archestra MCP catalog entry"
slug: "prepare-source-verified-archestra-mcp-catalog-entry"
description: "Prepare a catalog manifest from an MCP server URL, verify remote transport and tool metadata, and check the entry before maintainer review."
verification: "security_reviewed"
source: "https://github.com/archestra-ai/archestra/tree/main/.agents/skills/archestra-mcp-catalog-entry"
author: "Archestra AI"
publisher_type: "company"
category: "Developer Tools"
framework: "Multi-Framework"
---

# Prepare a source-verified Archestra MCP catalog entry

Prepare a catalog manifest from an MCP server URL, verify remote transport and tool metadata, and check the entry before maintainer review.

## Prerequisites

Git; a file-capable coding agent such as Claude Code or Codex; curl; Python 3; Node.js/npx for Prettier. Optional matching Archestra website checkout, pnpm and its catalog validator.

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/archestra-ai/archestra.git, enter the checkout, and read AGENTS.md, .agents/README.md and .agents/skills/archestra-mcp-catalog-entry/SKILL.md. The repository shares these skills with Codex directly and Claude Code through its .claude/skills symlink. Explicitly ask the agent to use archestra-mcp-catalog-entry to prepare an entry for the supplied URL and stop at the review handoff. No platform deployment or Docker installation is needed for catalog-file preparation. Keep the complete skill and its repository-relative catalog context available.

- Source: https://github.com/archestra-ai/archestra/tree/main/.agents/skills/archestra-mcp-catalog-entry

## Documentation

- https://github.com/archestra-ai/archestra/tree/main/.agents/skills/archestra-mcp-catalog-entry

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/prepare-source-verified-archestra-mcp-catalog-entry/)
