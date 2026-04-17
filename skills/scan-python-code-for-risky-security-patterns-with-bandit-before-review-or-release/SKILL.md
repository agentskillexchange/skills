---
title: "Scan Python code for risky security patterns with Bandit before review or release"
description: "Use Bandit when an agent needs a Python-specific security review pass before code review, release, or audit. The agent can scan a repository, flag risky APIs and insecure patterns, and return a finding list that is easy for a developer or reviewer to triage. Invoke this instead of using the product normally when the job is static security review of Python code, not broad multi-language SAST or dependency scanning. The boundary is Python code-pattern security analysis before approval, not a generic security platform listing."
verification: listed
source: "https://github.com/PyCQA/bandit"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "PyCQA/bandit"
  github_stars: 7933
---

# Scan Python code for risky security patterns with Bandit before review or release

Use Bandit when an agent needs a Python-specific security review pass before code review, release, or audit. The agent can scan a repository, flag risky APIs and insecure patterns, and return a finding list that is easy for a developer or reviewer to triage. Invoke this instead of using the product normally when the job is static security review of Python code, not broad multi-language SAST or dependency scanning. The boundary is Python code-pattern security analysis before approval, not a generic security platform listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/scan-python-code-for-risky-security-patterns-with-bandit-before-review-or-release
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/scan-python-code-for-risky-security-patterns-with-bandit-before-review-or-release` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-python-code-for-risky-security-patterns-with-bandit-before-review-or-release/)
