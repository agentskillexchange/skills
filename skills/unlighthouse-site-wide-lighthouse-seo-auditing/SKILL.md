---
title: "Unlighthouse Site-Wide Lighthouse and SEO Auditing"
description: "Unlighthouse is a site-wide auditing tool that runs Google Lighthouse across many URLs and turns the results into an actionable view of SEO, performance, accessibility, and best-practice issues. This skill uses Unlighthouse when an agent needs more than a one-page Lighthouse check. It can crawl a site, discover important routes, execute repeated Lighthouse runs, and summarize which pages have the biggest problems or the clearest optimization wins. For content and SEO workflows, the skill is useful for finding missing metadata patterns, weak indexability signals, poor internal page quality, slow templates, and route-level regressions that affect search visibility. The agent can scope the run to a sitemap, a development preview, or a production domain, then interpret the Unlighthouse output into a concise worklist. Typical outputs include page-level SEO scores, Lighthouse category scores, recurring template issues, and prioritized remediation notes grouped by severity or URL pattern. Integration points include CI pipelines, content refresh workflows, technical SEO audits, and reporting automations that need machine-readable output. Because Unlighthouse is available as an npm package and has dedicated documentation, it fits agent environments that already run Node-based tooling. The skill explicitly references concepts such as crawl discovery, Lighthouse scoring, route sampling, sitemap inputs, page templates, Core Web Vitals context, and structured issue summaries. Rather than treating SEO review as generic advice, the skill anchors the work in Unlighthouse runs so the agent can produce evidence-backed recommendations tied to specific URLs, categories of defects, and measurable audit output."
source: "https://github.com/harlan-zw/unlighthouse"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "harlan-zw/unlighthouse"
  github_stars: 4469
  npm_package: "unlighthouse"
  npm_weekly_downloads: 15320
---

# Unlighthouse Site-Wide Lighthouse and SEO Auditing

Unlighthouse is a site-wide auditing tool that runs Google Lighthouse across many URLs and turns the results into an actionable view of SEO, performance, accessibility, and best-practice issues. This skill uses Unlighthouse when an agent needs more than a one-page Lighthouse check. It can crawl a site, discover important routes, execute repeated Lighthouse runs, and summarize which pages have the biggest problems or the clearest optimization wins. For content and SEO workflows, the skill is useful for finding missing metadata patterns, weak indexability signals, poor internal page quality, slow templates, and route-level regressions that affect search visibility. The agent can scope the run to a sitemap, a development preview, or a production domain, then interpret the Unlighthouse output into a concise worklist. Typical outputs include page-level SEO scores, Lighthouse category scores, recurring template issues, and prioritized remediation notes grouped by severity or URL pattern. Integration points include CI pipelines, content refresh workflows, technical SEO audits, and reporting automations that need machine-readable output. Because Unlighthouse is available as an npm package and has dedicated documentation, it fits agent environments that already run Node-based tooling. The skill explicitly references concepts such as crawl discovery, Lighthouse scoring, route sampling, sitemap inputs, page templates, Core Web Vitals context, and structured issue summaries. Rather than treating SEO review as generic advice, the skill anchors the work in Unlighthouse runs so the agent can produce evidence-backed recommendations tied to specific URLs, categories of defects, and measurable audit output.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/unlighthouse-site-wide-lighthouse-seo-auditing/)
