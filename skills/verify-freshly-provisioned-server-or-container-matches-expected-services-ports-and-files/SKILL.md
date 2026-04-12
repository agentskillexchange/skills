---
title: "Verify a freshly provisioned server or container matches expected services, ports, and files"
slug: "verify-freshly-provisioned-server-or-container-matches-expected-services-ports-and-files"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
source: "https://github.com/goss-org/goss"
tool_ecosystem:
  github_repo: "goss-org/goss"
  github_stars: 5878
---

# Verify a freshly provisioned server or container matches expected services, ports, and files

Uses Goss to express the expected state of a machine or container, then validates that reality still matches the contract. Reach for it after provisioning, image builds, or config changes when an agent needs a fast pass or fail answer about service health and system drift.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-freshly-provisioned-server-or-container-matches-expected-services-ports-and-files/)
