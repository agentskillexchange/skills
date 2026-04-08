---
title: Markdown-to-AMP Article Converter
description: The Markdown-to-AMP Article Converter transforms standard Markdown content
  into fully compliant Accelerated Mobile Pages using the unified.js ecosystem. It
  processes Markdown through remark-parse, applies remark-gfm for GitHub Flavored
  Markdown support, then converts to HTML via remark-rehype. AMP-specific transformations
  include replacing img tags with amp-img components (with automatic width/height
  detection via probe-image-size), converting embedded videos to amp-video or amp-youtube,
  and injecting the required AMP boilerplate. The rehype-sanitize plugin strips non-compliant
  HTML while preserving semantic structure. Schema.org structured data is generated
  using the schema-dts TypeScript library, producing Article, NewsArticle, or BlogPosting
  markup based on frontmatter metadata. Every output is validated against Google’s
  amphtml-validator library before writing. The skill supports custom AMP components
  injection, Open Graph meta tags, canonical URL management, and sitemap.xml generation
  for batches of converted articles. CSS is inlined and minified to meet AMP’s 75KB
  limit using cssnano.
verification: security_reviewed
source: https://agentskillexchange.com/skills/markdown-to-amp-article-converter/
category:
- Content Writing &amp; SEO
framework:
- Codex
---

# Markdown-to-AMP Article Converter

The Markdown-to-AMP Article Converter transforms standard Markdown content into fully compliant Accelerated Mobile Pages using the unified.js ecosystem. It processes Markdown through remark-parse, applies remark-gfm for GitHub Flavored Markdown support, then converts to HTML via remark-rehype. AMP-specific transformations include replacing img tags with amp-img components (with automatic width/height detection via probe-image-size), converting embedded videos to amp-video or amp-youtube, and injecting the required AMP boilerplate. The rehype-sanitize plugin strips non-compliant HTML while preserving semantic structure. Schema.org structured data is generated using the schema-dts TypeScript library, producing Article, NewsArticle, or BlogPosting markup based on frontmatter metadata. Every output is validated against Google’s amphtml-validator library before writing. The skill supports custom AMP components injection, Open Graph meta tags, canonical URL management, and sitemap.xml generation for batches of converted articles. CSS is inlined and minified to meet AMP’s 75KB limit using cssnano.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/markdown-to-amp-article-converter/)
