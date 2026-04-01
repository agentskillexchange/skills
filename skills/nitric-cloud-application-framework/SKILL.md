---
name: "Nitric Multi-Language Cloud Application Framework with Infrastructure from Code"
description: "Nitric is an open-source multi-language framework that lets you define cloud infrastructure directly from your application code in TypeScript, Python, Go, or Dart. Write once and deploy to AWS, GCP, or Azure without changing code, with built-in support for APIs, databases, queues, storage, and sc..."
category: "Developer Tools"
framework: "Multi-Framework"
verification: "listed"
source: "https://github.com/nitrictech/nitric"
---

# Nitric Multi-Language Cloud Application Framework with Infrastructure from Code

## Overview

Nitric is an open-source framework that takes the “infrastructure from code” approach: you declare cloud resources like APIs, databases, key-value stores, message queues, blob storage, and scheduled tasks inline in your application code using Nitric SDKs. The framework then automatically provisions the appropriate cloud services when you deploy — whether to AWS, GCP, or Azure — without any Terraform, CloudFormation, or platform-specific configuration.

## How It Works

Nitric SDKs are available for TypeScript/JavaScript, Python, Go, and Dart. When you write code like `const bucket = bucket("images")` or `const api = api("main")`, Nitric understands the cloud resources your app needs. At deployment time, Nitric translates these declarations into the appropriate cloud-native services: S3 or GCS for buckets, SQS or Cloud Pub/Sub for queues, DynamoDB or Firestore for key-value stores, and so on. Custom providers can target any infrastructure.

## Key Features

- **Multi-language support** — First-class SDKs for TypeScript, Python, Go, and Dart with consistent APIs across all languages.
- **Cloud-agnostic deployment** — Deploy the same codebase to AWS, GCP, or Azure without code changes. Swap cloud providers by changing a single configuration.
- **Infrastructure from code** — No separate IaC files. Resources are declared inline and automatically provisioned.
- **Local development dashboard** — Run your entire cloud application locally with emulated services and a visual dashboard for debugging.
- **IAM for humans** — Security permissions are declared alongside resource usage, ensuring least-privilege access by default.
- **Custom providers** — Build custom deployment providers for on-prem, edge, or any target infrastructure using Pulumi or Terraform under the hood.

## Agent Integration

Agents can use Nitric to build cloud applications without needing to understand the specifics of AWS, GCP, or Azure APIs. The `nitric new` command scaffolds projects, `nitric start` runs locally with a development dashboard, and `nitric up` deploys to the configured cloud. The consistent SDK surface across languages makes it straightforward for agents to generate deployment-ready cloud services.

## Installation

`# macOS
brew install nitrictech/tap/nitric
# Linux
curl -L "https://nitric.io/install?version=latest" | bash
# Windows
scoop bucket add nitric https://github.com/nitrictech/scoop-bucket.git
scoop install nitric`

## Requirements

Docker for local development. Node.js, Python, Go, or Dart runtime depending on your chosen language.

## Installation

Install this skill using one of these methods:

```bash
# ClawHub
clawhub install nitric-cloud-application-framework

# OpenClaw CLI
openclaw skills install nitric-cloud-application-framework

# Git
git clone https://github.com/agentskillexchange/skills.git
cp -r skills/skills/nitric-cloud-application-framework ~/.openclaw/workspace/skills/

# Manual download
# Download from: https://agentskillexchange.com/skills/nitric-cloud-application-framework/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nitric-cloud-application-framework/)
