---
title: "Generate dependency update pull requests from code with dependabot-core"
description: "Scan manifests, compute safe version bumps, and prepare dependency update PR material when you need self-hosted or custom Dependabot flows outside the default GitHub service."
verification: "listed"
source: "https://github.com/dependabot/dependabot-core"
author: "GitHub"
publisher_type: "organization"
category:
  - "CI/CD Integrations"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "dependabot/dependabot-core"
  github_stars: 5549
---

# Generate dependency update pull requests from code with dependabot-core

Scan manifests, compute safe version bumps, and prepare dependency update PR material when you need self-hosted or custom Dependabot flows outside the default GitHub service.

## Prerequisites

Ruby/Bundler and the dependabot-core runtime or supported CLI entrypoint, plus access to the target repository manifests and lockfiles

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Follow the upstream dependabot-core development or CLI setup instructions, configure the supported ecosystem and repository access, then run the documented update job or entrypoint to generate dependency diffs or PR-ready update outputs.
```

## Documentation

- https://github.com/dependabot/dependabot-core

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-dependency-update-pull-requests-from-code-with-dependabot-core/)
