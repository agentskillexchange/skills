---
title: "Estimate Terraform and OpenTofu cost deltas before infrastructure changes merge with Infracost"
description: "Show projected cloud cost increases or savings from Terraform and OpenTofu plans before a PR merges."
verification: "listed"
source: "https://github.com/infracost/infracost"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "infracost/infracost"
  github_stars: 12267
---

# Estimate Terraform and OpenTofu cost deltas before infrastructure changes merge with Infracost

Use Infracost when an agent needs to answer a narrow pre-merge question: how much will this Terraform or OpenTofu change move projected cloud spend up or down. The agent can read plan output, run cost breakdowns and diffs, and turn the results into a review-ready summary before infrastructure changes merge. Invoke this instead of using the product normally when the job is pull request cost adjudication, not general IaC authoring or cloud billing. The boundary is cost-delta review for infrastructure plans before approval, not a generic Terraform tool or cloud cost platform.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/estimate-terraform-and-opentofu-cost-deltas-before-infrastructure-changes-merge-with-infracost/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/estimate-terraform-and-opentofu-cost-deltas-before-infrastructure-changes-merge-with-infracost
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/estimate-terraform-and-opentofu-cost-deltas-before-infrastructure-changes-merge-with-infracost`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/estimate-terraform-and-opentofu-cost-deltas-before-infrastructure-changes-merge-with-infracost/)
