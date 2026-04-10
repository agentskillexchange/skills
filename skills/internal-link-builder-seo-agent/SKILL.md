---
title: "Internal Link Builder"
description: "Analyzes site content graph using Screaming Frog SEO Spider API and builds internal linking recommendations. Calculates PageRank distribution using networkx graph algorithms."
slug: "internal-link-builder-seo-agent"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/internal-link-builder-seo-agent/"
listed: true
---

# Internal Link Builder

Analyzes site content graph using Screaming Frog SEO Spider API and builds internal linking recommendations. Calculates PageRank distribution using networkx graph algorithms.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install internal-link-builder-seo-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Internal Link Builder analyzes website content structure to optimize internal linking for SEO performance. It uses the Screaming Frog SEO Spider API to crawl the site and build a complete link graph including anchor text, follow/nofollow attributes, and HTTP status codes. The skill calculates internal PageRank distribution using the networkx Python library with customizable damping factors to identify pages that need more internal link equity. Orphan pages with zero internal links are automatically detected and matched with semantically related content using TF-IDF vectorization via scikit-learn. The skill generates specific linking recommendations with suggested anchor text variants that avoid over-optimization penalties. Content gap analysis identifies topical clusters with weak interconnection using community detection algorithms from the python-louvain library. For WordPress sites, recommendations can be automatically implemented via the WordPress REST API by injecting contextual links into post content. Reports include interactive D3.js force-directed graph visualizations of the site’s link structure with PageRank-sized nodes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/internal-link-builder-seo-agent/)
