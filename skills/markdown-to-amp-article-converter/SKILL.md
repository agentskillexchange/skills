---
title: "Markdown-to-AMP Article Converter"
description: "Converts Markdown files to valid AMP HTML articles using unified/remark/rehype pipeline. Validates output against amphtml-validator and generates structured data with schema-dts."
verification: "security_reviewed"
source: "https://github.com/ampproject/amphtml"
category:
  - "Content Writing & SEO"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "ampproject/amphtml"
  github_stars: 14904
---

# Markdown-to-AMP Article Converter

The Markdown-to-AMP Article Converter transforms standard Markdown content into fully compliant Accelerated Mobile Pages using the unified.js ecosystem. It processes Markdown through remark-parse, applies remark-gfm for GitHub Flavored Markdown support, then converts to HTML via remark-rehype. AMP-specific transformations include replacing img tags with amp-img components (with automatic width/height detection via probe-image-size), converting embedded videos to amp-video or amp-youtube, and injecting the required AMP boilerplate. The rehype-sanitize plugin strips non-compliant HTML while preserving semantic structure. Schema.org structured data is generated using the schema-dts TypeScript library, producing Article, NewsArticle, or BlogPosting markup based on frontmatter metadata. Every output is validated against Google’s amphtml-validator library before writing. The skill supports custom AMP components injection, Open Graph meta tags, canonical URL management, and sitemap.xml generation for batches of converted articles. CSS is inlined and minified to meet AMP’s 75KB limit using cssnano.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/markdown-to-amp-article-converter/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/markdown-to-amp-article-converter
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/markdown-to-amp-article-converter`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/markdown-to-amp-article-converter/)
