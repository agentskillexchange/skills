---
title: MDN Web API Reference Fetcher
description: The MDN Web API Reference Fetcher skill provides on-demand access to
  Mozilla Developer Network documentation for Web APIs through the MDN Yari content
  API. It fetches structured documentation pages, extracts API signatures, parameter
  descriptions, and return types, and presents them in a concise reference format.
  The skill queries the MDN search index at /api/v1/search for API discovery and fetches
  full document content from /api/v1/doc endpoints. It parses the structured content
  to extract method signatures, property types, event definitions, and inheritance
  hierarchies. Browser compatibility data is pulled from the browser-compat-data (BCD)
  package, showing support tables for Chrome, Firefox, Safari, and Edge with version
  ranges. Advanced features include local caching with TTL-based invalidation, specification
  link resolution to W3C and WHATWG specs, and interactive example extraction from
  MDN live samples. The skill supports batch queries for entire Web API interfaces,
  generates TypeScript declaration files from MDN type information, and provides polyfill
  recommendations for APIs with limited browser support. It also tracks the MDN content
  changelog to notify when documentation for monitored APIs is updated.
verification: security_reviewed
source: https://agentskillexchange.com/skills/mdn-web-api-reference-fetcher/
category:
- Library &amp; API Reference
framework:
- Custom Agents
---

# MDN Web API Reference Fetcher

The MDN Web API Reference Fetcher skill provides on-demand access to Mozilla Developer Network documentation for Web APIs through the MDN Yari content API. It fetches structured documentation pages, extracts API signatures, parameter descriptions, and return types, and presents them in a concise reference format. The skill queries the MDN search index at /api/v1/search for API discovery and fetches full document content from /api/v1/doc endpoints. It parses the structured content to extract method signatures, property types, event definitions, and inheritance hierarchies. Browser compatibility data is pulled from the browser-compat-data (BCD) package, showing support tables for Chrome, Firefox, Safari, and Edge with version ranges. Advanced features include local caching with TTL-based invalidation, specification link resolution to W3C and WHATWG specs, and interactive example extraction from MDN live samples. The skill supports batch queries for entire Web API interfaces, generates TypeScript declaration files from MDN type information, and provides polyfill recommendations for APIs with limited browser support. It also tracks the MDN content changelog to notify when documentation for monitored APIs is updated.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mdn-web-api-reference-fetcher/)
