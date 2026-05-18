---
name: "Verify a freshly provisioned server or container matches expected services, ports, and files"
slug: "verify-freshly-provisioned-server-or-container-matches-expected-services-ports-and-files"
description: "Uses Goss to express the expected state of a machine or container, then validates that reality still matches the contract. Reach for it after provisioning, image builds, or config changes when an agent needs a fast pass or fail answer about service health and system drift."
github_stars: 5877
verification: "security_reviewed"
source: "https://github.com/goss-org/goss"
author: "goss-org"
publisher_type: "Open Source Project"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "goss-org/goss"
  github_stars: 5877
---

# Verify a freshly provisioned server or container matches expected services, ports, and files

Uses Goss to express the expected state of a machine or container, then validates that reality still matches the contract. Reach for it after provisioning, image builds, or config changes when an agent needs a fast pass or fail answer about service health and system drift.

## Prerequisites

Goss binary, shell access to the target system, and appropriate permissions to inspect the resources under test

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
curl -L https://github.com/goss-org/goss/releases/latest/download/goss-linux-amd64 -o /usr/local/bin/goss && chmod +rx /usr/local/bin/goss
```

## Documentation

- https://goss.readthedocs.io/en/stable/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-freshly-provisioned-server-or-container-matches-expected-services-ports-and-files/)
