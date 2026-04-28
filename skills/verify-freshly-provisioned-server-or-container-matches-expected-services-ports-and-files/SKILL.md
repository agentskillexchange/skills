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
- Runbooks & Diagnostics
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: goss-org/goss
  github_stars: 5877
---

# Verify a freshly provisioned server or container matches expected services, ports, and files

Uses Goss to express the expected state of a machine or container, then validates that reality still matches the contract. Reach for it after provisioning, image builds, or config changes when an agent needs a fast pass or fail answer about service health and system drift.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/verify-freshly-provisioned-server-or-container-matches-expected-services-ports-and-files/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/verify-freshly-provisioned-server-or-container-matches-expected-services-ports-and-files
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/verify-freshly-provisioned-server-or-container-matches-expected-services-ports-and-files`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-freshly-provisioned-server-or-container-matches-expected-services-ports-and-files/)
