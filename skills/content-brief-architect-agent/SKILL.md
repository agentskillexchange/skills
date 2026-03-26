---
name: "Content Brief Architect"
description: "Creates detailed SEO content briefs using Ahrefs API keyword data, SurferSEO NLP analysis, and Clearscope content grading. Generates outlines with target word counts, headers, and semantic keyword clusters."
category: "Content Writing & SEO"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/content-brief-architect-agent/"
tool_ecosystem:
  tool: "notion"
  github_stars: 5562
  npm_weekly_downloads: 1084242
  github_repo: "makenotion/notion-sdk-js"
  license: "MIT"
  maintained: true
---

# Content Brief Architect

Creates detailed SEO content briefs using Ahrefs API keyword data, SurferSEO NLP analysis, and Clearscope content grading. Generates outlines with target word counts, headers, and semantic keyword clusters.

## Overview

The Content Brief Architect generates comprehensive, data-driven content briefs for SEO writers and content teams. It pulls keyword data from the Ahrefs API including search volume, keyword difficulty, SERP features, and parent topic analysis. The agent performs competitive content analysis using SurferSEO NLP processing to identify required semantic terms, optimal word counts, and header structures from top-ranking pages. It integrates with Clearscope for content scoring benchmarks and generates target grades for each brief. The architect creates detailed outlines with H2/H3 header suggestions, internal linking targets from existing site content (crawled via Screaming Frog API or Sitebulb), and external authority link recommendations. It analyzes People Also Ask data from Google SERP API to generate FAQ sections, identifies featured snippet opportunities through SERP feature analysis, and creates content calendars with topic clustering using the MarketMuse API. Briefs are exported as Google Docs via the Docs API v1 with formatted templates, Notion pages via Notion API, or Markdown files for CMS import.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill content-brief-architect-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill content-brief-architect-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill content-brief-architect-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill content-brief-architect-agent -a codex
```

### OpenClaw

```bash
clawhub install content-brief-architect-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/content-brief-architect-agent/
