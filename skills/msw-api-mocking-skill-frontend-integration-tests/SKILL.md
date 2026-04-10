---
name: MSW API Mocking Skill for Frontend and Integration Tests
description: Use this skill when an agent needs to stand up request handlers with
  Mock Service Worker, isolate network behavior in local development or tests, and
  keep mocks faithful to real endpoints. It is a task-focused mocking skill built
  around MSW, not a generic product card.
verification: security_reviewed
source: https://github.com/mswjs/msw
category:
- Code Quality &amp; Review
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: mswjs/msw
  github_stars: 17807
  ase_npm_package: msw
  npm_weekly_downloads: 12741702
---
# MSW API Mocking Skill for Frontend and Integration Tests

This skill teaches an agent how to use Mock Service Worker (MSW) to create realistic API mocks for browser development, component tests, and integration test suites. The agent’s job is not just “install MSW.” It identifies the network calls a feature depends on, creates focused request handlers, organizes mock data so it is easy to change, and wires the handlers into the project’s browser or test bootstrap. When a failing test depends on unstable external APIs, the agent can also replace brittle ad hoc stubs with consistent MSW handlers and explain which requests are now covered.
Invoke this skill when the user wants a feature developed against an API that is incomplete, rate-limited, expensive, flaky, or hard to reproduce locally. It is also the right fit when a repository already has tests but they rely on raw fetch mocks, repeated Jest spies, or framework-specific patching that makes behavior hard to reason about. In those situations the user needs a network-behavior skill, not a generic summary of the MSW project.
The scope boundary keeps this skill honest. It is not a listing for MSW as a library, and it is not a catch-all testing framework entry. The skill is specifically about defining handlers, matching routes, returning realistic mocked payloads, simulating success and failure paths, and keeping frontend or integration tests deterministic. Common integration points include Vitest, Jest, Playwright-backed app development, Storybook previews, and local feature branches that need predictable API responses.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/msw-api-mocking-skill-frontend-integration-tests/)
