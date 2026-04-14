---
title: "Linkup JS SDK for Sourced Web Search and Fetch"
description: "Linkup’s JS SDK wraps the Linkup API for sourced web search and clean content fetching. It gives agents a maintained client for standard and deep search modes, plus URL fetch operations that can return rendered page content in a cleaner form for downstream reasoning."
verification: security_reviewed
source: "https://github.com/LinkupPlatform/linkup-js-sdk"
category:
  - "Library &amp; API Reference"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "LinkupPlatform/linkup-js-sdk"
  github_stars: 4
---

# Linkup JS SDK for Sourced Web Search and Fetch

Linkup JS SDK is the official JavaScript and TypeScript client for the Linkup API. The upstream repository and docs describe a simple client for running standard and deep search queries, as well as fetching page content in cleaned markdown form. The npm package exposes a practical integration point for developers who want sourced answers and web retrieval without building every request and response transform manually.

For agent workflows, the job-to-be-done is straightforward. An agent can call Linkup to search for current information, switch to a deeper search mode for more complex queries, or fetch a specific URL with JavaScript rendering enabled when the target page depends on client-side execution. That combination makes the tool relevant for research assistants, monitoring agents, answer synthesis pipelines, and retrieval-heavy automations that need a documented SDK rather than ad hoc scraping logic.

The upstream README documents installation from npm, client creation with an API key, and examples for both search and fetch endpoints. The official documentation site provides SDK references and implementation details. Although the repository is smaller than some other candidates, it meets the intake bar because it has a public official repo, npm package, docs, license, tagged releases, and recent maintenance activity. Those factors are enough to publish it at the verified metadata tier while leaving security promotion to the separate scanner workflow.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/linkup-js-sdk-sourced-web-search-fetch/)
