---
name: Linkup JS SDK for Sourced Web Search and Fetch
description: Linkup&#8217;s JS SDK wraps the Linkup API for sourced web search and
  clean content fetching. It gives agents a maintained client for standard and deep
  search modes, plus URL fetch operations that can return rendered page content in
  a cleaner form for downstream reasoning.
verification: security_reviewed
source: https://github.com/LinkupPlatform/linkup-js-sdk
category:
- Library &amp; API Reference
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: LinkupPlatform/linkup-js-sdk
  github_stars: 4
---
# Linkup JS SDK for Sourced Web Search and Fetch

Linkup JS SDK is the official JavaScript and TypeScript client for the Linkup API. The upstream repository and docs describe a simple client for running standard and deep search queries, as well as fetching page content in cleaned markdown form. The npm package exposes a practical integration point for developers who want sourced answers and web retrieval without building every request and response transform manually.
For agent workflows, the job-to-be-done is straightforward. An agent can call Linkup to search for current information, switch to a deeper search mode for more complex queries, or fetch a specific URL with JavaScript rendering enabled when the target page depends on client-side execution. That combination makes the tool relevant for research assistants, monitoring agents, answer synthesis pipelines, and retrieval-heavy automations that need a documented SDK rather than ad hoc scraping logic.
The upstream README documents installation from npm, client creation with an API key, and examples for both search and fetch endpoints. The official documentation site provides SDK references and implementation details. Although the repository is smaller than some other candidates, it meets the intake bar because it has a public official repo, npm package, docs, license, tagged releases, and recent maintenance activity. Those factors are enough to publish it at the verified metadata tier while leaving security promotion to the separate scanner workflow.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/linkup-js-sdk-sourced-web-search-fetch/)
