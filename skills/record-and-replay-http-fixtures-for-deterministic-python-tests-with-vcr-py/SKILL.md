---
title: "Record and replay HTTP fixtures for deterministic Python tests with VCR.py"
description: "This ASE entry is built around VCR.py, the Python library that records HTTP interactions and replays them from cassette files during later test runs. The agent job-to-be-done is precise: capture a real API exchange once, save the request and response pair as test fixture data, and then rerun the same workflow without reaching the live network unless the cassette is intentionally refreshed.\nYou use this skill when invoking the product normally is the wrong abstraction. The point is not “install a library” or “mock HTTP somehow.” The point is to stabilize a Python test suite, reproduce third-party integrations offline, and make API-heavy tests fast enough for agent-driven edit, verify, and refactor loops. An agent can identify flaky tests that depend on Stripe, GitHub, Slack, or internal HTTP services, wrap them in VCR.py cassettes, scrub sensitive headers, rerun the suite deterministically, and regenerate fixtures only when the upstream contract changes. That is a bounded workflow, not a generic SDK listing.\nThe scope boundary is clear. This entry does not try to cover general API simulation platforms, service virtualization, or non-Python mocking stacks. It is specifically about cassette-based recording and replay for Python HTTP tests. Integration points include pytest suites, unittest-based projects, requests/httpx/urllib client calls, CI jobs, and fixture review workflows in version control. Upstream evidence is solid: official GitHub repository, PyPI package, MIT license, documentation on Read the Docs, releases, and active maintenance."
verification: security_reviewed
source: "https://github.com/kevin1024/vcrpy"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "kevin1024/vcrpy"
  github_stars: 2956
---

# Record and replay HTTP fixtures for deterministic Python tests with VCR.py

This ASE entry is built around VCR.py, the Python library that records HTTP interactions and replays them from cassette files during later test runs. The agent job-to-be-done is precise: capture a real API exchange once, save the request and response pair as test fixture data, and then rerun the same workflow without reaching the live network unless the cassette is intentionally refreshed.
You use this skill when invoking the product normally is the wrong abstraction. The point is not “install a library” or “mock HTTP somehow.” The point is to stabilize a Python test suite, reproduce third-party integrations offline, and make API-heavy tests fast enough for agent-driven edit, verify, and refactor loops. An agent can identify flaky tests that depend on Stripe, GitHub, Slack, or internal HTTP services, wrap them in VCR.py cassettes, scrub sensitive headers, rerun the suite deterministically, and regenerate fixtures only when the upstream contract changes. That is a bounded workflow, not a generic SDK listing.
The scope boundary is clear. This entry does not try to cover general API simulation platforms, service virtualization, or non-Python mocking stacks. It is specifically about cassette-based recording and replay for Python HTTP tests. Integration points include pytest suites, unittest-based projects, requests/httpx/urllib client calls, CI jobs, and fixture review workflows in version control. Upstream evidence is solid: official GitHub repository, PyPI package, MIT license, documentation on Read the Docs, releases, and active maintenance.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py/)
