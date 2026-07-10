---
title: "Mock AI app dependencies for deterministic local and CI tests"
description: "Use AiMock when an agent needs reproducible tests around LLM APIs, MCP tools, A2A flows, vector stores, search, or moderation services without depending on live providers."
verification: "security_reviewed"
source: "https://github.com/CopilotKit/aimock"
author: "CopilotKit"
publisher_type: "company"
category:
  - "Code Quality & Review"
framework:
  - "Multi-Framework"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with npm install @copilotkit/aimock for library use, or run it with npx aimock --config aimock.json for a CLI-driven mock server. Point your app at the mock base URL, define fixtures or record-and-replay behavior for the services you need, and run your tests against those deterministic endpoints instead of live providers.
```

## Documentation

- https://aimock.copilotkit.dev/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mock-ai-app-dependencies-for-deterministic-local-and-ci-tests/)
