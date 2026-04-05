---
name: "Bruno Git-Native API Client for Testing and Exploration"
description: "Bruno is an open-source, offline-first API client that stores collections as plain-text .bru files on your filesystem. It serves as a privacy-focused, git-friendly alternative to Postman and Insomnia with no cloud sync and no account required."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/usebruno/bruno"
tool_ecosystem:
  tool: bruno
  github_repo: usebruno/bruno
  github_stars: 42477
---
# Bruno Git-Native API Client for Testing and Exploration

Bruno is an open-source, offline-first API client that stores collections as plain-text .bru files on your filesystem. It serves as a privacy-focused, git-friendly alternative to Postman and Insomnia with no cloud sync and no account required.

## Overview

Bruno is an open-source API client that takes a fundamentally different approach to API collection management compared to Postman or Insomnia. Instead of storing API requests in proprietary cloud formats, Bruno saves everything as plain-text `.bru` files directly on the developer’s filesystem. With over 40,000 GitHub stars and growing, it has become one of the most popular API testing tools in the open-source ecosystem.

The core philosophy is offline-first and git-native. API collections live as regular files in a project directory, which means they can be version-controlled alongside application code using Git or any VCS. Teams collaborate on API definitions through pull requests and code review, not through shared cloud workspaces with opaque sync mechanisms. There are no accounts to create, no subscriptions to manage, and no data leaving the developer’s machine.

Bruno supports REST, GraphQL, and gRPC requests with a clean interface that will feel familiar to Postman users. It includes environment variables, request chaining, pre-request and post-request scripts (written in JavaScript), assertions for automated testing, and a CLI runner (`bru`) for headless execution in CI/CD pipelines. The Bru markup language is human-readable and diffable, making code review of API changes practical.

An agent skill built on Bruno enables automated API collection management, test suite execution, environment configuration, and CI integration. The skill can create and modify `.bru` files programmatically, run collections against different environments, and report test results. It integrates well with git workflows where API contracts are treated as code artifacts.

Bruno is available via Homebrew, Chocolatey, Scoop, Snap, Flatpak, and apt. It runs on Mac, Windows, and Linux. The project uses the MIT license for the open-source edition.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill bruno-git-native-api-client-testing-exploration
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill bruno-git-native-api-client-testing-exploration -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill bruno-git-native-api-client-testing-exploration -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill bruno-git-native-api-client-testing-exploration -a codex
```

### OpenClaw

```bash
clawhub install bruno-git-native-api-client-testing-exploration
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/bruno-git-native-api-client-testing-exploration/)
