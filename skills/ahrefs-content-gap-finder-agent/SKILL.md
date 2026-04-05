---
name: "Ahrefs Content Gap Finder"
description: "Identifies content gaps using the Ahrefs API v3 /site-explorer/organic-keywords endpoint. Compares competitor keyword profiles and surfaces untapped opportunities with volume, KD, and SERP feature data."
category: "Content Writing &amp; SEO"
framework: "OpenClaw"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ahrefs-content-gap-finder-agent/"
---
# Ahrefs Content Gap Finder

Identifies content gaps using the Ahrefs API v3 /site-explorer/organic-keywords endpoint. Compares competitor keyword profiles and surfaces untapped opportunities with volume, KD, and SERP feature data.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill ahrefs-content-gap-finder-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill ahrefs-content-gap-finder-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill ahrefs-content-gap-finder-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill ahrefs-content-gap-finder-agent -a codex
```

### OpenClaw

```bash
clawhub install ahrefs-content-gap-finder-agent
```

## Details

Ahrefs Content Gap Finder leverages the Ahrefs API v3 to identify keyword opportunities your competitors rank for but you don’t. It queries /site-explorer/organic-keywords for multiple competitor domains, collecting keyword sets with search volume, keyword difficulty (KD), CPC, and current ranking positions.

The agent performs set-difference analysis across competitor keyword profiles, filtering for keywords where at least 2 competitors rank in the top 20 but your domain is absent or ranks below position 50. It enriches results with SERP feature data (featured snippets, PAA boxes, image packs) via /serp-overview to identify quick-win opportunities.

Results are clustered by topical relevance using TF-IDF analysis and organized into content briefs with recommended H2/H3 structures. Each brief includes target keyword, secondary keywords, estimated traffic potential, and suggested word count based on top-ranking page analysis via /site-explorer/best-pages. Outputs to structured JSON, CSV, or formatted markdown for editorial calendars.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ahrefs-content-gap-finder-agent/)
