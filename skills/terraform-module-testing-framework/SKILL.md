---
name: "Terraform Module Testing Framework"
description: "Tests Terraform modules using Terratest Go library and terraform test native framework. Validates plan output, applies infrastructure in ephemeral environments, and asserts resource attributes with automatic cleanup."
category: "Templates & Workflows"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/terraform-module-testing-framework/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "terraform"  # from ase_tool_match
  github_stars: 47996  # from ase_github_stars (integer, not string)
  github_repo: "hashicorp/terraform"  # from ase_github_repo
  license: "NOASSERTION"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Terraform Module Testing Framework

Tests Terraform modules using Terratest Go library and terraform test native framework. Validates plan output, applies infrastructure in ephemeral environments, and asserts resource attributes with automatic cleanup.

## Overview

The Terraform Module Testing Framework skill implements comprehensive testing strategies for Terraform infrastructure modules using both the Terratest Go testing library and the native terraform test framework introduced in Terraform 1.6. Unit tests validate module logic by examining terraform plan JSON output for expected resource configurations, attribute values, and dependency relationships without provisioning real infrastructure. Integration tests use Terratest to apply modules in ephemeral cloud environments, verify deployed resource properties through provider APIs, and automatically destroy resources after assertions complete. The skill manages test fixtures with varying input variable combinations to exercise conditional logic branches within modules. Parallel test execution with unique resource naming prevents conflicts between concurrent test runs. Contract tests validate that module outputs conform to expected schemas for consumption by downstream modules. The skill integrates with GitHub Actions and GitLab CI to run tests on pull requests, caching provider plugins and state files for faster execution cycles.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill terraform-module-testing-framework
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill terraform-module-testing-framework -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill terraform-module-testing-framework -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill terraform-module-testing-framework -a codex
```

### OpenClaw

```bash
clawhub install terraform-module-testing-framework
```

## Source

- Marketplace: https://agentskillexchange.com/skills/terraform-module-testing-framework/
