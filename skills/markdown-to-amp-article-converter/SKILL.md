---
name: "Markdown-to-AMP Article Converter"
description: "Converts Markdown files to valid AMP HTML articles using unified/remark/rehype pipeline. Validates output against amphtml-validator and generates structured data with schema-dts."
category: "Content Writing & SEO"
framework: "Codex"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/markdown-to-amp-article-converter/"
---

# Markdown-to-AMP Article Converter

Converts Markdown files to valid AMP HTML articles using unified/remark/rehype pipeline. Validates output against amphtml-validator and generates structured data with schema-dts.

## Overview

The Markdown-to-AMP Article Converter transforms standard Markdown content into fully compliant Accelerated Mobile Pages using the unified.js ecosystem. It processes Markdown through remark-parse, applies remark-gfm for GitHub Flavored Markdown support, then converts to HTML via remark-rehype. AMP-specific transformations include replacing img tags with amp-img components (with automatic width/height detection via probe-image-size), converting embedded videos to amp-video or amp-youtube, and injecting the required AMP boilerplate. The rehype-sanitize plugin strips non-compliant HTML while preserving semantic structure. Schema.org structured data is generated using the schema-dts TypeScript library, producing Article, NewsArticle, or BlogPosting markup based on frontmatter metadata. Every output is validated against Google’s amphtml-validator library before writing. The skill supports custom AMP components injection, Open Graph meta tags, canonical URL management, and sitemap.xml generation for batches of converted articles. CSS is inlined and minified to meet AMP’s 75KB limit using cssnano.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill markdown-to-amp-article-converter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill markdown-to-amp-article-converter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill markdown-to-amp-article-converter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill markdown-to-amp-article-converter -a codex
```

### OpenClaw

```bash
clawhub install markdown-to-amp-article-converter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/markdown-to-amp-article-converter/
