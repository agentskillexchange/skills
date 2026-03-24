---
name: "Internal Link Optimizer"
description: "Optimizes internal linking structure using Screaming Frog SEO Spider XML exports and NetworkX graph analysis. Identifies orphan pages, calculates PageRank distribution, and suggests anchor text improvements."
category: "Content Writing & SEO"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/internal-link-optimizer-seo/"
---

# Internal Link Optimizer

Optimizes internal linking structure using Screaming Frog SEO Spider XML exports and NetworkX graph analysis. Identifies orphan pages, calculates PageRank distribution, and suggests anchor text improvements.

## Overview

The Internal Link Optimizer analyzes and improves website internal linking architecture using graph theory applied to crawl data. It processes Screaming Frog SEO Spider XML exports or sitemap data to build comprehensive link graphs with NetworkX for structural analysis.

Core analysis includes orphan page detection, link depth calculation from homepage, PageRank distribution modeling, and internal link equity flow visualization. The agent identifies pages with insufficient internal links, over-linked pages that dilute link equity, and broken internal link chains that create crawl dead ends.

Advanced capabilities include automated anchor text optimization suggestions based on target keyword mapping, topical cluster identification using content similarity scoring, and hub-and-spoke linking pattern generation. The agent creates actionable link insertion recommendations with specific source pages, target URLs, and suggested anchor text. It also monitors link structure changes over time, alerting when new content is published without adequate internal linking.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill internal-link-optimizer-seo
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill internal-link-optimizer-seo -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill internal-link-optimizer-seo -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill internal-link-optimizer-seo -a codex
```

### OpenClaw

```bash
clawhub install internal-link-optimizer-seo
```

## Source

- Marketplace: https://agentskillexchange.com/skills/internal-link-optimizer-seo/
