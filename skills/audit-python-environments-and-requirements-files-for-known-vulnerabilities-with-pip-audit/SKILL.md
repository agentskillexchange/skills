---
title: "Audit Python environments and requirements files for known vulnerabilities with pip-audit"
description: "Check Python environments and requirements files for published vulnerabilities before shipping, upgrading, or approving dependency changes."
verification: "security_reviewed"
source: "https://github.com/pypa/pip-audit"
author: "PyPA"
publisher_type: "organization"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "pypa/pip-audit"
  github_stars: 1260
---

# Audit Python environments and requirements files for known vulnerabilities with pip-audit

Check Python environments and requirements files for published vulnerabilities before shipping, upgrading, or approving dependency changes.

## Prerequisites

Python 3.9+, pip, pip-audit

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install with `pip install pip-audit`, then run `pip-audit` in the target environment or `pip-audit -r requirements.txt` for a pinned dependency file.
```

## Documentation

- https://pypa.github.io/pip-audit/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-python-environments-and-requirements-files-for-known-vulnerabilities-with-pip-audit/)
