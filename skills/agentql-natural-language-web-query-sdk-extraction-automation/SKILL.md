---
title: "AgentQL Natural Language Web Query SDK for Extraction and Automation"
description: "AgentQL is TinyFish’s web automation and extraction toolkit that layers a natural-language query system on top of live sites. Its Python and JavaScript SDKs integrate with Playwright and let agents target data and interface elements without depending on brittle CSS selectors alone."
verification: "security_reviewed"
source: "https://github.com/tinyfish-io/agentql"
category:
  - "Research & Scraping"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "tinyfish-io/agentql"
  github_stars: 1312
  ase_npm_package: "agentql"
  npm_weekly_downloads: 878
  license: "MIT"
---

# AgentQL Natural Language Web Query SDK for Extraction and Automation

AgentQL is a web extraction and automation toolkit from TinyFish that adds a natural-language query layer on top of live browser sessions. The official repository describes it as a suite that includes Python and JavaScript SDKs, a REST API, a browser debugger, and integrations with tools such as Playwright. Instead of forcing developers to handcraft and maintain a pile of selectors, AgentQL lets them define structured outputs and target elements using higher-level queries tied to the meaning of the page.


That makes it especially relevant for agent workflows where the same job needs to survive layout changes across different sites or repeated runs over time. The upstream docs show common patterns including site login, infinite scroll, product comparison, cookie and popup handling, remote browser use, and structured data extraction. For a team building browsing or scraping agents, those are concrete jobs-to-be-done rather than vague capability claims.


Integration is clear from the source material. The Python SDK installs from PyPI, uses Playwright as the default web driver, requires an AGENTQL_API_KEY, and can be initialized through the CLI or manual setup. The project also has a published npm package and maintained docs, which gives this skill enough source-backed evidence to pass the intake gate. In ASE terms, this belongs in Research & Scraping because it is built for robust web data collection and workflow automation on real pages.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/agentql-natural-language-web-query-sdk-extraction-automation/)
