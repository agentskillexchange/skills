---
name: "Octokit JavaScript GitHub SDK for REST GraphQL and App Automation"
description: "Octokit is GitHub’s JavaScript SDK family for REST API requests, GraphQL queries, authentication, webhooks, and GitHub App workflows. It gives agents and automation systems a typed, maintained client for working with GitHub from Node.js, browsers, and Deno."
category: "Library &amp; API Reference"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/octokit/octokit.js"
---
# Octokit JavaScript GitHub SDK for REST GraphQL and App Automation

Octokit is GitHub’s JavaScript SDK family for REST API requests, GraphQL queries, authentication, webhooks, and GitHub App workflows. It gives agents and automation systems a typed, maintained client for working with GitHub from Node.js, browsers, and Deno.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill octokit-javascript-github-sdk-rest-graphql-app-automation
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill octokit-javascript-github-sdk-rest-graphql-app-automation -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill octokit-javascript-github-sdk-rest-graphql-app-automation -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill octokit-javascript-github-sdk-rest-graphql-app-automation -a codex
```

### OpenClaw

```bash
clawhub install octokit-javascript-github-sdk-rest-graphql-app-automation
```

## Details

Octokit is the all-in-one JavaScript SDK for GitHub platform automation, maintained under the octokit organization. The package brings together REST API requests, GraphQL queries, authentication helpers, webhook tooling, and GitHub App workflows in a single ecosystem that works across Node.js, browsers, and Deno. For agent workflows, this is the practical foundation for reading repository state, opening issues, managing pull requests, paginating API results, and authenticating either as a personal token holder or as a GitHub App.

This skill is useful when an agent needs a reliable JavaScript client instead of hand-rolling raw fetch calls against GitHub. Octokit exposes endpoint methods, request helpers, retry and throttling support, and extension points for plugins, which makes it suitable for CI tooling, project automation, review bots, release workflows, and repo maintenance services. Because it also supports GitHub Enterprise Server through configurable base URLs, it works beyond public github.com installs.

Integration points include Node.js services, CLIs, serverless functions, browser-based internal tools, webhook consumers, and GitHub App backends. The upstream repo is actively maintained and MIT licensed, while the npm package provides the standard installation path used in the README. That combination gives this candidate a concrete job-to-be-done and multiple independent verification signals: official repo, package distribution, tagged releases, and documented usage for GitHub automation.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/octokit-javascript-github-sdk-rest-graphql-app-automation/)
