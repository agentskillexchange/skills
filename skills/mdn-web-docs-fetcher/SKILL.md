---
name: "MDN Web Docs Fetcher"
description: "Queries the MDN Web Docs content API (Yari) and the MDN search index to retrieve browser compatibility data, Web API references, and CSS property documentation. Uses BCD (browser-compat-data) npm package for offline lookups."
category: "Library & API Reference"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/mdn-web-docs-fetcher/"
---
# MDN Web Docs Fetcher

Queries the MDN Web Docs content API (Yari) and the MDN search index to retrieve browser compatibility data, Web API references, and CSS property documentation. Uses BCD (browser-compat-data) npm package for offline lookups.

The MDN Web Docs Fetcher skill provides instant access to comprehensive web platform documentation through the MDN content API (Yari). It queries the MDN search index for fast lookups of Web API references, CSS properties, HTML elements, and JavaScript features.



The skill leverages the @mdn/browser-compat-data (BCD) npm package for offline browser compatibility lookups, enabling quick checks of feature support across Chrome, Firefox, Safari, and Edge. It parses MDN structured content to extract syntax examples, parameter descriptions, and return value documentation.



Advanced features include cross-referencing related APIs, generating compatibility tables, and extracting polyfill recommendations for features with limited browser support. The skill supports querying by specification URL, feature name, or free-text search, making it ideal for rapid web development reference during coding sessions.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill mdn-web-docs-fetcher
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill mdn-web-docs-fetcher -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill mdn-web-docs-fetcher -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mdn-web-docs-fetcher -a codex
```

### OpenClaw

```bash
clawhub install mdn-web-docs-fetcher
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mdn-web-docs-fetcher/)
