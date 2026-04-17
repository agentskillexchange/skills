---
title: "Markdown-to-AMP Article Converter"
description: "Converts Markdown files to valid AMP HTML articles using unified/remark/rehype pipeline. Validates output against amphtml-validator and generates structured data with schema-dts."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/markdown-to-amp-article-converter/"
category:
  - "Content Writing & SEO"
framework:
  - "Codex"
---

# Markdown-to-AMP Article Converter

The Markdown-to-AMP Article Converter transforms standard Markdown content into fully compliant Accelerated Mobile Pages using the unified.js ecosystem. It processes Markdown through remark-parse, applies remark-gfm for GitHub Flavored Markdown support, then converts to HTML via remark-rehype. AMP-specific transformations include replacing img tags with amp-img components (with automatic width/height detection via probe-image-size), converting embedded videos to amp-video or amp-youtube, and injecting the required AMP boilerplate. The rehype-sanitize plugin strips non-compliant HTML while preserving semantic structure. Schema.org structured data is generated using the schema-dts TypeScript library, producing Article, NewsArticle, or BlogPosting markup based on frontmatter metadata. Every output is validated against Google’s amphtml-validator library before writing. The skill supports custom AMP components injection, Open Graph meta tags, canonical URL management, and sitemap.xml generation for batches of converted articles. CSS is inlined and minified to meet AMP’s 75KB limit using cssnano.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/markdown-to-amp-article-converter
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/markdown-to-amp-article-converter` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/markdown-to-amp-article-converter/)
