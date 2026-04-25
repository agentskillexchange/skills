---
title: "Record and replay HTTP fixtures for deterministic Python tests with VCR.py"
description: "Use VCR.py when an agent needs to turn flaky, slow, or rate-limited Python tests into stable runs by recording real HTTP interactions once and replaying them from cassette files. The agent decides which requests belong in fixtures, refreshes stale cassettes when upstream APIs change, and keeps external traffic out of the repeat test loop."
verification: "security_reviewed"
source: "https://github.com/kevin1024/vcrpy"
category:
  - "Developer Tools"
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

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py/)
