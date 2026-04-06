---
name: SEO Content Cluster Generator
description: Builds topical authority clusters using SEMrush Keyword Magic API, Ahrefs
  Content Explorer, and Google Search Console API. Generates pillar pages with internal
  linking maps and schema.org Article markup.
category: "Content Writing &amp; SEO"
framework: Claude Agents
verification: security_reviewed
source: "https://agentskillexchange.com/skills/seo-content-cluster-generator/"
---
# SEO Content Cluster Generator

Builds topical authority clusters using SEMrush Keyword Magic API, Ahrefs Content Explorer, and Google Search Console API. Generates pillar pages with internal linking maps and schema.org Article markup.

This skill creates comprehensive SEO content clusters designed to build topical authority. It starts with keyword research using the SEMrush Keyword Magic Tool API to identify seed keywords, related terms, and question-based queries with search volume and keyword difficulty scores. The Ahrefs Content Explorer API analyzes top-ranking content for word count benchmarks, referring domain patterns, and content gap opportunities. Google Search Console API integration via google.webmasters.searchanalytics.query identifies existing ranking positions and impression opportunities. The agent generates pillar page outlines with H2/H3 heading structures optimized for featured snippets. Internal linking maps connect cluster pages to pillar content using contextual anchor text variations. Each piece includes schema.org Article structured data with author, datePublished, and mainEntityOfPage properties for rich result eligibility. Meta descriptions are crafted within the 155-character limit with primary keyword placement. The skill tracks content performance through Google Analytics 4 Data API engagement metrics including average_session_duration and scroll_depth events.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill seo-content-cluster-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill seo-content-cluster-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill seo-content-cluster-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill seo-content-cluster-generator -a codex
```

### OpenClaw

```bash
clawhub install seo-content-cluster-generator
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/seo-content-cluster-generator/)
