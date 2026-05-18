---
name: "Execute DevOps delivery and infrastructure workflows with cc-devops-skills"
slug: "execute-devops-delivery-and-infrastructure-workflows-with-cc-devops-skills"
description: "Use generator and validator loops for infra, CI, and platform work so agents ship operational changes with more checks and less improvisation."
github_stars: 182
verification: "listed"
source: "https://github.com/akin-ozer/cc-devops-skills"
author: "Akin Ozer"
publisher_type: "individual"
category: "CI/CD Integrations"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "akin-ozer/cc-devops-skills"
  github_stars: 182
---

# Execute DevOps delivery and infrastructure workflows with cc-devops-skills

Use generator and validator loops for infra, CI, and platform work so agents ship operational changes with more checks and less improvisation.

## Prerequisites

Claude Code or Codex with skills or plugin support, the repository skill pack, and any DevOps tools required by the chosen skill such as Terraform, Kubernetes, linters, security scanners, or GitHub Actions.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/akin-ozer/cc-devops-skills.git ~/.codex/devops-skills
- brew install terraform tflint terragrunt helm kubeconform kubectl hadolint
- brew install actionlint act shellcheck prometheus yq fluent-bit
- pipx install ansible ansible-lint checkov yamllint molecule

Requirements and caveats from upstream:
- **Local-first validation pipelines**: many validator skills run shell/Python checks directly from their scripts/ folders.
- | Docker | hadolint |

Basic usage or getting-started notes:
- **14 validators** for linting, security checks, and dry-run validation
- To run as pure passthrough (no auto-injection):
- B --> C["Run matching validator"]

- Source: https://github.com/akin-ozer/cc-devops-skills
- Extracted from upstream docs: https://raw.githubusercontent.com/akin-ozer/cc-devops-skills/HEAD/README.md

## Documentation

- https://github.com/akin-ozer/cc-devops-skills#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/execute-devops-delivery-and-infrastructure-workflows-with-cc-devops-skills/)
