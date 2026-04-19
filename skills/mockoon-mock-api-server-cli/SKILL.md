---
title: "Mockoon Local Mock API Server and CLI for API Development"
description: "Overview Mockoon is an open-source tool for creating mock API servers quickly and without complexity. Available as a cross-platform desktop application (Electron-based) and a CLI (@mockoon/cli), it lets developers design complete mock API environments with realistic responses, dynamic templating, proxy forwarding, and CORS handling. Mockoon supports importing and exporting OpenAPI/Swagger specifications, making it easy to turn API documentation into working mock servers. How It Works Mockoon&#8217;s desktop app provides a visual interface for creating API routes with customizable HTTP methods, paths, status codes, headers, and response bodies. The response templating engine supports Handlebars-like helpers (Faker.js data generation, request body/query/header access, conditional logic, loops) to produce dynamic, realistic responses. Environments can be exported as JSON files and run headlessly via the CLI, making them suitable for CI/CD pipelines and automated testing. Key Features Zero-config mock servers: Create and run mock APIs in seconds with the desktop app CLI for CI/CD: Run mock environments headlessly via @mockoon/cli in Docker, GitHub Actions, and pipelines Dynamic response templating: Faker.js data, request interpolation, conditional responses, and loops Proxy mode: Forward unmatched requests to a real API while intercepting specific routes OpenAPI import/export: Import Swagger/OpenAPI specs to auto-generate mock routes Request logging: Inspect incoming requests and outgoing responses for debugging CORS handling: Automatic CORS preflight responses for frontend development Multiple environments: Run several mock servers on different ports simultaneously Response rules: Serve different responses based on request body, headers, query params, or cookies Agent Integration AI agents can leverage Mockoon for API testing workflows: generating mock servers from OpenAPI specs to test integrations without hitting production endpoints, running mock APIs in CI to validate client code against expected contracts, prototyping new API designs by defining routes and testing them locally, or using the proxy mode to intercept and modify specific API calls during debugging sessions. Installation npm install -g @mockoon/cli Desktop app available at mockoon.com/download . Docker: docker run -p 3000:3000 mockoon/cli:latest Quick Example mockoon-cli start --data ./environment.json --port 3000"
source: "https://github.com/mockoon/mockoon"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "mockoon/mockoon"
  github_stars: 8196
---

# Mockoon Local Mock API Server and CLI for API Development

Overview Mockoon is an open-source tool for creating mock API servers quickly and without complexity. Available as a cross-platform desktop application (Electron-based) and a CLI (@mockoon/cli), it lets developers design complete mock API environments with realistic responses, dynamic templating, proxy forwarding, and CORS handling. Mockoon supports importing and exporting OpenAPI/Swagger specifications, making it easy to turn API documentation into working mock servers. How It Works Mockoon&#8217;s desktop app provides a visual interface for creating API routes with customizable HTTP methods, paths, status codes, headers, and response bodies. The response templating engine supports Handlebars-like helpers (Faker.js data generation, request body/query/header access, conditional logic, loops) to produce dynamic, realistic responses. Environments can be exported as JSON files and run headlessly via the CLI, making them suitable for CI/CD pipelines and automated testing. Key Features Zero-config mock servers: Create and run mock APIs in seconds with the desktop app CLI for CI/CD: Run mock environments headlessly via @mockoon/cli in Docker, GitHub Actions, and pipelines Dynamic response templating: Faker.js data, request interpolation, conditional responses, and loops Proxy mode: Forward unmatched requests to a real API while intercepting specific routes OpenAPI import/export: Import Swagger/OpenAPI specs to auto-generate mock routes Request logging: Inspect incoming requests and outgoing responses for debugging CORS handling: Automatic CORS preflight responses for frontend development Multiple environments: Run several mock servers on different ports simultaneously Response rules: Serve different responses based on request body, headers, query params, or cookies Agent Integration AI agents can leverage Mockoon for API testing workflows: generating mock servers from OpenAPI specs to test integrations without hitting production endpoints, running mock APIs in CI to validate client code against expected contracts, prototyping new API designs by defining routes and testing them locally, or using the proxy mode to intercept and modify specific API calls during debugging sessions. Installation npm install -g @mockoon/cli Desktop app available at mockoon.com/download . Docker: docker run -p 3000:3000 mockoon/cli:latest Quick Example mockoon-cli start --data ./environment.json --port 3000

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mockoon-mock-api-server-cli/)
