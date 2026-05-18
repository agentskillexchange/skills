---
name: "Run AI browser regression checks with Playwright and multi-model verification through Passmark"
slug: "run-ai-browser-regression-checks-with-playwright-and-multi-model-verification-through-passmark"
description: "Execute natural-language browser regression tests with Playwright, caching, auto-healing, and multi-model assertion verification."
github_stars: 676
verification: "listed"
source: "https://github.com/bug0inc/passmark"
author: "bug0"
publisher_type: "organization"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "bug0inc/passmark"
  github_stars: 676
  npm_package: "passmark"
  npm_weekly_downloads: 12341
---

# Run AI browser regression checks with Playwright and multi-model verification through Passmark

Execute natural-language browser regression tests with Playwright, caching, auto-healing, and multi-model assertion verification.

## Prerequisites

Node.js, Playwright, passmark package, browser test project, model provider keys or AI gateway

## Installation

Use the upstream install or setup path that matches your environment:
- npm init playwright@latest passmark-project # select the default options and set language to TypeScript
- npm install passmark
- Make sure you install dotenv by running npm install dotenv.
- npx playwright test example.spec.ts --project chromium

Requirements and caveats from upstream:
- // if the gateway is authenticated) in your .env file. Cloudflare also requires
- gateway: "none", // CUA requires direct OpenAI access

Basic usage or getting-started notes:
- bash
- cd passmark-project
- We need at least one model from Anthropic and one from Google to use Passmark's multi-model consensus features. Set the required environment variables in .env:

- Source: https://github.com/bug0inc/passmark
- Extracted from upstream docs: https://raw.githubusercontent.com/bug0inc/passmark/HEAD/README.md

## Documentation

- https://passmark.dev

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-ai-browser-regression-checks-with-playwright-and-multi-model-verification-through-passmark/)
