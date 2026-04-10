---
name: "AWS SDK Method Resolver"
description: "Resolves AWS SDK v3 client commands and service endpoint signatures using @aws-sdk/client-* packages. Maps IAM permission requirements to specific API calls with request/response type definitions."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/aws-sdk-method-resolver/"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
---

# AWS SDK Method Resolver

The AWS SDK Method Resolver indexes the complete AWS SDK v3 modular client surface across 300+ service packages. Given a task description, it identifies the correct @aws-sdk client package, command class, and input/output type interfaces. The skill maps each API call to its required IAM actions and resource ARN patterns, enabling least-privilege policy generation. It understands credential provider chains including SSO, AssumeRole, and container credential providers. For S3 operations, it handles multipart upload orchestration, presigned URL generation with expiry calculations, and server-side encryption configurations. DynamoDB queries get optimized with proper KeyConditionExpression construction, projection expressions, and consistent read strategies. The resolver also covers CloudFormation resource type schemas, helping translate infrastructure intent into correct template properties with dependency ordering.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-sdk-method-resolver/)
