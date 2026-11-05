---
name: "AltoRank"
slug: "altorank"
description: "Use the AltoRank MCP server to audit whether search engines and AI assistants can read a site, propose JSON-LD, read Google Search Console, research keywords, and write SEO drafts into a person's review queue. Never approves or publishes."
verification: "listed"
source: "https://github.com/AltoRank/altorank/tree/main/plugins/altorank/skills/altorank"
author: "AltoRank"
publisher_type: "vendor"
category: "Content Writing & SEO"
framework: "Claude Code"
---

# AltoRank

Use AltoRank when a coding agent should check a site's search and AI-search readiness, read its Search Console data, research keywords, or write SEO drafts for a person to review. AltoRank is open-source SEO content software (AGPL-3.0). Its hosted MCP server is at https://app.altorank.co/api/mcp (Streamable HTTP, OAuth) and is listed in the official MCP registry as `co.altorank/altorank`.

The skill teaches the agent the tool contract: run a preflight (`altorank_whoami`, `altorank_get_workspace`, `altorank_readiness_report`), read `agent_guidance` and `allowed_mutations` on every result, ask before spending research credits or quota, write one draft per keyword with an idempotency key and poll until it reaches review, and keep Search Console states apart (not connected, nothing synced, measured zero). Readiness tools (`altorank_check_readiness`, `altorank_propose_schema`, `altorank_generate_machine_readable`) work on any public domain. There is no approve, hold, publish or delete tool; a person decides what publishes.

## Prerequisites

An AltoRank account and an MCP client that supports remote Streamable HTTP servers with OAuth, such as Claude Code, Cursor or Codex. Self-hosting is free (Docker Compose, Next.js + Supabase); hosted plans are paid and include a 7-day trial. Pricing is on https://altorank.co.

## Installation

Install or set up from the source-backed instructions:

- Claude Code plugin (bundles this skill and the MCP server): run `claude plugin marketplace add AltoRank/altorank`, then `claude plugin install altorank@altorank`.
- Claude Code, server only: run `claude mcp add --transport http altorank https://app.altorank.co/api/mcp`, then `/mcp`, select altorank and authenticate in the browser.
- Skill files: copy `plugins/altorank/skills/altorank` from https://github.com/AltoRank/altorank into your agent's skills directory.

## Documentation

- https://altorank.co/docs/mcp/
- https://github.com/AltoRank/altorank#readme

## Source

- https://altorank.co
- https://github.com/AltoRank/altorank
