---
name: "Give coding agents runtime context for Encore services"
slug: "give-coding-agents-runtime-context-for-encore-services"
description: "Use Encore's AI integration and built-in MCP server so an agent can inspect service architecture, query local resources, call APIs, and analyze traces while iterating on TypeScript or Go backends."
github_stars: 11921
verification: "security_reviewed"
source: "https://github.com/encoredev/encore"
author: "Encore"
publisher_type: "open_source_project"
category: "Developer Tools"
framework: "MCP"
tool_ecosystem:
  github_repo: "encoredev/encore"
  github_stars: 11921
---

# Give coding agents runtime context for Encore services

Use Encore's AI integration and built-in MCP server so an agent can inspect service architecture, query local resources, call APIs, and analyze traces while iterating on TypeScript or Go backends.

## Prerequisites

Encore CLI; Encore TypeScript or Go project; agent runtime with MCP support

## Installation

Requirements and caveats from upstream:
- **Self-hosted:** Use the Encore CLI to export your app as Docker images, then supply your infra config to host anywhere.
- This includes all code needed for local development, everything that runs in your application when it is deployed, and everything needed to generate a Docker image for your application, so you can easily deploy your a...
- Should you want to migrate away, it's straightforward and does not require a big rewrite. 99% of your code is regular Go or TypeScript.

Basic usage or getting-started notes:
- **Framework:** The Encore framework, available for TypeScript and Go, lets you define APIs, services, and infrastructure (databases, Pub/Sub, caching, buckets, cron jobs) as type-safe objects in your code. Write your...
- **TypeScript:** encore app create --example=ts/hello-world
- **Go:** encore app create --example=hello-world

- Source: https://github.com/encoredev/encore
- Extracted from upstream docs: https://raw.githubusercontent.com/encoredev/encore/HEAD/README.md

## Documentation

- https://encore.dev/docs/ts/ai-integration

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/give-coding-agents-runtime-context-for-encore-services/)
