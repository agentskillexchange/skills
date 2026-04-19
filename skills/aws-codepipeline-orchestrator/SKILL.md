---
title: "AWS CodePipeline Orchestrator"
description: "The AWS CodePipeline Orchestrator provides full lifecycle management of AWS CI/CD pipelines through the AWS SDK. It creates and configures pipeline stages using the CodePipeline API putPipeline method, sets up CodeBuild projects with custom buildspec.yml generation, and orchestrates CodeDeploy deployment groups for EC2, ECS, and Lambda targets. The skill manages cross-account pipeline execution through IAM role assumption chains, configures S3 artifact stores with KMS encryption, and implements manual approval actions with SNS notification integration. It uses the CloudWatch Events API to set up pipeline state change triggers, monitors build execution through the CodeBuild batchGetBuilds API, and implements automatic rollback based on CloudWatch alarm evaluations. The orchestrator handles pipeline variable resolution, configures parallel action groups within stages, and manages custom action type registrations for third-party integrations. Advanced features include pipeline-as-code templates using CloudFormation, automated testing gate insertion, and cross-region replication for disaster recovery pipelines. It also integrates with AWS Systems Manager Parameter Store for secure configuration injection during builds."
source: "https://github.com/aws/aws-sdk-js-v3"
verification: "security_reviewed"
category:
  - "CI/CD Integrations"
framework:
  - "MCP"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS CodePipeline Orchestrator

The AWS CodePipeline Orchestrator provides full lifecycle management of AWS CI/CD pipelines through the AWS SDK. It creates and configures pipeline stages using the CodePipeline API putPipeline method, sets up CodeBuild projects with custom buildspec.yml generation, and orchestrates CodeDeploy deployment groups for EC2, ECS, and Lambda targets. The skill manages cross-account pipeline execution through IAM role assumption chains, configures S3 artifact stores with KMS encryption, and implements manual approval actions with SNS notification integration. It uses the CloudWatch Events API to set up pipeline state change triggers, monitors build execution through the CodeBuild batchGetBuilds API, and implements automatic rollback based on CloudWatch alarm evaluations. The orchestrator handles pipeline variable resolution, configures parallel action groups within stages, and manages custom action type registrations for third-party integrations. Advanced features include pipeline-as-code templates using CloudFormation, automated testing gate insertion, and cross-region replication for disaster recovery pipelines. It also integrates with AWS Systems Manager Parameter Store for secure configuration injection during builds.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-codepipeline-orchestrator/)
