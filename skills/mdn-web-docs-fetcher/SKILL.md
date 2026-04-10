---
title: "MDN Web Docs Fetcher"
description: "Queries the MDN Web Docs content API (Yari) and the MDN search index to retrieve browser compatibility data, Web API references, and CSS property documentation. Uses BCD (browser-compat-data) npm package for offline lookups."
slug: "mdn-web-docs-fetcher"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/mdn-web-docs-fetcher/"
listed: true
---

# MDN Web Docs Fetcher

Queries the MDN Web Docs content API (Yari) and the MDN search index to retrieve browser compatibility data, Web API references, and CSS property documentation. Uses BCD (browser-compat-data) npm package for offline lookups.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install mdn-web-docs-fetcher
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The MDN Web Docs Fetcher skill provides instant access to comprehensive web platform documentation through the MDN content API (Yari). It queries the MDN search index for fast lookups of Web API references, CSS properties, HTML elements, and JavaScript features.
The skill leverages the @mdn/browser-compat-data (BCD) npm package for offline browser compatibility lookups, enabling quick checks of feature support across Chrome, Firefox, Safari, and Edge. It parses MDN structured content to extract syntax examples, parameter descriptions, and return value documentation.
Advanced features include cross-referencing related APIs, generating compatibility tables, and extracting polyfill recommendations for features with limited browser support. The skill supports querying by specification URL, feature name, or free-text search, making it ideal for rapid web development reference during coding sessions.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mdn-web-docs-fetcher/)
