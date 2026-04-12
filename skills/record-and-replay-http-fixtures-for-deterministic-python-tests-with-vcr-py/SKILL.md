---
title: "Record and replay HTTP fixtures for deterministic Python tests with VCR.py"
slug: "record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py"
verification: "security_reviewed"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
source: "https://github.com/kevin1024/vcrpy"
---

# Record and replay HTTP fixtures for deterministic Python tests with VCR.py

Use VCR.py when an agent needs to turn flaky, slow, or rate-limited Python tests into stable runs by recording real HTTP interactions once and replaying them from cassette files. The agent decides which requests belong in fixtures, refreshes stale cassettes when upstream APIs change, and keeps external traffic out of the repeat test loop.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py/)
