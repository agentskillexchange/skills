---
title: "Mockoon Local Mock API Server and CLI for API Development"
description: "Mockoon is the fastest way to run mock REST APIs locally. It provides a desktop application and a CLI for creating mock API servers with dynamic response templates, proxy mode, OpenAPI import, and request logging — no account required, fully open source."
slug: "mockoon-mock-api-server-cli"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/mockoon/mockoon"
tool_ecosystem:
  github_repo: "mockoon/mockoon"
  github_stars: 8196
listed: true
---

# Mockoon Local Mock API Server and CLI for API Development

Mockoon is the fastest way to run mock REST APIs locally. It provides a desktop application and a CLI for creating mock API servers with dynamic response templates, proxy mode, OpenAPI import, and request logging — no account required, fully open source.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install mockoon-mock-api-server-cli
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Overview
Mockoon is an open-source tool for creating mock API servers quickly and without complexity. Available as a cross-platform desktop application (Electron-based) and a CLI (@mockoon/cli), it lets developers design complete mock API environments with realistic responses, dynamic templating, proxy forwarding, and CORS handling. Mockoon supports importing and exporting OpenAPI/Swagger specifications, making it easy to turn API documentation into working mock servers.
How It Works
Mockoon’s desktop app provides a visual interface for creating API routes with customizable HTTP methods, paths, status codes, headers, and response bodies. The response templating engine supports Handlebars-like helpers (Faker.js data generation, request body/query/header access, conditional logic, loops) to produce dynamic, realistic responses. Environments can be exported as JSON files and run headlessly via the CLI, making them suitable for CI/CD pipelines and automated testing.
Key Features
- Zero-config mock servers: Create and run mock APIs in seconds with the desktop app
- CLI for CI/CD: Run mock environments headlessly via @mockoon/cli in Docker, GitHub Actions, and pipelines
- Dynamic response templating: Faker.js data, request interpolation, conditional responses, and loops
- Proxy mode: Forward unmatched requests to a real API while intercepting specific routes
- OpenAPI import/export: Import Swagger/OpenAPI specs to auto-generate mock routes
- Request logging: Inspect incoming requests and outgoing responses for debugging
- CORS handling: Automatic CORS preflight responses for frontend development
- Multiple environments: Run several mock servers on different ports simultaneously
- Response rules: Serve different responses based on request body, headers, query params, or cookies
Agent Integration
AI agents can leverage Mockoon for API testing workflows: generating mock servers from OpenAPI specs to test integrations without hitting production endpoints, running mock APIs in CI to validate client code against expected contracts, prototyping new API designs by defining routes and testing them locally, or using the proxy mode to intercept and modify specific API calls during debugging sessions.
Installation
npm install -g @mockoon/cli
Desktop app available at mockoon.com/download. Docker: docker run -p 3000:3000 mockoon/cli:latest
Quick Example
mockoon-cli start --data ./environment.json --port 3000

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mockoon-mock-api-server-cli/)
