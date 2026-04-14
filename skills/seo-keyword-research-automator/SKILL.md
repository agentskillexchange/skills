---
title: "SEO Keyword Research Automator"
description: "Automated keyword research using DataForSEO API and Google Search Console API. Performs SERP analysis, keyword clustering with TF-IDF scoring, and generates content briefs with search intent classification."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/seo-keyword-research-automator/"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Gemini"
---

# SEO Keyword Research Automator

The SEO Keyword Research Automator combines DataForSEO API for comprehensive SERP data collection with Google Search Console API for first-party performance metrics. It automates the entire keyword research pipeline from seed keyword expansion to final content brief generation.

The agent performs bulk keyword analysis including search volume, keyword difficulty, CPC data, and SERP feature detection through DataForSEO’s Keywords Data endpoints. It clusters related keywords using TF-IDF scoring and cosine similarity, grouping them by search intent categories: informational, navigational, transactional, and commercial investigation.

Advanced capabilities include competitor gap analysis by cross-referencing ranking domains, content brief generation with recommended headings and word counts based on top-ranking pages, and automated tracking of keyword position changes via Search Console’s searchAnalytics query endpoint. The agent also identifies featured snippet opportunities and People Also Ask patterns for content optimization.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/seo-keyword-research-automator/)
