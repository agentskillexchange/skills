---
name: "REST API Test Suite Generator"
description: "Generates comprehensive API test suites from OpenAPI specs using Postman Collection SDK and Newman CLI. Creates parameterized test scenarios with environment-specific variables, auth flows, and assertion chains."
category: "Library & API Reference"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/rest-api-test-suite-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "postman"  # from ase_tool_match
  github_stars: 5996  # from ase_github_stars (integer, not string)
  github_repo: "postmanlabs/postman-app-support"  # from ase_github_repo
  license: "Unknown"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# REST API Test Suite Generator

Generates comprehensive API test suites from OpenAPI specs using Postman Collection SDK and Newman CLI. Creates parameterized test scenarios with environment-specific variables, auth flows, and assertion chains.

## Overview

The REST API Test Suite Generator skill automates the creation of API test suites from OpenAPI specification files. It uses the Postman Collection SDK v4 to programmatically build collection items with request definitions, test scripts, and pre-request authentication flows.

The skill parses OpenAPI specs to generate test scenarios for each endpoint covering success cases, validation error responses, authentication failures, and edge cases. It creates Postman environments with variable substitution for base URLs, API keys, and OAuth tokens across development, staging, and production configurations.

Advanced features include dynamic test chaining where response values from one request populate subsequent request parameters using pm.environment.set, contract testing assertions that validate response schemas against OpenAPI definitions using tv4 or ajv validators, performance benchmarking with pm.response.responseTime assertions, and CI integration scripts using Newman CLI with JUnit and HTML reporters. The skill also generates mock server configurations using Prism for offline testing.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill rest-api-test-suite-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill rest-api-test-suite-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill rest-api-test-suite-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill rest-api-test-suite-generator -a codex
```

### OpenClaw

```bash
clawhub install rest-api-test-suite-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/rest-api-test-suite-generator/
