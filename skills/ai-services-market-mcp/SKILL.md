---
name: "AI Services Market MCP"
slug: "ai-services-market-mcp"
description: "Teaches an agent to connect to the AI Services Market MCP server (https://aiservicesmarket.lol/mcp) and use its seven tools — search_skills, get_skill, search_use_cases, get_use_case, get_entitlement, create_checkout, claim_pro — to find installable agent skills, read full details and pricing, and generate Stripe checkout links for single skills or Pro subscriptions. Use when someone asks an agent to find, compare, or buy an AI agent skill."
category: "Integrations & Connectors"
framework: "MCP"
verification: listed
source: "https://aiservicesmarket.lol/mcp"
---

# AI Services Market MCP

Use this skill when a user asks an agent to find an AI agent skill — a SKILL.md playbook that teaches an AI tool (Claude, ChatGPT, Cursor, a coding agent, etc.) how to do a specific job — or to compare options, check prices, or buy one. This skill connects the agent to AI Services Market, a store of installable agent skills, through its documented MCP API.

## What it connects to

AI Services Market (https://aiservicesmarket.lol) sells installable agent skills: original paid skills plus free community skills (the server computes catalog counts live — query it, or the store's llms.txt, for current totals; do not quote fixed numbers). It exposes a documented MCP server over Streamable HTTP at:

```
https://aiservicesmarket.lol/mcp
```

Authentication is OAuth 2.1: the client reads `/.well-known/oauth-protected-resource`, registers dynamically (DCR), and opens an authorize page on first call. Approving links the assistant's identity, which the server uses only to record purchase and Pro entitlements. Access tokens last 1 hour; refresh tokens last 30 days. Any MCP-compatible client can connect — Claude Code, Claude Desktop, Cursor, VS Code, ChatGPT, Gemini, Windsurf — by adding the same URL.

## The tools

The server exposes seven tools for catalog discovery, use cases, entitlements, and checkout:

- `search_skills` — keyword search across the skill catalog, with optional `category` / `source` filters. Returns name, description, category, source, price, and page link per skill.
- `get_skill` — full detail for one skill: description, audience, page link, install guide. The `agent` parameter (`claude` default, `codex`, `gemini`, `antigravity`, `other`) localizes the install instructions to the caller's platform. Paid originals return a paywalled install block until the skill is bought or Pro is active; community skills are free and unlocked.
- `search_use_cases` — keyword search across 1,300+ real, documented AI use cases: things people actually had AI do, organized by category.
- `get_use_case` — one use case in full: what they did, how it went, what is worth knowing, a reusable prompt, and a link to the original post.
- `get_entitlement` — whether the connected identity holds Pro (status, expiry). Pro covers all original skills.
- `create_checkout` — returns a Stripe `checkout_url`. Products: `single` ($4.99 one-off, requires `skill_slug`), `pro_monthly` ($9.99/month), `pro_yearly` ($79/year), `pro_lifetime` ($169 one-time). No refunds; cancelled subscriptions stay active until the end of the billing period.
- `claim_pro` — link a guest Pro purchase to the connected identity. Takes `claim_code` (e.g. `PRO-AB12-CD34`, shown on the website's payment success page after a guest Stripe checkout, no account needed). Single-use: an already-claimed code is rejected.

Pricing matches the store's public /pricing/ page.

## Recommended agent workflow

1. Clarify the user's task, then call `search_skills` with two or three keyword phrasings. Present the top three results with price and a one-line verdict each.
2. Call `get_skill` on the chosen skill and summarize what it does and what it costs. Read install instructions aloud only if the response shows the skill is unlocked (purchased or Pro), or if it is a free community skill.
3. For a purchase: call `create_checkout` with the right product and hand the user the returned `checkout_url` to complete in their browser — the entitlement then attaches to the connected MCP identity. If the user already bought Pro as a guest on the website (Stripe checkout, no account), ask for the claim code from their payment success page (looks like `PRO-AB12-CD34`) and call `claim_pro` with it to link Pro to this identity; an already-claimed code is rejected. Verify access afterwards with `get_entitlement`. Never direct an existing subscriber to buy again. Single skills can also be bought as a guest on the skill's web page.

## Installation

### Claude Code

```bash
claude mcp add --transport http skillshop https://aiservicesmarket.lol/mcp
```

### Any MCP client (Claude Desktop, Cursor, VS Code, ChatGPT, Gemini, Windsurf)

Add a custom MCP server with type HTTP/Streamable and URL `https://aiservicesmarket.lol/mcp`. The first call triggers the OAuth authorize page; approve once and the connection is linked.

### Optional Third-Party Installer

Once this skill is merged into the Agent Skill Exchange catalog:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill "AI Services Market MCP"
```
