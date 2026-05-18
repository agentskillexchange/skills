---
name: "Verify a freshly provisioned server or container matches expected services, ports, and files"
slug: "verify-freshly-provisioned-server-or-container-matches-expected-services-ports-and-files"
description: "Uses Goss to express the expected state of a machine or container, then validates that reality still matches the contract. Reach for it after provisioning, image builds, or config changes when an agent needs a fast pass or fail answer about service health and system drift."
github_stars: 5877
verification: "listed"
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

Use the upstream install or setup path that matches your environment:
- make build

Requirements and caveats from upstream:
- and Docker Compose [dcgoss](https://github.com/goss-org/goss/tree/master/extras/dcgoss).
- **Note:** For some Docker/Kubernetes healthcheck, health endpoint, and
- # (optional) dgoss docker wrapper (use 'master' for latest version)

Basic usage or getting-started notes:
- **Note:** For macOS and Windows, see: [platform-feature-parity].
- This will install goss and [dgoss](https://github.com/goss-org/goss/tree/master/extras/dgoss).
- bash

- Source: https://github.com/goss-org/goss
- Extracted from upstream docs: https://raw.githubusercontent.com/goss-org/goss/HEAD/README.md

## Documentation

- https://goss.readthedocs.io/en/stable/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-freshly-provisioned-server-or-container-matches-expected-services-ports-and-files/)
