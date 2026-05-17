---
name: "Load-test HTTP endpoints with reproducible attack profiles and latency reports before rollout with Vegeta"
slug: "load-test-http-endpoints-with-reproducible-attack-profiles-and-latency-reports-before-rollout-with-vegeta"
description: "Run constant-rate HTTP attacks, capture binary results, and generate reports or plots before capacity changes and releases."
github_stars: 25004
verification: "security_reviewed"
source: "https://github.com/tsenart/vegeta"
author: "tsenart"
publisher_type: "individual"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "tsenart/vegeta"
  github_stars: 25004
---

# Load-test HTTP endpoints with reproducible attack profiles and latency reports before rollout with Vegeta

Run constant-rate HTTP attacks, capture binary results, and generate reports or plots before capacity changes and releases.

## Prerequisites

Vegeta CLI and a targets file or piped HTTP target definitions

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install a prebuilt release binary or use a package manager such as Homebrew with `brew install vegeta`, then pipe targets into `vegeta attack` and pass the results to `vegeta report` or `vegeta plot`.
```

## Documentation

- https://github.com/tsenart/vegeta

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/load-test-http-endpoints-with-reproducible-attack-profiles-and-latency-reports-before-rollout-with-vegeta/)
