---
title: "SearXNG Privacy-First Metasearch Engine and Search API"
description: "SearXNG is an open-source metasearch engine that aggregates results from multiple search providers without tracking users. It fits research and scraping workflows that need self-hosted search, configurable engines, and a documented admin surface for search aggregation and result control."
verification: "security_reviewed"
source: "https://github.com/searxng/searxng"
category:
  - "Research &amp; Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "searxng/searxng"
  github_stars: 28324
  license: "AGPL-3.0"
---

# SearXNG Privacy-First Metasearch Engine and Search API

SearXNG is a self-hostable metasearch engine that aggregates results from many search providers and databases while avoiding user tracking and profiling. For agent and automation workflows, the core job to be done is straightforward: run a privacy-preserving search layer you control, then tune its engines and behavior to fit internal research, discovery, or retrieval use cases. Because it is open source and actively maintained, teams can inspect the code, deploy their own instance, and configure upstream sources instead of depending entirely on a single commercial search endpoint.

The project is useful in research pipelines, internal discovery portals, scraping-adjacent workflows, and privacy-conscious assistant systems that need a configurable search backend. Its documentation covers installation, administration, and settings, which matters for operators who want to manage engines, ranking, request handling, and deployment details from a single codebase. The repository also publishes license information and shows recent commit activity, which helps validate that the project is live and maintained.

As a marketplace skill entry, SearXNG belongs on the practical infrastructure side of research automation. It is not just a generic search concept; it is a concrete upstream project with a documented installation path, a real community, and clear operational value for users who want search aggregation under their own control.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/searxng-privacy-first-metasearch-engine-search-api/)
