---
title: "Record and replay HTTP fixtures for deterministic Python tests with VCR.py"
description: "This ASE entry is built around VCR.py, the Python library that records HTTP interactions and replays them from cassette files during later test runs. The agent job-to-be-done is precise: capture a real API exchange once, save the request and response pair as test fixture data, and then rerun the same workflow without reaching the live network unless the cassette is intentionally refreshed. You use this skill when invoking the product normally is the wrong abstraction. The point is not “install a library” or “mock HTTP somehow.” The point is to stabilize a Python test suite, reproduce third-party integrations offline, and make API-heavy tests fast enough for agent-driven edit, verify, and refactor loops. An agent can identify flaky tests that depend on Stripe, GitHub, Slack, or internal HTTP services, wrap them in VCR.py cassettes, scrub sensitive headers, rerun the suite deterministically, and regenerate fixtures only when the upstream contract changes. That is a bounded workflow, not a generic SDK listing. The scope boundary is clear. This entry does not try to cover general API simulation platforms, service virtualization, or non-Python mocking stacks. It is specifically about cassette-based recording and replay for Python HTTP tests. Integration points include pytest suites, unittest-based projects, requests/httpx/urllib client calls, CI jobs, and fixture review workflows in version control. Upstream evidence is solid: official GitHub repository, PyPI package, MIT license, documentation on Read the Docs, releases, and active maintenance."
source: "https://github.com/kevin1024/vcrpy"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "kevin1024/vcrpy"
  github_stars: 2956
---

# Record and replay HTTP fixtures for deterministic Python tests with VCR.py

This ASE entry is built around VCR.py, the Python library that records HTTP interactions and replays them from cassette files during later test runs. The agent job-to-be-done is precise: capture a real API exchange once, save the request and response pair as test fixture data, and then rerun the same workflow without reaching the live network unless the cassette is intentionally refreshed. You use this skill when invoking the product normally is the wrong abstraction. The point is not “install a library” or “mock HTTP somehow.” The point is to stabilize a Python test suite, reproduce third-party integrations offline, and make API-heavy tests fast enough for agent-driven edit, verify, and refactor loops. An agent can identify flaky tests that depend on Stripe, GitHub, Slack, or internal HTTP services, wrap them in VCR.py cassettes, scrub sensitive headers, rerun the suite deterministically, and regenerate fixtures only when the upstream contract changes. That is a bounded workflow, not a generic SDK listing. The scope boundary is clear. This entry does not try to cover general API simulation platforms, service virtualization, or non-Python mocking stacks. It is specifically about cassette-based recording and replay for Python HTTP tests. Integration points include pytest suites, unittest-based projects, requests/httpx/urllib client calls, CI jobs, and fixture review workflows in version control. Upstream evidence is solid: official GitHub repository, PyPI package, MIT license, documentation on Read the Docs, releases, and active maintenance.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py/)
