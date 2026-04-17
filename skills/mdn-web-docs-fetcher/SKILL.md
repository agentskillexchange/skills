---
title: "MDN Web Docs Fetcher"
description: "The MDN Web Docs Fetcher skill provides instant access to comprehensive web platform documentation through the MDN content API (Yari). It queries the MDN search index for fast lookups of Web API references, CSS properties, HTML elements, and JavaScript features.\nThe skill leverages the @mdn/browser-compat-data (BCD) npm package for offline browser compatibility lookups, enabling quick checks of feature support across Chrome, Firefox, Safari, and Edge. It parses MDN structured content to extract syntax examples, parameter descriptions, and return value documentation.\nAdvanced features include cross-referencing related APIs, generating compatibility tables, and extracting polyfill recommendations for features with limited browser support. The skill supports querying by specification URL, feature name, or free-text search, making it ideal for rapid web development reference during coding sessions."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/mdn-web-docs-fetcher/"
framework:
  - "Cursor"
---

# MDN Web Docs Fetcher

The MDN Web Docs Fetcher skill provides instant access to comprehensive web platform documentation through the MDN content API (Yari). It queries the MDN search index for fast lookups of Web API references, CSS properties, HTML elements, and JavaScript features.
The skill leverages the @mdn/browser-compat-data (BCD) npm package for offline browser compatibility lookups, enabling quick checks of feature support across Chrome, Firefox, Safari, and Edge. It parses MDN structured content to extract syntax examples, parameter descriptions, and return value documentation.
Advanced features include cross-referencing related APIs, generating compatibility tables, and extracting polyfill recommendations for features with limited browser support. The skill supports querying by specification URL, feature name, or free-text search, making it ideal for rapid web development reference during coding sessions.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/mdn-web-docs-fetcher
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/mdn-web-docs-fetcher` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mdn-web-docs-fetcher/)
