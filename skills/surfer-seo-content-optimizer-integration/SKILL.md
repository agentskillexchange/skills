---
title: "Surfer SEO Content Optimizer Integration"
description: "This skill integrates with Surfer SEO&#8217;s content optimization API to analyze and improve content for search engine rankings. It creates content audits via POST to /v1/content_editors with target keyword and country parameters, receiving back NLP-based optimization recommendations. The skill compares existing content against Surfer&#8217;s guidelines for: word count range (min/max based on top-ranking competitors), heading count and structure (H2, H3 distribution), paragraph count, image count, and bold/strong tag usage. The core optimization loop analyzes semantic term coverage—Surfer provides a list of NLP-identified terms with target frequency ranges, and the skill identifies which terms are missing, underused, or overused in the content. It calculates a content score (0-100) matching Surfer&#8217;s scoring methodology based on weighted compliance across all ranking factors. The skill suggests specific insertions: where to add missing terms naturally, which headings to restructure, and where additional paragraphs or images would improve the score. For title tag optimization, it checks character length (50-60 chars), keyword position (front-loaded preferred), and power word inclusion. Meta description optimization targets 150-160 characters with keyword inclusion and call-to-action phrasing. Output includes a before/after content score comparison, itemized recommendations with priority ranking, and an auto-optimized version of the content with changes highlighted."
source: "https://agentskillexchange.com/skills/surfer-seo-content-optimizer-integration/"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Cursor"
---

# Surfer SEO Content Optimizer Integration

This skill integrates with Surfer SEO&#8217;s content optimization API to analyze and improve content for search engine rankings. It creates content audits via POST to /v1/content_editors with target keyword and country parameters, receiving back NLP-based optimization recommendations. The skill compares existing content against Surfer&#8217;s guidelines for: word count range (min/max based on top-ranking competitors), heading count and structure (H2, H3 distribution), paragraph count, image count, and bold/strong tag usage. The core optimization loop analyzes semantic term coverage—Surfer provides a list of NLP-identified terms with target frequency ranges, and the skill identifies which terms are missing, underused, or overused in the content. It calculates a content score (0-100) matching Surfer&#8217;s scoring methodology based on weighted compliance across all ranking factors. The skill suggests specific insertions: where to add missing terms naturally, which headings to restructure, and where additional paragraphs or images would improve the score. For title tag optimization, it checks character length (50-60 chars), keyword position (front-loaded preferred), and power word inclusion. Meta description optimization targets 150-160 characters with keyword inclusion and call-to-action phrasing. Output includes a before/after content score comparison, itemized recommendations with priority ranking, and an auto-optimized version of the content with changes highlighted.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/surfer-seo-content-optimizer-integration/)
