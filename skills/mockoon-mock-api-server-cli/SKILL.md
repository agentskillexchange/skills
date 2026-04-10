---
name: Mockoon Local Mock API Server and CLI for API Development
description: Mockoon is the fastest way to run mock REST APIs locally. It provides
  a desktop application and a CLI for creating mock API servers with dynamic response
  templates, proxy mode, OpenAPI import, and request logging — no account required,
  fully open source.
verification: security_reviewed
source: https://github.com/mockoon/mockoon
category:
- Developer Tools
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: mockoon/mockoon
  github_stars: 8196
---
# Mockoon Local Mock API Server and CLI for API Development

Overview
Mockoon is an open-source tool for creating mock API servers quickly and without complexity. Available as a cross-platform desktop application (Electron-based) and a CLI (@mockoon/cli), it lets developers design complete mock API environments with realistic responses, dynamic templating, proxy forwarding, and CORS handling. Mockoon supports importing and exporting OpenAPI/Swagger specifications, making it easy to turn API documentation into working mock servers.
How It Works
Mockoon's desktop app provides a visual interface for creating API routes with customizable HTTP methods, paths, status codes, headers, and response bodies. The response templating engine supports Handlebars-like helpers (Faker.js data generation, request body/query/header access, conditional logic, loops) to produce dynamic, realistic responses. Environments can be exported as JSON files and run headlessly via the CLI, making them suitable for CI/CD pipelines and automated testing.
Key Features

Zero-config mock servers: Create and run mock APIs in seconds with the desktop app
CLI for CI/CD: Run mock environments headlessly via @mockoon/cli in Docker, GitHub Actions, and pipelines
Dynamic response templating: Faker.js data, request interpolation, conditional responses, and loops
Proxy mode: Forward unmatched requests to a real API while intercepting specific routes
OpenAPI import/export: Import Swagger/OpenAPI specs to auto-generate mock routes
Request logging: Inspect incoming requests and outgoing responses for debugging
CORS handling: Automatic CORS preflight responses for frontend development
Multiple environments: Run several mock servers on different ports simultaneously
Response rules: Serve different responses based on request body, headers, query params, or cookies

Agent Integration
AI agents can leverage Mockoon for API testing workflows: generating mock servers from OpenAPI specs to test integrations without hitting production endpoints, running mock APIs in CI to validate client code against expected contracts, prototyping new API designs by defining routes and testing them locally, or using the proxy mode to intercept and modify specific API calls during debugging sessions.
Installation
npm install -g @mockoon/cli
Desktop app available at mockoon.com/download. Docker: docker run -p 3000:3000 mockoon/cli:latest
Quick Example
mockoon-cli start --data ./environment.json --port 3000

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mockoon-mock-api-server-cli/)
