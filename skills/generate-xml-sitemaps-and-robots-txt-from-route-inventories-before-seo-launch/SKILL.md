---
title: "Generate XML sitemaps and robots.txt from route inventories before SEO launch"
description: "Use sitemap when an agent already knows the site routes or content URLs and needs valid sitemap XML, sitemap indexes, or robots.txt references before launch. This is a publishing-artifact skill, not a crawler or SEO platform."
verification: "security_reviewed"
source: "https://github.com/ekalinin/sitemap.js"
category:
  - "Content Writing & SEO"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ekalinin/sitemap.js"
  github_stars: 1708
---

# Generate XML sitemaps and robots.txt from route inventories before SEO launch

This skill uses sitemap (sitemap.js), the Node.js library and CLI for generating sitemap XML from known URLs and for managing sitemap indexes at larger scales. In agent workflows, it shines when the site structure is already available from a CMS export, route manifest, database query, or content inventory and the missing piece is the final sitemap output that search engines expect. Rather than hand-writing XML or leaning on a broad SEO platform, the agent can emit valid sitemap artifacts directly from the route list it already has.


The concrete job-to-be-done is sitemap generation before a launch, migration, bulk content publish, or SEO QA pass. Invoke it when an automation needs to turn a trusted list of URLs into sitemap.xml, split large inventories across indexed sitemap files, or validate and update sitemap outputs as content changes. The upstream project also documents CLI usage for one-shot sitemap generation from plain URL lists, which is especially useful for agents operating in build pipelines or release checklists.


The scope boundary is what keeps this skill from collapsing into a generic SEO product card. sitemap generates sitemap and sitemap-index artifacts, plus related robots.txt references, but it does not crawl the web, score rankings, audit backlinks, or replace a technical SEO suite. Integration points are Node.js build steps, static-site deploy pipelines, CMS export jobs, CI release tasks, and scripts that already have the canonical URLs in hand. When the agent needs deterministic XML output from a route inventory, this is the right tool and the right scope.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-xml-sitemaps-and-robots-txt-from-route-inventories-before-seo-launch/)
