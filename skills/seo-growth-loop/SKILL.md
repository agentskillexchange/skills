---
name: "SEO Growth Loop"
slug: "seo-growth-loop"
description: "Run a closed-loop SEO growth workflow using Search Console data, keyword demand analysis, SERP Authority Mark checks, and the available publishing path. Works across CMS/API, local repo, hybrid, and advisory-only environments."
verification: "listed"
source: "https://github.com/marketingskills/seo-growth-loop"
category: "Content Writing & SEO"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "marketingskills/seo-growth-loop"
---

# SEO Growth Loop

Run a closed-loop SEO growth workflow by gathering real performance data, validating keyword demand, checking SERP competitiveness with Authority Mark, then publishing through whatever safe path the project exposes. Adapts to Claude Code, Codex, OpenCode, and advisory-only environments.

The skill follows an evidence-before-action decision loop: prefer optimizations on existing URLs with real GSC impressions over speculative new pages; validate demand before creating anything net-new; and always verify the rendered output and indexing path.

## Installation

### OpenClaw

```bash
clawhub install seo-growth-loop
```

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/seo-growth-loop ~/.agent-skills/seo-growth-loop
```

### Optional Third-Party Installer

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill seo-growth-loop
```

### Direct from GitHub

```bash
npx skills add marketingskills/seo-growth-loop
```

## How it works

1. **Gather performance** from GSC, Bing, analytics, or rank tracking
2. **Check memory** — read existing SEO logs, topical maps, sitemaps, and live pages
3. **Optimize before building** — improve existing URLs that already have search impressions
4. **Validate demand** with keyword volume and commercial intent
5. **Run Authority Mark** — compare SERP competitor domain authority against the user's site
6. **Choose one justified action** — pick something completeable and verifiable
7. **Publish** through CMS/API, local repo, hybrid, or advisory adapter
8. **Verify** rendered output, indexability, schema, and internal links
9. **Submit for indexing** via IndexNow, Search Console, or sitemap
10. **Log the baseline and change** with follow-up date

## Source

- [GitHub: marketingskills/seo-growth-loop](https://github.com/marketingskills/seo-growth-loop)
- [Agent Skill Exchange](https://agentskillexchange.com/skills/seo-growth-loop/)
