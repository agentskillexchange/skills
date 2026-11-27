---
name: "Record and replay FrontMCP calls to catch server regressions"
slug: "record-and-replay-frontmcp-calls-to-catch-server-regressions"
description: "Capture baseline MCP calls as JSONL, replay them against a changed FrontMCP server, and review answer differences and new or resolved errors before accepting the build."
verification: "security_reviewed"
source: "https://github.com/agentfront/frontmcp/blob/a5810ef05dbdcc3878c6a6ae6e6a7bf436bab813/libs/skills/catalog/frontmcp-testing/references/replay-calls.md"
author: "AgentFront"
publisher_type: "organization"
category: "Code Quality & Review"
framework: "MCP"
---

# Record and replay FrontMCP calls to catch server regressions

Capture baseline MCP calls as JSONL, replay them against a changed FrontMCP server, and review answer differences and new or resolved errors before accepting the build.

## Prerequisites

Node.js 24+, npm, frontmcp CLI, @frontmcp/sdk, @frontmcp/testing, a FrontMCP TypeScript project and isolated test dependencies

## Installation

Install or set up from the source-backed instructions:

In an existing FrontMCP project, use Node.js 24+ and matching @frontmcp package versions. Install the testing skill with npx frontmcp skills install frontmcp-testing (add --provider codex for Codex). Read its references/replay-calls.md alongside the server project. Ensure frontmcp and @frontmcp/testing are available as project development dependencies, aligned with the SDK version. Enable CallRecorderPlugin for a controlled baseline, review the JSONL, then run npx frontmcp test --replay fixtures/calls.jsonl against the changed server.

- Source: https://github.com/agentfront/frontmcp/blob/a5810ef05dbdcc3878c6a6ae6e6a7bf436bab813/libs/skills/catalog/frontmcp-testing/references/replay-calls.md

## Documentation

- https://github.com/agentfront/frontmcp/blob/a5810ef05dbdcc3878c6a6ae6e6a7bf436bab813/libs/skills/catalog/frontmcp-testing/references/replay-calls.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/record-and-replay-frontmcp-calls-to-catch-server-regressions/)
