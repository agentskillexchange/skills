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

Use the upstream install or setup path that matches your environment:
- pipx :
- pipx run reuse lint
- pipx automatically isolates reuse into its own Python virtualenv, which means
- pipx install reuse

Requirements and caveats from upstream:
- This website requires JavaScript.
- python
- Python

Basic usage or getting-started notes:
- Lint 3rd party repositories / third-party-lint (https://github.com/fsfe/reuse-example) (push) Successful in 31s
- Maintainers
- Contributing

- Source: https://codeberg.org/fsfe/reuse-tool

## Documentation

- https://reuse.readthedocs.io/en/stable/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-and-normalize-spdx-license-headers-before-releasing-or-open-sourcing-a-repository/)
