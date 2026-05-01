---
title: "Internal Link Builder"
description: "Analyzes site content graph using Screaming Frog SEO Spider API and builds internal linking recommendations. Calculates PageRank distribution using networkx graph algorithms."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/internal-link-builder-seo-agent/"
category:
  - "Content Writing & SEO"
framework:
  - "Claude Agents"
---

# Internal Link Builder

The Internal Link Builder analyzes website content structure to optimize internal linking for SEO performance. It uses the Screaming Frog SEO Spider API to crawl the site and build a complete link graph including anchor text, follow/nofollow attributes, and HTTP status codes. The skill calculates internal PageRank distribution using the networkx Python library with customizable damping factors to identify pages that need more internal link equity. Orphan pages with zero internal links are automatically detected and matched with semantically related content using TF-IDF vectorization via scikit-learn. The skill generates specific linking recommendations with suggested anchor text variants that avoid over-optimization penalties. Content gap analysis identifies topical clusters with weak interconnection using community detection algorithms from the python-louvain library. For WordPress sites, recommendations can be automatically implemented via the WordPress REST API by injecting contextual links into post content. Reports include interactive D3.js force-directed graph visualizations of the site’s link structure with PageRank-sized nodes.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/internal-link-builder-seo-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/internal-link-builder-seo-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/internal-link-builder-seo-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/internal-link-builder-seo-agent/)
