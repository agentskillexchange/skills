---
name: Record and replay HTTP fixtures for deterministic Python tests with VCR.py
description: Use VCR.py when an agent needs to turn flaky, slow, or rate-limited Python
  tests into stable runs by recording real HTTP interactions once and replaying them
  from cassette files. The agent decides which requests belong in fixtures, refreshes
  stale cassettes when upstream APIs change, and keeps external traffic out of the
  repeat test loop.
category: Developer Tools
framework: Multi-Framework
verification: security_reviewed
source: https://github.com/kevin1024/vcrpy
tool_ecosystem:
  github_repo: kevin1024/vcrpy
  github_stars: 2956
  tool: vcrpy
---
# Record and replay HTTP fixtures for deterministic Python tests with VCR.py
Use VCR.py when an agent needs to turn flaky, slow, or rate-limited Python tests into stable runs by recording real HTTP interactions once and replaying them from cassette files. The agent decides which requests belong in fixtures, refreshes stale cassettes when upstream APIs change, and keeps external traffic out of the repeat test loop.

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
