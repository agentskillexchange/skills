---
title: "REST API Test Suite Generator"
description: "Generates comprehensive API test suites from OpenAPI specs using Postman Collection SDK and Newman CLI. Creates parameterized test scenarios with environment-specific variables, auth flows, and assertion chains."
slug: "rest-api-test-suite-generator"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/rest-api-test-suite-generator/"
---

# REST API Test Suite Generator

Generates comprehensive API test suites from OpenAPI specs using Postman Collection SDK and Newman CLI. Creates parameterized test scenarios with environment-specific variables, auth flows, and assertion chains.

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
clawhub install rest-api-test-suite-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The REST API Test Suite Generator skill automates the creation of API test suites from OpenAPI specification files. It uses the Postman Collection SDK v4 to programmatically build collection items with request definitions, test scripts, and pre-request authentication flows.
The skill parses OpenAPI specs to generate test scenarios for each endpoint covering success cases, validation error responses, authentication failures, and edge cases. It creates Postman environments with variable substitution for base URLs, API keys, and OAuth tokens across development, staging, and production configurations.
Advanced features include dynamic test chaining where response values from one request populate subsequent request parameters using pm.environment.set, contract testing assertions that validate response schemas against OpenAPI definitions using tv4 or ajv validators, performance benchmarking with pm.response.responseTime assertions, and CI integration scripts using Newman CLI with JUnit and HTML reporters. The skill also generates mock server configurations using Prism for offline testing.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rest-api-test-suite-generator/)
