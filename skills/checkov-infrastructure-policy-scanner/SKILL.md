---
name: "Checkov Infrastructure Policy Scanner"
slug: "checkov-infrastructure-policy-scanner"
description: "Scans IaC files with Bridgecrew Checkov for policy violations across Terraform, CloudFormation, Kubernetes, and Dockerfile configurations. Supports custom Python-based policy authoring and Prisma Cloud integration."
github_stars: 8646
verification: "security_reviewed"
source: "https://github.com/bridgecrewio/checkov"
author: "Bridgecrew"
category: "Security & Verification"
framework: "Codex"
tool_ecosystem:
  github_repo: "bridgecrewio/checkov"
  github_stars: 8646
---

# Checkov Infrastructure Policy Scanner

Scans IaC files with Bridgecrew Checkov for policy violations across Terraform, CloudFormation, Kubernetes, and Dockerfile configurations. Supports custom Python-based policy authoring and Prisma Cloud integration.

## Installation

Use the upstream install or setup path that matches your environment:
- To install pip follow the official [docs](https://pip.pypa.io/en/stable/cli/pip_install/)
- pip install checkov
- brew install checkov
- brew upgrade checkov

Requirements and caveats from upstream:
- [![Python Version](https://img.shields.io/pypi/pyversions/checkov)](#)
- [![Docker Pulls](https://img.shields.io/docker/pulls/bridgecrew/checkov.svg)](https://hub.docker.com/r/bridgecrew/checkov)
- Supports Python format for attribute policies and YAML format for both attribute and composite policies.

Basic usage or getting-started notes:
- [Getting Started](#getting-started)
- Terraform >= 0.12
- sh

- Source: https://github.com/bridgecrewio/checkov
- Extracted from upstream docs: https://raw.githubusercontent.com/bridgecrewio/checkov/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/checkov-infrastructure-policy-scanner/)
