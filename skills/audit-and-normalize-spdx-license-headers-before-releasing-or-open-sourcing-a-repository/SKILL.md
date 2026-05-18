---
name: "Audit and normalize SPDX license headers before releasing or open-sourcing a repository"
slug: "audit-and-normalize-spdx-license-headers-before-releasing-or-open-sourcing-a-repository"
description: "Use REUSE when an agent needs file-level licensing clarity instead of guessing from a single top-level LICENSE file. The agent checks compliance, adds or verifies SPDX headers, pulls missing license texts into LICENSES/, and produces a concrete remediation list or SPDX export."
verification: "security_reviewed"
source: "https://codeberg.org/fsfe/reuse-tool"
author: "Free Software Foundation Europe e.V."
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
---

# Audit and normalize SPDX license headers before releasing or open-sourcing a repository

Use REUSE when an agent needs file-level licensing clarity instead of guessing from a single top-level LICENSE file. The agent checks compliance, adds or verifies SPDX headers, pulls missing license texts into LICENSES/, and produces a concrete remediation list or SPDX export.

## Prerequisites

Python 3.10+, optional libmagic, optional VCS tools

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
pipx install reuse, apt install reuse, or dnf install reuse
```

## Documentation

- https://reuse.readthedocs.io/en/stable/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-and-normalize-spdx-license-headers-before-releasing-or-open-sourcing-a-repository/)
