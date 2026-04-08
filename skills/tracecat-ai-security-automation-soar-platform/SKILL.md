---
title: Tracecat AI-Native Security Automation and SOAR Platform
description: 'Tracecat is an open-source security orchestration, automation, and response
  (SOAR) platform designed specifically for security teams and AI agents. Positioned
  as a self-hosted alternative to commercial platforms like Tines and Splunk SOAR,
  Tracecat provides a comprehensive automation toolkit that combines workflow orchestration,
  AI agents, case management, and data tables in a single unified platform. Architecture
  and Technology Tracecat is built on a modern stack with Python (FastAPI, SQLAlchemy,
  Pydantic) on the backend and Next.js with TypeScript on the frontend. Durable workflow
  execution is powered by Temporal, ensuring reliability and scale. All untrusted
  code and agent operations run inside nsjail sandboxes for security isolation. Data
  is stored in PostgreSQL with S3-compatible object storage for attachments. Key Features
  AI Agents : Build custom agents with prompts, tools, chat interfaces, and MCP server
  integration (remote HTTP/OAuth or local via npx/uvx) Workflows : Low-code visual
  builder with complex control flow including if-conditions, loops, and durable execution
  via Temporal Case Management : Track, automate, and resolve security incidents with
  agents and workflows 100+ Integrations : Pre-built connectors to enterprise tools
  via HTTP, SMTP, gRPC, OAuth, and more Custom Registry : Turn custom Python scripts
  into agent tools and workflow steps synced from your Git repository Sandboxed Execution
  : Run untrusted code and agents within nsjail sandboxes Human-in-the-Loop : Review
  and approve sensitive tool calls from a unified inbox, Slack, or email MCP Server
  : Work with Tracecat through your own agent harness (Claude Code, Codex, OpenCode)
  Fine-grained Access Control : RBAC, ABAC, OAuth2.0 scopes for humans and agents
  No SSO Tax : SAML/OIDC support included in the open-source edition Agent Integration
  Security-focused AI agents can leverage Tracecat as their automation backbone. The
  platform’s MCP server enables agents built with Claude Code, Codex, or OpenCode
  to directly trigger workflows, manage cases, and query lookup tables. Agents can
  build prompt-to-automation pipelines for incident response, threat investigation,
  and compliance automation. Deployment git clone https://github.com/TracecatHQ/tracecat.git
  cd tracecat docker compose up -d Self-host on Docker, Kubernetes, or AWS Fargate.
  Licensed under AGPL-3.0 with enterprise features available separately.'
verification: security_reviewed
source: https://github.com/TracecatHQ/tracecat
category:
- Security &amp; Verification
framework:
- Multi-Framework
---

# Tracecat AI-Native Security Automation and SOAR Platform

Tracecat is an open-source security orchestration, automation, and response (SOAR) platform designed specifically for security teams and AI agents. Positioned as a self-hosted alternative to commercial platforms like Tines and Splunk SOAR, Tracecat provides a comprehensive automation toolkit that combines workflow orchestration, AI agents, case management, and data tables in a single unified platform. Architecture and Technology Tracecat is built on a modern stack with Python (FastAPI, SQLAlchemy, Pydantic) on the backend and Next.js with TypeScript on the frontend. Durable workflow execution is powered by Temporal, ensuring reliability and scale. All untrusted code and agent operations run inside nsjail sandboxes for security isolation. Data is stored in PostgreSQL with S3-compatible object storage for attachments. Key Features AI Agents : Build custom agents with prompts, tools, chat interfaces, and MCP server integration (remote HTTP/OAuth or local via npx/uvx) Workflows : Low-code visual builder with complex control flow including if-conditions, loops, and durable execution via Temporal Case Management : Track, automate, and resolve security incidents with agents and workflows 100+ Integrations : Pre-built connectors to enterprise tools via HTTP, SMTP, gRPC, OAuth, and more Custom Registry : Turn custom Python scripts into agent tools and workflow steps synced from your Git repository Sandboxed Execution : Run untrusted code and agents within nsjail sandboxes Human-in-the-Loop : Review and approve sensitive tool calls from a unified inbox, Slack, or email MCP Server : Work with Tracecat through your own agent harness (Claude Code, Codex, OpenCode) Fine-grained Access Control : RBAC, ABAC, OAuth2.0 scopes for humans and agents No SSO Tax : SAML/OIDC support included in the open-source edition Agent Integration Security-focused AI agents can leverage Tracecat as their automation backbone. The platform’s MCP server enables agents built with Claude Code, Codex, or OpenCode to directly trigger workflows, manage cases, and query lookup tables. Agents can build prompt-to-automation pipelines for incident response, threat investigation, and compliance automation. Deployment git clone https://github.com/TracecatHQ/tracecat.git cd tracecat docker compose up -d Self-host on Docker, Kubernetes, or AWS Fargate. Licensed under AGPL-3.0 with enterprise features available separately.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tracecat-ai-security-automation-soar-platform/)
