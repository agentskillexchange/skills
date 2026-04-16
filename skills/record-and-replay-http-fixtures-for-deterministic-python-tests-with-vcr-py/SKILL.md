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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py/)
