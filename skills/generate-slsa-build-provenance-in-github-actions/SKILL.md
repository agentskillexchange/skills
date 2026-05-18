---
name: "Generate SLSA build provenance in GitHub Actions"
slug: "generate-slsa-build-provenance-in-github-actions"
description: "Attach signed SLSA provenance to GitHub Actions builds so release artifacts ship with verifiable supply-chain metadata."
github_stars: 566
verification: "security_reviewed"
source: "https://github.com/slsa-framework/slsa-github-generator"
author: "SLSA maintainers"
publisher_type: "organization"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "slsa-framework/slsa-github-generator"
  github_stars: 566
---

# Generate SLSA build provenance in GitHub Actions

Attach signed SLSA provenance to GitHub Actions builds so release artifacts ship with verifiable supply-chain metadata.

## Prerequisites

GitHub Actions, SLSA GitHub Generator

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Follow the repository setup for the relevant generator, add the recommended GitHub Actions workflow, then build artifacts and inspect the generated provenance attestation.
```

## Documentation

- https://github.com/slsa-framework/slsa-github-generator

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-slsa-build-provenance-in-github-actions/)
