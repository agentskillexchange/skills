---
name: "AWS CodePipeline Orchestrator"
description: "Manages AWS CodePipeline stages and actions using AWS SDK for JavaScript (CodePipeline, CodeBuild, CodeDeploy APIs). Automates blue-green deployments and cross-account pipeline configurations."
category: "CI/CD Integrations"
framework: "MCP"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-codepipeline-orchestrator/"
---
# AWS CodePipeline Orchestrator

Manages AWS CodePipeline stages and actions using AWS SDK for JavaScript (CodePipeline, CodeBuild, CodeDeploy APIs). Automates blue-green deployments and cross-account pipeline configurations.

## Overview

The AWS CodePipeline Orchestrator provides full lifecycle management of AWS CI/CD pipelines through the AWS SDK. It creates and configures pipeline stages using the CodePipeline API putPipeline method, sets up CodeBuild projects with custom buildspec.yml generation, and orchestrates CodeDeploy deployment groups for EC2, ECS, and Lambda targets. The skill manages cross-account pipeline execution through IAM role assumption chains, configures S3 artifact stores with KMS encryption, and implements manual approval actions with SNS notification integration. It uses the CloudWatch Events API to set up pipeline state change triggers, monitors build execution through the CodeBuild batchGetBuilds API, and implements automatic rollback based on CloudWatch alarm evaluations. The orchestrator handles pipeline variable resolution, configures parallel action groups within stages, and manages custom action type registrations for third-party integrations. Advanced features include pipeline-as-code templates using CloudFormation, automated testing gate insertion, and cross-region replication for disaster recovery pipelines. It also integrates with AWS Systems Manager Parameter Store for secure configuration injection during builds.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-codepipeline-orchestrator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-codepipeline-orchestrator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-codepipeline-orchestrator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-codepipeline-orchestrator -a codex
```

### OpenClaw

```bash
clawhub install aws-codepipeline-orchestrator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-codepipeline-orchestrator/)
