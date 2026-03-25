---
name: "MDN Web API Reference Fetcher"
description: "Fetches and indexes Mozilla Developer Network Web API documentation using the MDN Yari content API. Provides structured API signatures, browser compatibility data from BCD, and code examples."
category: "Library & API Reference"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/mdn-web-api-reference-fetcher/"
---

# MDN Web API Reference Fetcher

Fetches and indexes Mozilla Developer Network Web API documentation using the MDN Yari content API. Provides structured API signatures, browser compatibility data from BCD, and code examples.

## Overview

The MDN Web API Reference Fetcher skill provides on-demand access to Mozilla Developer Network documentation for Web APIs through the MDN Yari content API. It fetches structured documentation pages, extracts API signatures, parameter descriptions, and return types, and presents them in a concise reference format.

The skill queries the MDN search index at /api/v1/search for API discovery and fetches full document content from /api/v1/doc endpoints. It parses the structured content to extract method signatures, property types, event definitions, and inheritance hierarchies. Browser compatibility data is pulled from the browser-compat-data (BCD) package, showing support tables for Chrome, Firefox, Safari, and Edge with version ranges.

Advanced features include local caching with TTL-based invalidation, specification link resolution to W3C and WHATWG specs, and interactive example extraction from MDN live samples. The skill supports batch queries for entire Web API interfaces, generates TypeScript declaration files from MDN type information, and provides polyfill recommendations for APIs with limited browser support. It also tracks the MDN content changelog to notify when documentation for monitored APIs is updated.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill mdn-web-api-reference-fetcher
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill mdn-web-api-reference-fetcher -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill mdn-web-api-reference-fetcher -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mdn-web-api-reference-fetcher -a codex
```

### OpenClaw

```bash
clawhub install mdn-web-api-reference-fetcher
```

## Source

- Marketplace: https://agentskillexchange.com/skills/mdn-web-api-reference-fetcher/
