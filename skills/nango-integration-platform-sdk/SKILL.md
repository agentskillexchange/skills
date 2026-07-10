---
name: "Nango Integration Platform SDK"
slug: "nango-integration-platform-sdk"
description: "Nango is an integration platform for connecting products and agents to hundreds of APIs with managed auth, proxying, and function execution. This skill covers how to use the real Nango project for OAuth-backed integrations, API tool calling, and production sync workflows."
github_stars: 7092
verification: "security_reviewed"
source: "https://github.com/NangoHQ/nango"
author: "NangoHQ"
publisher_type: "Company"
category: "Integrations & Connectors"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "NangoHQ/nango"
  github_stars: 7092
  npm_package: "nango"
  npm_weekly_downloads: 17748
---

# Nango Integration Platform SDK

Nango is an integration platform for connecting products and agents to hundreds of APIs with managed auth, proxying, and function execution. This skill covers how to use the real Nango project for OAuth-backed integrations, API tool calling, and production sync workflows.

## Prerequisites

Node.js, TypeScript

## Installation

Use the upstream install or setup path that matches your environment:
- Make authenticated API requests on behalf of your users. Send requests through Nango's proxy: it resolves the provider, injects credentials, handles retries and rate limits, and returns the response.

Requirements and caveats from upstream:
- [![NPM Downloads](https://img.shields.io/npm/dm/@nangohq/node)](https://www.npmjs.com/package/@nangohq/node)
- import { Nango } from '@nangohq/node';

Basic usage or getting-started notes:
- Connect your product & AI agents with 700+ APIs. Build, run, and maintain integrations with AI in code, on infrastructure built for scale.
- export default async function run(nango: Nango) {
- Get up and running in under 5 minutes:

- Source: https://github.com/NangoHQ/nango
- Extracted from upstream docs: https://raw.githubusercontent.com/NangoHQ/nango/HEAD/README.md

## Documentation

- https://nango.dev/docs/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nango-integration-platform-sdk/)
