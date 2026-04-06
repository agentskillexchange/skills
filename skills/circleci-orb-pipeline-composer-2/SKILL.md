---
name: CircleCI Orb Pipeline Composer
description: Composes multi-stage CircleCI pipelines using reusable Orbs and the CircleCI
  v2 API. Supports dynamic config generation with setup workflows and pipeline parameters
  for monorepo deployments.
category: CI/CD Integrations
framework: Claude Code
verification: security_reviewed
source: "https://agentskillexchange.com/skills/circleci-orb-pipeline-composer-2/"
---
# CircleCI Orb Pipeline Composer

Composes multi-stage CircleCI pipelines using reusable Orbs and the CircleCI v2 API. Supports dynamic config generation with setup workflows and pipeline parameters for monorepo deployments.

The CircleCI Orb Pipeline Composer skill generates optimized CircleCI pipeline configurations by leveraging the CircleCI v2 API and the Orb registry. It creates multi-stage workflows that compose reusable Orbs for common tasks like Docker image building (circleci/docker), AWS deployments (circleci/aws-cli), and Kubernetes rollouts (circleci/kubernetes). The skill supports dynamic configuration through setup workflows, enabling monorepo projects to selectively trigger downstream pipelines based on changed paths using the path-filtering orb. It configures pipeline parameters for environment-specific builds, implements workspace persistence between jobs, and sets up approval gates for production deployments. The composer validates configurations against the CircleCI config schema, checks Orb version compatibility, and generates pipeline parameter maps for API-triggered runs via the CircleCI Pipeline Trigger API endpoint.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-pipeline-composer-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-pipeline-composer-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-pipeline-composer-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill circleci-orb-pipeline-composer-2 -a codex
```

### OpenClaw

```bash
clawhub install circleci-orb-pipeline-composer-2
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/circleci-orb-pipeline-composer-2/)
