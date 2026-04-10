---
title: "SEO Content Cluster Generator"
description: "Builds topical authority clusters using SEMrush Keyword Magic API, Ahrefs Content Explorer, and Google Search Console API. Generates pillar pages with internal linking maps and schema.org Article markup."
slug: "seo-content-cluster-generator"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/seo-content-cluster-generator/"
---

# SEO Content Cluster Generator

Builds topical authority clusters using SEMrush Keyword Magic API, Ahrefs Content Explorer, and Google Search Console API. Generates pillar pages with internal linking maps and schema.org Article markup.

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
clawhub install seo-content-cluster-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill creates comprehensive SEO content clusters designed to build topical authority. It starts with keyword research using the SEMrush Keyword Magic Tool API to identify seed keywords, related terms, and question-based queries with search volume and keyword difficulty scores. The Ahrefs Content Explorer API analyzes top-ranking content for word count benchmarks, referring domain patterns, and content gap opportunities. Google Search Console API integration via google.webmasters.searchanalytics.query identifies existing ranking positions and impression opportunities. The agent generates pillar page outlines with H2/H3 heading structures optimized for featured snippets. Internal linking maps connect cluster pages to pillar content using contextual anchor text variations. Each piece includes schema.org Article structured data with author, datePublished, and mainEntityOfPage properties for rich result eligibility. Meta descriptions are crafted within the 155-character limit with primary keyword placement. The skill tracks content performance through Google Analytics 4 Data API engagement metrics including average_session_duration and scroll_depth events.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/seo-content-cluster-generator/)
