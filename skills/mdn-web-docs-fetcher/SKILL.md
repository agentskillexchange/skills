---
name: "MDN Web Docs Fetcher"
description: "Queries the MDN Web Docs content API (Yari) and the MDN search index to retrieve browser compatibility data, Web API references, and CSS property documentation. Uses BCD (browser-compat-data) npm package for offline lookups."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/mdn-web-docs-fetcher/"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
---

# MDN Web Docs Fetcher

The MDN Web Docs Fetcher skill provides instant access to comprehensive web platform documentation through the MDN content API (Yari). It queries the MDN search index for fast lookups of Web API references, CSS properties, HTML elements, and JavaScript features.
The skill leverages the @mdn/browser-compat-data (BCD) npm package for offline browser compatibility lookups, enabling quick checks of feature support across Chrome, Firefox, Safari, and Edge. It parses MDN structured content to extract syntax examples, parameter descriptions, and return value documentation.
Advanced features include cross-referencing related APIs, generating compatibility tables, and extracting polyfill recommendations for features with limited browser support. The skill supports querying by specification URL, feature name, or free-text search, making it ideal for rapid web development reference during coding sessions.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mdn-web-docs-fetcher/)
