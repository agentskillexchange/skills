---
name: "eBay Listing Research with SoldFetch"
slug: "soldfetch-ebay-data"
description: "Research sold and active eBay listings through SoldFetch MCP for resale comparisons, pricing observations, and public item lookup. Not affiliated with eBay."
category: "Research & Scraping"
framework: "Codex"
verification: listed
source: "https://github.com/ricciflow-api/soldfetch-agent-skills/tree/main/skills/ebay-data"
---

# eBay Listing Research with SoldFetch

Use this workflow when a user asks for resale comparables, an active price check, or context about a public eBay item. Confirm the eBay site, search phrase or item ID, condition, and how many results the user needs. Start with one page of up to 20 results and use the MCP structured response to inspect listing fields. Search sold listings first for comparables, and keep active asking prices in their own group. Use an individual item lookup only when it resolves a material difference such as condition, bundle contents, or model. Exclude obvious mismatches, deduplicate by marketplace and item ID, and preserve currency and source links. A missing result does not establish that an item sold. SoldFetch is independent of eBay.

## Workflow

- Call `search_ebay_sold` with `sold=true` for comparable listings. Use `sold=false` for active asking prices. Use `get_ebay_item` when the user provides a specific item ID or when comparable listings need more context.
- Use `search_ebay_category` for category browsing. If it reports `upstream_blocked`, explain the source failure and keep the original category constraint.
- Report displayed listing prices as observations. Accepted Best Offer amounts can be hidden, and dates supplied by the source are unverified. If there are too few comparable items, state how many qualify.
- Stop within the agreed request budget. One successful page or item call uses one unit. Failed requests use zero units. Keep API keys in the client’s credential configuration.

## Installation

Connect the hosted MCP server in Codex. Store your own key in the `SOLDFETCH_API_KEY` environment variable before connecting.

```bash
codex mcp add soldfetch --url https://soldfetch.com/api/mcp --bearer-token-env-var SOLDFETCH_API_KEY
```

Install the upstream skill bundle if you need its operation reference or Python REST fallback.

```bash
npx skills add ricciflow-api/soldfetch-agent-skills
```

[SoldFetch documentation](https://docs.soldfetch.com) and [official skill source](https://github.com/ricciflow-api/soldfetch-agent-skills/tree/main/skills/ebay-data). Adapted from the upstream MIT-licensed SoldFetch skill.
