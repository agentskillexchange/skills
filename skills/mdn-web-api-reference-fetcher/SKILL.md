---
title: "MDN Web API Reference Fetcher"
description: "The MDN Web API Reference Fetcher skill provides on-demand access to Mozilla Developer Network documentation for Web APIs through the MDN Yari content API. It fetches structured documentation pages, extracts API signatures, parameter descriptions, and return types, and presents them in a concise reference format. The skill queries the MDN search index at /api/v1/search for API discovery and fetches full document content from /api/v1/doc endpoints. It parses the structured content to extract method signatures, property types, event definitions, and inheritance hierarchies. Browser compatibility data is pulled from the browser-compat-data (BCD) package, showing support tables for Chrome, Firefox, Safari, and Edge with version ranges. Advanced features include local caching with TTL-based invalidation, specification link resolution to W3C and WHATWG specs, and interactive example extraction from MDN live samples. The skill supports batch queries for entire Web API interfaces, generates TypeScript declaration files from MDN type information, and provides polyfill recommendations for APIs with limited browser support. It also tracks the MDN content changelog to notify when documentation for monitored APIs is updated."
source: "https://agentskillexchange.com/skills/mdn-web-api-reference-fetcher/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Custom Agents"
---

# MDN Web API Reference Fetcher

The MDN Web API Reference Fetcher skill provides on-demand access to Mozilla Developer Network documentation for Web APIs through the MDN Yari content API. It fetches structured documentation pages, extracts API signatures, parameter descriptions, and return types, and presents them in a concise reference format. The skill queries the MDN search index at /api/v1/search for API discovery and fetches full document content from /api/v1/doc endpoints. It parses the structured content to extract method signatures, property types, event definitions, and inheritance hierarchies. Browser compatibility data is pulled from the browser-compat-data (BCD) package, showing support tables for Chrome, Firefox, Safari, and Edge with version ranges. Advanced features include local caching with TTL-based invalidation, specification link resolution to W3C and WHATWG specs, and interactive example extraction from MDN live samples. The skill supports batch queries for entire Web API interfaces, generates TypeScript declaration files from MDN type information, and provides polyfill recommendations for APIs with limited browser support. It also tracks the MDN content changelog to notify when documentation for monitored APIs is updated.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mdn-web-api-reference-fetcher/)
