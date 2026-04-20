---
title: Verify a freshly provisioned server or container matches expected services,
  ports, and files
description: Uses Goss to express the expected state of a machine or container, then
  validates that reality still matches the contract. Reach for it after provisioning,
  image builds, or config changes when an agent needs a fast pass or fail answer about
  service health and system drift.
verification: security_reviewed
source: https://github.com/goss-org/goss
category:
- Runbooks &amp; Diagnostics
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: goss-org/goss
  github_stars: 5877
---

# Verify a freshly provisioned server or container matches expected services, ports, and files

Uses Goss to express the expected state of a machine or container, then validates that reality still matches the contract. Reach for it after provisioning, image builds, or config changes when an agent needs a fast pass or fail answer about service health and system drift.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-freshly-provisioned-server-or-container-matches-expected-services-ports-and-files/)
