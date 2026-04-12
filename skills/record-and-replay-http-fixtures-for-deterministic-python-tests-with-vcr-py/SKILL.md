---
title: "Record and replay HTTP fixtures for deterministic Python tests with VCR.py"
description: "Use VCR.py when an agent needs to turn flaky, slow, or rate-limited Python tests into stable runs by recording real HTTP interactions once and replaying them from cassette files. The agent decides which requests belong in fixtures, refreshes stale cassettes when upstream APIs change, and keeps external traffic out of the repeat test loop."
verification: security_reviewed
source: "https://github.com/kevin1024/vcrpy"
---

# Record and replay HTTP fixtures for deterministic Python tests with VCR.py

Use VCR.py when an agent needs to turn flaky, slow, or rate-limited Python tests into stable runs by recording real HTTP interactions once and replaying them from cassette files. The agent decides which requests belong in fixtures, refreshes stale cassettes when upstream APIs change, and keeps external traffic out of the repeat test loop.

## Installation

Choose the path that fits your setup:

1. Clone this repository and use the skill locally.
2. Copy the skill folder into your local skills directory.
3. Add the skill as a Git submodule in your skills workspace.
4. Vendor the files into an internal skill catalog for your team.
5. Reference the upstream source and recreate the skill in your own agent environment.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/record-and-replay-http-fixtures-for-deterministic-python-tests-with-vcr-py/)
