---
name: "AWS SDK Method Resolver"
description: "Resolves AWS SDK v3 client commands and service endpoint signatures using @aws-sdk/client-* packages. Maps IAM permission requirements to specific API calls with request/response type definitions."
category: "Library & API Reference"
framework: "Claude Code"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/aws-sdk-method-resolver/"
tool_ecosystem:
  tool: aws
  github_stars: 3594
  npm_weekly_downloads: 9204385
  github_repo: aws/aws-sdk-js-v3
  license: Apache-2.0
  maintained: true
---

# AWS SDK Method Resolver

Resolves AWS SDK v3 client commands and service endpoint signatures using @aws-sdk/client-* packages. Maps IAM permission requirements to specific API calls with request/response type definitions.

## Overview

The AWS SDK Method Resolver indexes the complete AWS SDK v3 modular client surface across 300+ service packages. Given a task description, it identifies the correct @aws-sdk client package, command class, and input/output type interfaces. The skill maps each API call to its required IAM actions and resource ARN patterns, enabling least-privilege policy generation. It understands credential provider chains including SSO, AssumeRole, and container credential providers. For S3 operations, it handles multipart upload orchestration, presigned URL generation with expiry calculations, and server-side encryption configurations. DynamoDB queries get optimized with proper KeyConditionExpression construction, projection expressions, and consistent read strategies. The resolver also covers CloudFormation resource type schemas, helping translate infrastructure intent into correct template properties with dependency ordering.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill aws-sdk-method-resolver
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill aws-sdk-method-resolver -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill aws-sdk-method-resolver -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill aws-sdk-method-resolver -a codex
```

### OpenClaw

```bash
clawhub install aws-sdk-method-resolver
```

## Source

- Marketplace: https://agentskillexchange.com/skills/aws-sdk-method-resolver/
