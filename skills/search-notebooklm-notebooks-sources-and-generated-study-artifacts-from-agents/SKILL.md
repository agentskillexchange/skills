---
title: "Search NotebookLM notebooks, sources, and generated study artifacts from agents"
description: "Use notebooklm-mcp-cli when an agent needs to search NotebookLM notebooks, add sources, run notebook queries, and retrieve generated study artifacts without leaving an MCP workflow."
verification: "security_reviewed"
source: "https://github.com/jacob-bd/notebooklm-mcp-cli"
category:
  - "Research & Scraping"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "jacob-bd/notebooklm-mcp-cli"
  github_stars: 3558
---

# Search NotebookLM notebooks, sources, and generated study artifacts from agents

notebooklm-mcp-cli gives an agent programmatic access to Google NotebookLM through an MCP server and companion CLI. It can list or create notebooks, add URLs, files, Drive items, or text as sources, run notebook queries that persist into NotebookLM, kick off research or studio artifacts such as audio and slides, and pull results back into a broader research workflow.

The scope boundary is clear enough to be skill-shaped: this is for agent-side NotebookLM research operations, not a generic Google product card, not a broad browser automation workaround, and not a general note-taking platform listing. Invoke it when an agent needs NotebookLM’s source-grounded notebook workflows inside a repeatable research process, not when a human can just use the NotebookLM web UI directly.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/search-notebooklm-notebooks-sources-and-generated-study-artifacts-from-agents/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/search-notebooklm-notebooks-sources-and-generated-study-artifacts-from-agents
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/search-notebooklm-notebooks-sources-and-generated-study-artifacts-from-agents`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-notebooklm-notebooks-sources-and-generated-study-artifacts-from-agents/)
