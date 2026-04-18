---
title: "AWS SDK Method Resolver"
description: "Resolves AWS SDK v3 client commands and service endpoint signatures using @aws-sdk/client-* packages. Maps IAM permission requirements to specific API calls with request/response type definitions."
verification: security_reviewed
source: "https://github.com/aws/aws-sdk-js-v3"
category:
  - "Library & API Reference"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "aws/aws-sdk-js-v3"
  github_stars: 3607
---

# AWS SDK Method Resolver

The AWS SDK Method Resolver indexes the complete AWS SDK v3 modular client surface across 300+ service packages. Given a task description, it identifies the correct @aws-sdk client package, command class, and input/output type interfaces. The skill maps each API call to its required IAM actions and resource ARN patterns, enabling least-privilege policy generation. It understands credential provider chains including SSO, AssumeRole, and container credential providers. For S3 operations, it handles multipart upload orchestration, presigned URL generation with expiry calculations, and server-side encryption configurations. DynamoDB queries get optimized with proper KeyConditionExpression construction, projection expressions, and consistent read strategies. The resolver also covers CloudFormation resource type schemas, helping translate infrastructure intent into correct template properties with dependency ordering.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/aws-sdk-method-resolver
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/aws-sdk-method-resolver` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-sdk-method-resolver/)
