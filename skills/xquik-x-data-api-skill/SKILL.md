---
name: "Xquik X Data API Skill"
slug: "xquik-x-data-api-skill"
description: "Use Xquik from coding agents to search X posts, inspect profiles, run bulk extractions, monitor accounts or keywords, verify HMAC webhooks, and call the remote MCP server or REST API with an XQUIK_API_KEY."
github_stars: 111
verification: "security_reviewed"
source: "https://github.com/Xquik-dev/x-twitter-scraper"
author: "Xquik-dev"
publisher_type: "tool_vendor"
category: "Research & Scraping"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Xquik-dev/x-twitter-scraper"
  github_stars: 111
  npm_package: "x-developer"
  npm_weekly_downloads: 136
---

# Xquik X Data API Skill

Xquik gives coding agents a source-backed way to work with X data through one package, one REST API, and one remote MCP server. Use this skill when a workflow needs post search, profile lookup, follower or following export, timeline reads, Spaces and article lookups, bulk extraction jobs, account or keyword monitors, webhook delivery, giveaway draw workflows, tweet composition, or confirmed write actions. The package exposes agent-oriented setup material for Codex, Claude Code, Cursor, OpenClaw, Gemini CLI, and other runtimes, while the API keeps authentication behind an `XQUIK_API_KEY`. Before creating persistent monitors, webhooks, or write actions, confirm the target account, destination URL, event type, and user intent.

## Installation

Install the source package when the agent runtime can load npm packages:

```bash
npm install x-developer@2.4.16
```

Set `XQUIK_API_KEY` in the agent runtime. Get the key from the Xquik dashboard account page, then follow the package README for MCP setup, REST endpoint selection, SDK links, and task-specific workflow files.

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
mkdir -p ~/.agent-skills
cp -R skills/skills/xquik-x-data-api-skill ~/.agent-skills/xquik-x-data-api-skill
```

## Source

- [Xquik x-twitter-scraper](https://github.com/Xquik-dev/x-twitter-scraper)
- [Xquik documentation](https://docs.xquik.com)
