---
title: AgentQL Natural Language Web Query SDK for Extraction and Automation
description: AgentQL is a web extraction and automation toolkit from TinyFish that
  adds a natural-language query layer on top of live browser sessions. The official
  repository describes it as a suite that includes Python and JavaScript SDKs, a REST
  API, a browser debugger, and integrations with tools such as Playwright. Instead
  of forcing developers to handcraft and maintain a pile of selectors, AgentQL lets
  them define structured outputs and target elements using higher-level queries tied
  to the meaning of the page. That makes it especially relevant for agent workflows
  where the same job needs to survive layout changes across different sites or repeated
  runs over time. The upstream docs show common patterns including site login, infinite
  scroll, product comparison, cookie and popup handling, remote browser use, and structured
  data extraction. For a team building browsing or scraping agents, those are concrete
  jobs-to-be-done rather than vague capability claims. Integration is clear from the
  source material. The Python SDK installs from PyPI, uses Playwright as the default
  web driver, requires an AGENTQL_API_KEY , and can be initialized through the CLI
  or manual setup. The project also has a published npm package and maintained docs,
  which gives this skill enough source-backed evidence to pass the intake gate. In
  ASE terms, this belongs in Research & Scraping because it is built for robust web
  data collection and workflow automation on real pages.
verification: security_reviewed
source: https://github.com/tinyfish-io/agentql
category:
- Research &amp; Scraping
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: tinyfish-io/agentql
  github_stars: 1311
  npm_package: agentql
  npm_weekly_downloads: 953
---

# AgentQL Natural Language Web Query SDK for Extraction and Automation

AgentQL is a web extraction and automation toolkit from TinyFish that adds a natural-language query layer on top of live browser sessions. The official repository describes it as a suite that includes Python and JavaScript SDKs, a REST API, a browser debugger, and integrations with tools such as Playwright. Instead of forcing developers to handcraft and maintain a pile of selectors, AgentQL lets them define structured outputs and target elements using higher-level queries tied to the meaning of the page. That makes it especially relevant for agent workflows where the same job needs to survive layout changes across different sites or repeated runs over time. The upstream docs show common patterns including site login, infinite scroll, product comparison, cookie and popup handling, remote browser use, and structured data extraction. For a team building browsing or scraping agents, those are concrete jobs-to-be-done rather than vague capability claims. Integration is clear from the source material. The Python SDK installs from PyPI, uses Playwright as the default web driver, requires an AGENTQL_API_KEY , and can be initialized through the CLI or manual setup. The project also has a published npm package and maintained docs, which gives this skill enough source-backed evidence to pass the intake gate. In ASE terms, this belongs in Research & Scraping because it is built for robust web data collection and workflow automation on real pages.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/agentql-natural-language-web-query-sdk-extraction-automation/)
