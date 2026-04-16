---
title: "Unlighthouse Site-Wide Lighthouse and SEO Auditing"
description: "Unlighthouse runs Google Lighthouse across an entire site instead of just a single page. This skill gives agents a repeatable way to crawl URLs, surface SEO and accessibility issues, and return prioritized audit findings for content and technical optimization work."
verification: "security_reviewed"
source: "https://github.com/harlan-zw/unlighthouse"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "harlan-zw/unlighthouse"
  github_stars: 4469
  ase_npm_package: "unlighthouse"
  npm_weekly_downloads: 15320
  license: "MIT"
---

# Unlighthouse Site-Wide Lighthouse and SEO Auditing

Unlighthouse is a site-wide auditing tool that runs Google Lighthouse across many URLs and turns the results into an actionable view of SEO, performance, accessibility, and best-practice issues. This skill uses Unlighthouse when an agent needs more than a one-page Lighthouse check. It can crawl a site, discover important routes, execute repeated Lighthouse runs, and summarize which pages have the biggest problems or the clearest optimization wins.

For content and SEO workflows, the skill is useful for finding missing metadata patterns, weak indexability signals, poor internal page quality, slow templates, and route-level regressions that affect search visibility. The agent can scope the run to a sitemap, a development preview, or a production domain, then interpret the Unlighthouse output into a concise worklist. Typical outputs include page-level SEO scores, Lighthouse category scores, recurring template issues, and prioritized remediation notes grouped by severity or URL pattern.

Integration points include CI pipelines, content refresh workflows, technical SEO audits, and reporting automations that need machine-readable output. Because Unlighthouse is available as an npm package and has dedicated documentation, it fits agent environments that already run Node-based tooling. The skill explicitly references concepts such as crawl discovery, Lighthouse scoring, route sampling, sitemap inputs, page templates, Core Web Vitals context, and structured issue summaries. Rather than treating SEO review as generic advice, the skill anchors the work in Unlighthouse runs so the agent can produce evidence-backed recommendations tied to specific URLs, categories of defects, and measurable audit output.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/unlighthouse-site-wide-lighthouse-seo-auditing/)
