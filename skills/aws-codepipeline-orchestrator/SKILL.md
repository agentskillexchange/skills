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
---

# AWS CodePipeline Orchestrator

The AWS CodePipeline Orchestrator provides full lifecycle management of AWS CI/CD pipelines through the AWS SDK. It creates and configures pipeline stages using the CodePipeline API putPipeline method, sets up CodeBuild projects with custom buildspec.yml generation, and orchestrates CodeDeploy deployment groups for EC2, ECS, and Lambda targets. The skill manages cross-account pipeline execution through IAM role assumption chains, configures S3 artifact stores with KMS encryption, and implements manual approval actions with SNS notification integration. It uses the CloudWatch Events API to set up pipeline state change triggers, monitors build execution through the CodeBuild batchGetBuilds API, and implements automatic rollback based on CloudWatch alarm evaluations. The orchestrator handles pipeline variable resolution, configures parallel action groups within stages, and manages custom action type registrations for third-party integrations. Advanced features include pipeline-as-code templates using CloudFormation, automated testing gate insertion, and cross-region replication for disaster recovery pipelines. It also integrates with AWS Systems Manager Parameter Store for secure configuration injection during builds.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-codepipeline-orchestrator/)
