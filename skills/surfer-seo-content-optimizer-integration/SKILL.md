---
title: Surfer SEO Content Optimizer Integration
description: 'This skill integrates with Surfer SEO’s content optimization API to
  analyze and improve content for search engine rankings. It creates content audits
  via POST to /v1/content_editors with target keyword and country parameters, receiving
  back NLP-based optimization recommendations. The skill compares existing content
  against Surfer’s guidelines for: word count range (min/max based on top-ranking
  competitors), heading count and structure (H2, H3 distribution), paragraph count,
  image count, and bold/strong tag usage. The core optimization loop analyzes semantic
  term coverage—Surfer provides a list of NLP-identified terms with target frequency
  ranges, and the skill identifies which terms are missing, underused, or overused
  in the content. It calculates a content score (0-100) matching Surfer’s scoring
  methodology based on weighted compliance across all ranking factors. The skill suggests
  specific insertions: where to add missing terms naturally, which headings to restructure,
  and where additional paragraphs or images would improve the score. For title tag
  optimization, it checks character length (50-60 chars), keyword position (front-loaded
  preferred), and power word inclusion. Meta description optimization targets 150-160
  characters with keyword inclusion and call-to-action phrasing. Output includes a
  before/after content score comparison, itemized recommendations with priority ranking,
  and an auto-optimized version of the content with changes highlighted.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/surfer-seo-content-optimizer-integration/
category:
- Content Writing &amp; SEO
framework:
- Cursor
---

# Surfer SEO Content Optimizer Integration

This skill integrates with Surfer SEO’s content optimization API to analyze and improve content for search engine rankings. It creates content audits via POST to /v1/content_editors with target keyword and country parameters, receiving back NLP-based optimization recommendations. The skill compares existing content against Surfer’s guidelines for: word count range (min/max based on top-ranking competitors), heading count and structure (H2, H3 distribution), paragraph count, image count, and bold/strong tag usage. The core optimization loop analyzes semantic term coverage—Surfer provides a list of NLP-identified terms with target frequency ranges, and the skill identifies which terms are missing, underused, or overused in the content. It calculates a content score (0-100) matching Surfer’s scoring methodology based on weighted compliance across all ranking factors. The skill suggests specific insertions: where to add missing terms naturally, which headings to restructure, and where additional paragraphs or images would improve the score. For title tag optimization, it checks character length (50-60 chars), keyword position (front-loaded preferred), and power word inclusion. Meta description optimization targets 150-160 characters with keyword inclusion and call-to-action phrasing. Output includes a before/after content score comparison, itemized recommendations with priority ranking, and an auto-optimized version of the content with changes highlighted.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/surfer-seo-content-optimizer-integration/)
