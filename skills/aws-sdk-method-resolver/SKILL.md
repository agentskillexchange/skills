---
title: "AWS SDK Method Resolver"
description: "Resolves AWS SDK v3 client commands and service endpoint signatures using @aws-sdk/client-* packages. Maps IAM permission requirements to specific API calls with request/response type definitions."
slug: "aws-sdk-method-resolver"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-sdk-method-resolver/"
listed: true
---

# AWS SDK Method Resolver

Resolves AWS SDK v3 client commands and service endpoint signatures using @aws-sdk/client-* packages. Maps IAM permission requirements to specific API calls with request/response type definitions.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install aws-sdk-method-resolver
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The AWS SDK Method Resolver indexes the complete AWS SDK v3 modular client surface across 300+ service packages. Given a task description, it identifies the correct @aws-sdk client package, command class, and input/output type interfaces. The skill maps each API call to its required IAM actions and resource ARN patterns, enabling least-privilege policy generation. It understands credential provider chains including SSO, AssumeRole, and container credential providers. For S3 operations, it handles multipart upload orchestration, presigned URL generation with expiry calculations, and server-side encryption configurations. DynamoDB queries get optimized with proper KeyConditionExpression construction, projection expressions, and consistent read strategies. The resolver also covers CloudFormation resource type schemas, helping translate infrastructure intent into correct template properties with dependency ordering.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-sdk-method-resolver/)
