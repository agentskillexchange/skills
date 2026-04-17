---
title: "AWS CodePipeline Orchestrator"
description: "Manages AWS CodePipeline stages and actions using AWS SDK for JavaScript (CodePipeline, CodeBuild, CodeDeploy APIs). Automates blue-green deployments and cross-account pipeline configurations."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
  license: "Apache-2.0"
---

# AWS CodePipeline Orchestrator

The AWS CodePipeline Orchestrator provides full lifecycle management of AWS CI/CD pipelines through the AWS SDK. It creates and configures pipeline stages using the CodePipeline API putPipeline method, sets up CodeBuild projects with custom buildspec.yml generation, and orchestrates CodeDeploy deployment groups for EC2, ECS, and Lambda targets. The skill manages cross-account pipeline execution through IAM role assumption chains, configures S3 artifact stores with KMS encryption, and implements manual approval actions with SNS notification integration. It uses the CloudWatch Events API to set up pipeline state change triggers, monitors build execution through the CodeBuild batchGetBuilds API, and implements automatic rollback based on CloudWatch alarm evaluations. The orchestrator handles pipeline variable resolution, configures parallel action groups within stages, and manages custom action type registrations for third-party integrations. Advanced features include pipeline-as-code templates using CloudFormation, automated testing gate insertion, and cross-region replication for disaster recovery pipelines. It also integrates with AWS Systems Manager Parameter Store for secure configuration injection during builds.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-codepipeline-orchestrator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aws-codepipeline-orchestrator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-codepipeline-orchestrator/)
