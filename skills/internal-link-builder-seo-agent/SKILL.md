---
name: Internal Link Builder
description: Analyzes site content graph using Screaming Frog SEO Spider API and builds
  internal linking recommendations. Calculates PageRank distribution using networkx
  graph algorithms.
verification: security_reviewed
source: https://agentskillexchange.com/skills/internal-link-builder-seo-agent/
category:
- Content Writing &amp; SEO
framework:
- Claude Agents
---
# Internal Link Builder

The Internal Link Builder analyzes website content structure to optimize internal linking for SEO performance. It uses the Screaming Frog SEO Spider API to crawl the site and build a complete link graph including anchor text, follow/nofollow attributes, and HTTP status codes. The skill calculates internal PageRank distribution using the networkx Python library with customizable damping factors to identify pages that need more internal link equity. Orphan pages with zero internal links are automatically detected and matched with semantically related content using TF-IDF vectorization via scikit-learn. The skill generates specific linking recommendations with suggested anchor text variants that avoid over-optimization penalties. Content gap analysis identifies topical clusters with weak interconnection using community detection algorithms from the python-louvain library. For WordPress sites, recommendations can be automatically implemented via the WordPress REST API by injecting contextual links into post content. Reports include interactive D3.js force-directed graph visualizations of the site's link structure with PageRank-sized nodes.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/internal-link-builder-seo-agent/)
