---
name: "Internal Link Builder"
description: "Analyzes site content graph using Screaming Frog SEO Spider API and builds internal linking recommendations. Calculates PageRank distribution using networkx graph algorithms."
category: "Content Writing & SEO"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/internal-link-builder-seo-agent/"
tool_ecosystem:
  tool: "wordpress"
  github_stars: 20976
  github_repo: "WordPress/WordPress"
  maintained: true
---

# Internal Link Builder

Analyzes site content graph using Screaming Frog SEO Spider API and builds internal linking recommendations. Calculates PageRank distribution using networkx graph algorithms.

## Overview

The Internal Link Builder analyzes website content structure to optimize internal linking for SEO performance. It uses the Screaming Frog SEO Spider API to crawl the site and build a complete link graph including anchor text, follow/nofollow attributes, and HTTP status codes. The skill calculates internal PageRank distribution using the networkx Python library with customizable damping factors to identify pages that need more internal link equity. Orphan pages with zero internal links are automatically detected and matched with semantically related content using TF-IDF vectorization via scikit-learn. The skill generates specific linking recommendations with suggested anchor text variants that avoid over-optimization penalties. Content gap analysis identifies topical clusters with weak interconnection using community detection algorithms from the python-louvain library. For WordPress sites, recommendations can be automatically implemented via the WordPress REST API by injecting contextual links into post content. Reports include interactive D3.js force-directed graph visualizations of the site’s link structure with PageRank-sized nodes.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill internal-link-builder-seo-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill internal-link-builder-seo-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill internal-link-builder-seo-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill internal-link-builder-seo-agent -a codex
```

### OpenClaw

```bash
clawhub install internal-link-builder-seo-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/internal-link-builder-seo-agent/
