---
name: "SST Open Source Full-Stack Application Deployment Framework"
description: "SST is an open-source framework for building and deploying full-stack applications on your own AWS infrastructure. It provides live development, resource linking, and components for Next.js, Remix, Astro, and more."
category: "Developer Tools"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/sst/sst"
---
# SST Open Source Full-Stack Application Deployment Framework

SST is an open-source framework for building and deploying full-stack applications on your own AWS infrastructure. It provides live development, resource linking, and components for Next.js, Remix, Astro, and more.

## Overview

SST (formerly Serverless Stack Toolkit) is an open-source framework that makes it straightforward to build and deploy full-stack applications on AWS. With over 25,000 GitHub stars and widespread adoption among serverless developers, SST has become one of the leading tools for teams that want production-grade infrastructure without leaving their codebase.

How SST Works

SST uses a component-based approach built on top of Pulumi and Terraform providers. You define your infrastructure in TypeScript alongside your application code. SST manages AWS resources like Lambda functions, API Gateway endpoints, S3 buckets, DynamoDB tables, CloudFront distributions, and more through typed, composable components.

Live Development

One of SST’s most distinctive features is its Live development mode. When you run `sst dev`, SST connects your local machine to your cloud environment in real time. Changes to your Lambda functions are reflected instantly without redeployment, cutting the feedback loop from minutes to milliseconds. This eliminates the need to mock AWS services locally.

Resource Linking

SST provides a linking system that lets you connect infrastructure resources (databases, queues, buckets) to your functions and frontends. Links are type-safe and work at both build time and runtime, so your application code can reference cloud resources without hardcoded ARNs or environment variables.

Framework Support

SST includes first-class support for deploying popular frontend frameworks: Next.js, Remix, Astro, SvelteKit, and SolidStart. Each framework gets its own optimized deployment target, handling edge functions, static assets, and server-side rendering automatically on AWS.

Agent Integration

AI agents can use SST to scaffold, configure, and deploy cloud infrastructure programmatically. The TypeScript-based configuration is well-suited for code generation. Agents can create new SST projects, add resources, configure linking, and trigger deployments through the CLI (`sst deploy`) or programmatic API.

Installation

Install via npm: `npm install sst` or globally: `curl -fsSL https://sst.dev/install | bash`

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill sst-open-source-full-stack-deployment-framework
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill sst-open-source-full-stack-deployment-framework -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill sst-open-source-full-stack-deployment-framework -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill sst-open-source-full-stack-deployment-framework -a codex
```

### OpenClaw

```bash
clawhub install sst-open-source-full-stack-deployment-framework
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sst-open-source-full-stack-deployment-framework/)
