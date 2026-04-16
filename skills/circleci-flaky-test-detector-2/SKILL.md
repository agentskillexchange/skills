---
title: "CircleCI Flaky Test Detector"
description: "Queries CircleCI Insights API to identify test cases that flip between pass and fail across recent runs. Produces a ranked list by failure rate with quarantine strategies for Jest, pytest, RSpec, and JUnit."
verification: "security_reviewed"
source: "https://github.com/circleci/circleci-docs"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "circleci/circleci-docs"
  github_stars: 843
---

# CircleCI Flaky Test Detector

CircleCI Flaky Test Detector is built around CircleCI continuous integration platform. The underlying ecosystem is represented by circleci/circleci-docs (842+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like CircleCI API v2, Insights API, workflows, jobs, test metadata, artifacts and preserving the operational context that matters for real tasks.

For testing and review work, the skill wraps the normal circleci commands into a repeatable analysis loop that can produce summaries, prioritized findings, and CI-friendly output instead of a wall of raw logs. The original use case is clear: Queries CircleCI Insights API to identify test cases that flip between pass and fail across recent runs. Produces a ranked list by failure rate with quarantine strategies for Jest, pytest, RSpec, and JUnit. The implementation typically relies on CircleCI API v2, Insights API, workflows, jobs, test metadata, artifacts, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses CircleCI API v2, Insights API, workflows, jobs, test metadata, artifacts instead of scraping a UI, which makes runs easier to audit and retry.

Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

Fits into broader integration points such as CI diagnostics, flaky test analysis, pipeline automation, and deployment gates.

Key integration points include CI diagnostics, flaky test analysis, pipeline automation, and deployment gates. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-flaky-test-detector-2/)
