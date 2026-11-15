---
name: "Work an SEO and AI-Visibility Backlog with LogNorm"
slug: "lognorm-seo-geo-backlog"
description: "Use LogNorm when Claude Code, Codex or Cursor should work a site's SEO and AI-visibility (GEO) backlog through a hosted MCP server: audits, fixes, content drafts and AI-answer tracking."
verification: "listed"
source: "https://github.com/lognorm/lognorm-mcp/tree/main/skills/lognorm"
author: "lognorm"
publisher_type: "vendor"
category: "Content Writing & SEO"
framework: "Claude Code"
---

# Work an SEO and AI-Visibility Backlog with LogNorm

Use LogNorm when a coding agent should work a website's SEO and AI-visibility (GEO) backlog instead of only reading about it. LogNorm is a hosted MCP server (https://lognorm.com/api/mcp, Streamable HTTP, OAuth 2.1, no API keys). It crawls and audits the site, runs a GEO audit, pulls keyword and competitor research, tracks how ChatGPT, Gemini and Google AI Overviews answer buyer questions, and ranks the findings into prioritized "moves". The skill teaches the agent to join the workspace as a named teammate: read the plan, claim a move, fix the issue in the codebase, validate the fix, write and save content drafts, and leave a comment trail on the LogNorm dashboard.

The skill is a single SKILL.md plus reference files in the lognorm-mcp repository. It also ships MCP prompts for common workflows (weekly growth plan, fix audit, write post, plan topic, AI-visibility check).

## Prerequisites

A LogNorm account (a free plan with one website is available) and an MCP client that supports remote Streamable HTTP servers with OAuth, such as Claude Code, Codex or Cursor. The hosted service is separate from this repository and its pricing is on https://lognorm.com.

## Installation

Install or set up from the source-backed instructions:

- Claude Code: run `claude mcp add --transport http lognorm https://lognorm.com/api/mcp`, then `/mcp`, select lognorm and authenticate in the browser.
- Codex: run `codex mcp add lognorm --url https://lognorm.com/api/mcp`, then `codex mcp login lognorm`.
- Skill files: copy `skills/lognorm` from https://github.com/lognorm/lognorm-mcp into your agent's skills directory, or install the repository as a Claude Code plugin.

## Documentation

- https://lognorm.com/docs/agents
- https://github.com/lognorm/lognorm-mcp#readme

## Source

- https://lognorm.com
- https://github.com/lognorm/lognorm-mcp
