---
name: "SEO Keyword Research Automator"
description: "Automated keyword research using DataForSEO API and Google Search Console API. Performs SERP analysis, keyword clustering with TF-IDF scoring, and generates content briefs with search intent classification."
category: "Content Writing &amp; SEO"
framework: "Gemini"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/seo-keyword-research-automator/"
---
# SEO Keyword Research Automator

Automated keyword research using DataForSEO API and Google Search Console API. Performs SERP analysis, keyword clustering with TF-IDF scoring, and generates content briefs with search intent classification.

## Overview

The SEO Keyword Research Automator combines DataForSEO API for comprehensive SERP data collection with Google Search Console API for first-party performance metrics. It automates the entire keyword research pipeline from seed keyword expansion to final content brief generation.

The agent performs bulk keyword analysis including search volume, keyword difficulty, CPC data, and SERP feature detection through DataForSEO's Keywords Data endpoints. It clusters related keywords using TF-IDF scoring and cosine similarity, grouping them by search intent categories: informational, navigational, transactional, and commercial investigation.

Advanced capabilities include competitor gap analysis by cross-referencing ranking domains, content brief generation with recommended headings and word counts based on top-ranking pages, and automated tracking of keyword position changes via Search Console's searchAnalytics query endpoint. The agent also identifies featured snippet opportunities and People Also Ask patterns for content optimization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill seo-keyword-research-automator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill seo-keyword-research-automator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill seo-keyword-research-automator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill seo-keyword-research-automator -a codex
```

### OpenClaw

```bash
clawhub install seo-keyword-research-automator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/seo-keyword-research-automator/)
