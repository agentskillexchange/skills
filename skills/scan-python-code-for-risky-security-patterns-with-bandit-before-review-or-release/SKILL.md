---
title: "Scan Python code for risky security patterns with Bandit before review or release"
description: "Catch insecure Python calls, weak crypto usage, shell injection risks, and similar patterns before merge or release."
verification: "listed"
source: "https://github.com/PyCQA/bandit"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "PyCQA/bandit"
  github_stars: 7933
---

# Scan Python code for risky security patterns with Bandit before review or release

Use Bandit when an agent needs a Python-specific security review pass before code review, release, or audit. The agent can scan a repository, flag risky APIs and insecure patterns, and return a finding list that is easy for a developer or reviewer to triage. Invoke this instead of using the product normally when the job is static security review of Python code, not broad multi-language SAST or dependency scanning. The boundary is Python code-pattern security analysis before approval, not a generic security platform listing.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/scan-python-code-for-risky-security-patterns-with-bandit-before-review-or-release/)
