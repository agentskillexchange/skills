---
title: "Lint and validate Prometheus alerting rules before noisy or broken alerts reach production with Pint"
description: "Check Prometheus alerting and recording rules in CI or ad hoc runs so invalid, misleading, or dangerous rules are caught before deploy."
verification: "listed"
source: "https://github.com/cloudflare/pint"
author: "Cloudflare"
publisher_type: "organization"
category:
  - "errors"
  - "error_data"
framework:
  - "errors"
  - "error_data"
tool_ecosystem:
  github_repo: "cloudflare/pint"
  github_stars: 1015
---

# Lint and validate Prometheus alerting rules before noisy or broken alerts reach production with Pint

Check Prometheus alerting and recording rules in CI or ad hoc runs so invalid, misleading, or dangerous rules are caught before deploy.

## Prerequisites

Pint binary, Prometheus rule files, optional Prometheus API access

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install Pint from the release binaries, then run `pint lint` or `pint ci` against your Prometheus rule directories, optionally with a config that points at live Prometheus servers for deeper checks.
```

## Documentation

- https://cloudflare.github.io/pint/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lint-and-validate-prometheus-alerting-rules-before-noisy-or-broken-alerts-reach-production-with-pint/)
