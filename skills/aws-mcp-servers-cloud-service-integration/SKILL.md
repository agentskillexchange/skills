---
name: "AWS MCP Servers for Cloud Service Integration"
slug: "aws-mcp-servers-cloud-service-integration"
description: "The official AWS Labs MCP server collection provides AI agents with structured access to AWS documentation, service APIs, billing data, and infrastructure metadata through the Model Context Protocol, built and maintained by AWS for secure cloud automation workflows."
github_stars: 8645
verification: "security_reviewed"
source: "https://github.com/awslabs/mcp"
category: "Integrations & Connectors"
framework: "MCP"
tool_ecosystem:
  github_repo: "awslabs/mcp"
  github_stars: 8645
---

# AWS MCP Servers for Cloud Service Integration

The official AWS Labs MCP server collection provides AI agents with structured access to AWS documentation, service APIs, billing data, and infrastructure metadata through the Model Context Protocol, built and maintained by AWS for secure cloud automation workflows.

## Installation

Use the upstream install or setup path that matches your environment:
- Install uv from [Astral](https://docs.astral.sh/uv/getting-started/installation/)
- Docker images for each MCP server are published to the [public AWS ECR registry](https://gallery.ecr.aws/awslabs-mcp).
- docker build -t awslabs/aws-documentation-mcp-server .
- Follow the steps above in the **Installation and Setup** section to install uv from [Astral](https://docs.astral.sh/uv/getting-started/installation/), install Python, and configure AWS credentials with the required se...

Requirements and caveats from upstream:
- A Python library for creating serverless HTTP handlers for the Model Context Protocol (MCP) using AWS Lambda. This module provides a flexible framework for building MCP HTTP endpoints with pluggable session management...
- Install Python using uv python install 3.10
- *This example uses docker with the "awslabs.aws-documentation-mcp-server and can be repeated for each MCP server*

Basic usage or getting-started notes:
- [🚀 Getting Started with AWS](#-getting-started-with-aws)
- [Getting Started with Kiro](#getting-started-with-kiro)
- [Getting Started with Cline and Amazon Bedrock](#getting-started-with-cline-and-amazon-bedrock)

- Source: https://github.com/awslabs/mcp
- Extracted from upstream docs: https://raw.githubusercontent.com/awslabs/mcp/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/aws-mcp-servers-cloud-service-integration/)
