---
name: "Firecrawl Alexandria"
slug: "firecrawl-alexandria"
description: "Firecrawl Alexandria gives coding agents a direct path to structured data through ready-made website workflows, data APIs, and specialized indexes. The agent discovers a tool with Firecrawl search, inspects its contract, and runs it through Firecrawl scrape to get typed records instead of parsing pages."
verification: "listed"
source: "https://github.com/firecrawl/skills/tree/main/skills/core/firecrawl-alexandria"
author: "Firecrawl"
publisher_type: "commercial_saas"
category: "Research & Scraping"
framework: "Multi-Framework"
---

# Firecrawl Alexandria

The Firecrawl Alexandria skill teaches a coding agent to find and call the tools in [Firecrawl Alexandria](https://alexandria.firecrawl.dev/?utm_source=agentskillexchange-skills&utm_medium=integration), a catalog of ready-made website workflows, data APIs, and specialized indexes that runs inside Firecrawl search and scrape. When a task needs structured records, filterable listings, filings, or datasets, the agent checks for a tool that returns that data directly, which can reduce the browsing, parsing, and repeated requests it would otherwise need to assemble the data itself.

## How it works

- **Discover.** `firecrawl search '<user question>'` returns web results and, with an API key, matching Firecrawl Alexandria tools in one response. Semantic discovery matches the meaning of the question to tool capabilities, and domain matching connects websites in the web results to tools that may return richer structured data than the linked page. `firecrawl search alexandria '<data you need>'` returns tool matches only, and `firecrawl find-tools <url>` lists the tools for a known website.
- **Inspect.** `firecrawl list <provider> <capability> --pretty` shows a tool's contract: its inputs, coverage, and access requirements. Discovery and inspection don't run the tool.
- **Run.** `firecrawl scrape <provider/capability> --options '<input JSON>'` executes the selected tool and returns structured results. For large results, the scrape skill's remote Bash guidance selects only the data the task needs.
- **Report coverage.** `firecrawl alexandria feedback` records whether a tool answered the need, and which websites or capabilities were missing. It sends the website, the need, and a rating to Firecrawl; set `FIRECRAWL_NO_ENDPOINT_FEEDBACK=1` to turn it off.

The agent uses ordinary web results when they answer the question and a provider tool when its coverage and inputs fit. For example, a search for a public company's SEC filings surfaces the `sec-gov` tools for EDGAR filer profiles and filing lists.

The skill hands off to the `firecrawl-search` and `firecrawl-scrape` skills, which the full catalog install below includes.

## Prerequisites

- Node.js and npm
- A Firecrawl account (sign in with `firecrawl login`) or a `FIRECRAWL_API_KEY` from a team with Firecrawl Alexandria enabled. Keyless access doesn't include Firecrawl Alexandria.
- Running a tool uses Firecrawl credits at its listed price, and some providers ask an organization admin to accept their terms first.

## Installation

### Agent Skills CLI (Claude Code, Cursor, Codex, and other agents)

Install this skill:

```bash
npx skills add firecrawl/skills --skill firecrawl-alexandria
```

Or install the full Firecrawl catalog, including the search and scrape skills:

```bash
npx skills add firecrawl/skills
```

### Firecrawl CLI

Install the CLI, sign in through the browser, and add the core skills (including `firecrawl-alexandria`) to every detected agent:

```bash
npx -y firecrawl-cli@latest init --all --browser
```

To install the CLI on its own:

```bash
npm install -g firecrawl-cli
firecrawl login
```

### MCP clients

Add the hosted Firecrawl MCP server at `https://mcp.firecrawl.dev/v2/mcp-oauth` and sign in. `firecrawl_search` with `sources: ["alexandria"]` finds tools, `firecrawl_find_tools` inspects their inputs, and `firecrawl_scrape` with an `alexandria` argument runs one.

## Documentation

- [Firecrawl Alexandria](https://alexandria.firecrawl.dev/?utm_source=agentskillexchange-skills&utm_medium=integration)
- [firecrawl-alexandria SKILL.md](https://github.com/firecrawl/skills/blob/main/skills/core/firecrawl-alexandria/SKILL.md)
- [Firecrawl skills catalog](https://github.com/firecrawl/skills)
