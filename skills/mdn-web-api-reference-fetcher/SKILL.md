---
title: "MDN Web API Reference Fetcher"
description: "Fetches and indexes Mozilla Developer Network Web API documentation using the MDN Yari content API. Provides structured API signatures, browser compatibility data from BCD, and code examples."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/mdn-web-api-reference-fetcher/"
category:
  - "Library &amp; API Reference"
framework:
  - "Custom Agents"
---

# MDN Web API Reference Fetcher

The MDN Web API Reference Fetcher skill provides on-demand access to Mozilla Developer Network documentation for Web APIs through the MDN Yari content API. It fetches structured documentation pages, extracts API signatures, parameter descriptions, and return types, and presents them in a concise reference format.

The skill queries the MDN search index at /api/v1/search for API discovery and fetches full document content from /api/v1/doc endpoints. It parses the structured content to extract method signatures, property types, event definitions, and inheritance hierarchies. Browser compatibility data is pulled from the browser-compat-data (BCD) package, showing support tables for Chrome, Firefox, Safari, and Edge with version ranges.

Advanced features include local caching with TTL-based invalidation, specification link resolution to W3C and WHATWG specs, and interactive example extraction from MDN live samples. The skill supports batch queries for entire Web API interfaces, generates TypeScript declaration files from MDN type information, and provides polyfill recommendations for APIs with limited browser support. It also tracks the MDN content changelog to notify when documentation for monitored APIs is updated.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mdn-web-api-reference-fetcher/)
