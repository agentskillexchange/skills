---
name: "DealMachine Sales Intelligence"
slug: "dealmachine-sales-intelligence"
description: "Searches and enriches US property, owner, people, and company data through the DealMachine CLI and hosted MCP server for prospecting, lead generation, comparable-sales research, and targeted sales and marketing exports."
verification: "listed"
source: "https://github.com/DealMachine/dealmachine-cli"
category: "Integrations & Connectors"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "dealmachine/dealmachine-cli"
  npm_package: "@dealmachine/cli"
---

# DealMachine Sales Intelligence

Use this skill when an agent needs structured US property, owner, people, or company data for sales prospecting, marketing audience research, real estate lead generation, contact enrichment, comparable sales, or a targeted export. It connects to DealMachine through the public `dm` CLI or the hosted MCP server at `https://mcp.dealmachine.com`.

The workflow starts by discovering valid filter and field IDs, then counts or estimates the matching audience before running a paid search or export. It limits contact enrichment to the people and fields the user actually requests. For broad or credit-consuming operations, it explains the scope and asks for confirmation first. Results should distinguish counts, previews, enriched records, and completed exports.

## Install the skill

Install the canonical upstream skill from the DealMachine repository:

```bash
npm exec --yes skills@latest -- add DealMachine/dealmachine-cli --skill dealmachine
```

For a manual installation, clone the upstream repository and copy `skills/dealmachine` into the skill directory used by Codex, Claude Code, Cursor, or another compatible agent.

## Connect the hosted MCP server

Add the following remote HTTP server to a compatible MCP client:

```json
{
  "mcpServers": {
    "dealmachine": {
      "type": "http",
      "url": "https://mcp.dealmachine.com"
    }
  }
}
```

The hosted server supports OAuth 2.1. Developer clients that support bearer-token configuration can use a DealMachine API key. Never paste credentials into a prompt or commit them to a repository.

## Install the CLI

```bash
npm install -g dealmachine
dm login
```

The CLI provides JSON output for automation and covers property and people search, enrichment, comparable sales, filters, fields, lists, exports, usage, account activity, direct mail, CRM, tasks, and developer utilities. Run `dm --help` or a command-specific help screen before constructing an unfamiliar request.

## Safe operating pattern

1. Identify the entity, location, filters, output fields, audience, limit, and desired result type.
2. Discover supported filters and fields instead of inventing IDs.
3. Run a count or cost estimate before a broad paid operation.
4. Start with a small preview unless the user asks for a complete result.
5. Confirm the expected scope and credit impact before a material export.
6. Report the filters applied, records returned, and credits used when available.

See the [upstream repository](https://github.com/DealMachine/dealmachine-cli) for current commands, MCP Tool coverage, and authentication details.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/DealMachine/dealmachine-cli
