---
name: "Mock AI app dependencies for deterministic local and CI tests"
slug: "mock-ai-app-dependencies-for-deterministic-local-and-ci-tests"
description: "Use AiMock when an agent needs reproducible tests around LLM APIs, MCP tools, A2A flows, vector stores, search, or moderation services without depending on live providers."
github_stars: 324
verification: "security_reviewed"
source: "https://github.com/CopilotKit/aimock"
author: "CopilotKit"
publisher_type: "company"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "CopilotKit/aimock"
  github_stars: 324
  npm_package: "@copilotkit/aimock"
  npm_weekly_downloads: 6430
---

# Mock AI app dependencies for deterministic local and CI tests

Use AiMock when an agent needs reproducible tests around LLM APIs, MCP tools, A2A flows, vector stores, search, or moderation services without depending on live providers.

## Prerequisites

Node.js; a JavaScript or TypeScript test environment; local or CI access to the app under test; fixture definitions for the providers or protocols you want to mock.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install @copilotkit/aimock
- npx -p @copilotkit/aimock llmock -p 4010 -f ./fixtures
- npx -p @copilotkit/aimock llmock -p 4010 \
- npx @copilotkit/aimock --config aimock.json

Requirements and caveats from upstream:
- process.env.OPENAI_API_KEY = "mock"; // SDK requires a value, even when base URL is mocked
- **[Docker + Helm](https://aimock.copilotkit.dev/docker)** — Container image and Helm chart for CI/CD
- **Zero dependencies** — Everything from Node.js builtins

Basic usage or getting-started notes:
- bash
- typescript
- // The class is still named LLMock for back-compat after the v1.7.0 package

- Source: https://github.com/CopilotKit/aimock
- Extracted from upstream docs: https://raw.githubusercontent.com/CopilotKit/aimock/HEAD/README.md

## Documentation

- https://aimock.copilotkit.dev/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mock-ai-app-dependencies-for-deterministic-local-and-ci-tests/)
