---
title: "Terraform Module Registry Browser"
description: "Searches and evaluates Terraform modules from the HashiCorp Registry API and private registries. Uses hcl2json parser to analyze module input variables, outputs, and provider requirements."
slug: "terraform-module-registry-browser"
category:
  - "Templates &amp; Workflows"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/terraform-module-registry-browser/"
listed: true
---

# Terraform Module Registry Browser

Searches and evaluates Terraform modules from the HashiCorp Registry API and private registries. Uses hcl2json parser to analyze module input variables, outputs, and provider requirements.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install terraform-module-registry-browser
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Terraform Module Registry Browser provides intelligent search and evaluation of Terraform modules from the official HashiCorp Registry API (registry.terraform.io) and private module registries. It uses the Registry API v1 to fetch module metadata, version history, provider dependencies, and submodule structures. The hcl2json parser extracts input variables with types, defaults, and validation rules from module source code. The skill evaluates modules on maintenance signals: last publish date, open issues count, download trends, and provider version compatibility. It generates comparison tables when multiple modules serve the same purpose (e.g., AWS VPC modules from different publishers). Provider requirement analysis ensures module compatibility with your locked provider versions. The skill also generates example usage blocks with properly typed variable assignments and recommends complementary modules for common infrastructure patterns like VPC + EKS + RDS stacks.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/terraform-module-registry-browser/)
