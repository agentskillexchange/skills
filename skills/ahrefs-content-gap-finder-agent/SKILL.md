---
name: "Ahrefs Content Gap Finder"
description: "Identifies content gaps using the Ahrefs API v3 /site-explorer/organic-keywords endpoint. Compares competitor keyword profiles and surfaces untapped opportunities with volume, KD, and SERP feature data."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/ahrefs-content-gap-finder-agent/"
category:
  - "Content Writing &amp; SEO"
framework:
  - "OpenClaw"
---

# Ahrefs Content Gap Finder

Ahrefs Content Gap Finder leverages the Ahrefs API v3 to identify keyword opportunities your competitors rank for but you don't. It queries /site-explorer/organic-keywords for multiple competitor domains, collecting keyword sets with search volume, keyword difficulty (KD), CPC, and current ranking positions.
The agent performs set-difference analysis across competitor keyword profiles, filtering for keywords where at least 2 competitors rank in the top 20 but your domain is absent or ranks below position 50. It enriches results with SERP feature data (featured snippets, PAA boxes, image packs) via /serp-overview to identify quick-win opportunities.
Results are clustered by topical relevance using TF-IDF analysis and organized into content briefs with recommended H2/H3 structures. Each brief includes target keyword, secondary keywords, estimated traffic potential, and suggested word count based on top-ranking page analysis via /site-explorer/best-pages. Outputs to structured JSON, CSV, or formatted markdown for editorial calendars.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ahrefs-content-gap-finder-agent/)
