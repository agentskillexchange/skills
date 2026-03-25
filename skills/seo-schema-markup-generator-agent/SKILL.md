---
name: "SEO Schema Markup Generator"
description: "Generates JSON-LD structured data for articles, products, FAQs, and local business schemas using Schema.org vocabulary. Validates output against Google Rich Results Test API and Yoast SEO wp_head hooks."
category: "Content Writing & SEO"
framework: "OpenClaw"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/seo-schema-markup-generator-agent/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "wordpress"  # from ase_tool_match
  github_stars: 20976  # from ase_github_stars (integer, not string)
  github_repo: "WordPress/WordPress"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# SEO Schema Markup Generator

Generates JSON-LD structured data for articles, products, FAQs, and local business schemas using Schema.org vocabulary. Validates output against Google Rich Results Test API and Yoast SEO wp_head hooks.

## Overview

The SEO Schema Markup Generator creates comprehensive JSON-LD structured data following Schema.org specifications for improved search engine visibility. It generates Article, Product, FAQPage, HowTo, LocalBusiness, and Organization schemas with proper nesting and required properties. The agent validates all generated markup against the Google Rich Results Test API and checks compatibility with the Search Console structured data reports. It integrates with Yoast SEO through the wpseo_json_ld_output filter and Rank Math via rank_math/json_ld hook for WordPress sites. The generator supports dynamic schema generation from page content using natural language processing to extract FAQ pairs, product attributes, and review ratings. It handles breadcrumb schema via BreadcrumbList type with automatic URL hierarchy detection, generates VideoObject schema from embedded YouTube and Vimeo content using their oEmbed APIs, and creates SiteNavigationElement schemas from menu structures. Output is minified and injected via wp_head action with proper script type application/ld+json.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill seo-schema-markup-generator-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill seo-schema-markup-generator-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill seo-schema-markup-generator-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill seo-schema-markup-generator-agent -a codex
```

### OpenClaw

```bash
clawhub install seo-schema-markup-generator-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/seo-schema-markup-generator-agent/
