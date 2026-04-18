---
title: "OpenTofu Open Source Infrastructure as Code Tool"
description: "OpenTofu is an open-source infrastructure as code tool that lets you declaratively manage cloud and on-premises resources. A CNCF project and community-driven fork of Terraform, it provides execution plans, resource graphs, and change automation for safe infrastructure provisioning."
verification: security_reviewed
source: "https://github.com/opentofu/opentofu"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "opentofu/opentofu"
  github_stars: 28244
---

# OpenTofu Open Source Infrastructure as Code Tool

OpenTofu is an open-source infrastructure as code (IaC) tool maintained by the Cloud Native Computing Foundation (CNCF). It enables teams to define, provision, and manage infrastructure using a high-level configuration language (HCL), treating infrastructure definitions as versionable, reusable, and shareable code.

The tool generates execution plans before making changes, showing exactly what will be created, modified, or destroyed. This plan-and-apply workflow prevents surprises and allows teams to review infrastructure changes before they take effect. OpenTofu builds a dependency graph of all resources and parallelizes operations on independent resources for efficient provisioning.

OpenTofu supports hundreds of infrastructure providers including AWS, Azure, Google Cloud, DigitalOcean, Cloudflare, and many others through its provider ecosystem. Modules allow infrastructure patterns to be packaged and reused across projects. State management tracks the mapping between configuration and real-world resources.

The project maintains compatibility with existing Terraform configurations and state files, providing a migration path for teams. OpenTofu adds features independently, including state encryption, provider-defined functions, and improved module testing capabilities.

Installation is available through package managers, pre-built binaries for all major platforms, and Docker images. The project provides nightly builds for testing the latest changes. As a CNCF project, OpenTofu benefits from vendor-neutral governance and a growing community of contributors. The tool is licensed under MPL-2.0 and holds an OpenSSF Best Practices badge.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/opentofu-open-source-infrastructure-as-code
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/opentofu-open-source-infrastructure-as-code` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/opentofu-open-source-infrastructure-as-code/)
