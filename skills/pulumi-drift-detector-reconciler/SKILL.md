---
name: "Pulumi Drift Detector & Reconciler"
slug: "pulumi-drift-detector-reconciler"
description: "Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up --target for specific resources."
github_stars: 25042
verification: "security_reviewed"
source: "https://github.com/pulumi/pulumi"
category: "Runbooks & Diagnostics"
framework: "Codex"
tool_ecosystem:
  github_repo: "pulumi/pulumi"
  github_stars: 25042
  npm_package: "@pulumi/pulumi"
  npm_weekly_downloads: 2073384
---

# Pulumi Drift Detector & Reconciler

Runs pulumi refresh on schedule to detect drift between live cloud resources and Pulumi state. Classifies drift by severity and opens a Jira ticket for destructive changes. Non-destructive drift is auto-reconciled via pulumi up --target for specific resources.

## Installation

Requirements and caveats from upstream:
- [![Python version](https://badge.fury.io/py/pulumi.svg)](https://pypi.org/project/pulumi)
- const aws = require("@pulumi/aws");
- nohup python -m SimpleHTTPServer 80 &,

Basic usage or getting-started notes:
- For example, create three web servers:
- ## <a name="getting-started"></a>Getting Started
- To install the latest Pulumi release, run the following (see full

- Source: https://github.com/pulumi/pulumi
- Extracted from upstream docs: https://raw.githubusercontent.com/pulumi/pulumi/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pulumi-drift-detector-reconciler/)
