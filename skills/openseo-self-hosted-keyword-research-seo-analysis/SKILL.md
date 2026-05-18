---
name: "OpenSEO Self-Hosted Keyword Research and SEO Analysis Platform"
slug: "openseo-self-hosted-keyword-research-seo-analysis"
description: "OpenSEO is an open-source, self-hostable SEO platform that provides keyword research, domain insights, backlink analysis, and site audits. It serves as a pay-as-you-go alternative to Semrush and Ahrefs, powered by DataForSEO APIs with no subscription required."
github_stars: 783
verification: "listed"
source: "https://github.com/every-app/open-seo"
category: "Content Writing & SEO"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "every-app/open-seo"
  github_stars: 783
---

# OpenSEO Self-Hosted Keyword Research and SEO Analysis Platform

OpenSEO is an open-source, self-hostable SEO platform that provides keyword research, domain insights, backlink analysis, and site audits. It serves as a pay-as-you-go alternative to Semrush and Ahrefs, powered by DataForSEO APIs with no subscription required.

## Installation

Use the upstream install or setup path that matches your environment:
- Docker is recommended for getting started. It's super easy to get up and running once you install Docker.
- Install Docker: https://www.docker.com/products/docker-desktop/
- docker compose pull
- docker compose up -d

Requirements and caveats from upstream:
- [Docker Self Hosting](#docker-self-hosting)
- Backlinks requires one more step beyond the API key: you also need DataForSEO Backlinks enabled on your account (trial or paid subscription), then confirm access from the Backlinks page in OpenSEO.
- Docker self-hosting: .env

Basic usage or getting-started notes:
- DataForSEO API: pay-as-you-go based on usage.
- cp .env.example .env
- Set DATAFORSEO_API_KEY in .env

- Source: https://github.com/every-app/open-seo
- Extracted from upstream docs: https://raw.githubusercontent.com/every-app/open-seo/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openseo-self-hosted-keyword-research-seo-analysis/)
