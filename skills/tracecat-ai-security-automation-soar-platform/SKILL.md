---
title: "Tracecat AI-Native Security Automation and SOAR Platform"
description: "Tracecat is an open-source security orchestration, automation, and response (SOAR) platform designed specifically for security teams and AI agents. Positioned as a self-hosted alternative to commercial platforms like Tines and Splunk SOAR, Tracecat provides a comprehensive automation toolkit that combines workflow orchestration, AI agents, case management, and data tables in a single unified platform.\nArchitecture and Technology\nTracecat is built on a modern stack with Python (FastAPI, SQLAlchemy, Pydantic) on the backend and Next.js with TypeScript on the frontend. Durable workflow execution is powered by Temporal, ensuring reliability and scale. All untrusted code and agent operations run inside nsjail sandboxes for security isolation. Data is stored in PostgreSQL with S3-compatible object storage for attachments.\nKey Features\n\nAI Agents: Build custom agents with prompts, tools, chat interfaces, and MCP server integration (remote HTTP/OAuth or local via npx/uvx)\nWorkflows: Low-code visual builder with complex control flow including if-conditions, loops, and durable execution via Temporal\nCase Management: Track, automate, and resolve security incidents with agents and workflows\n100+ Integrations: Pre-built connectors to enterprise tools via HTTP, SMTP, gRPC, OAuth, and more\nCustom Registry: Turn custom Python scripts into agent tools and workflow steps synced from your Git repository\nSandboxed Execution: Run untrusted code and agents within nsjail sandboxes\nHuman-in-the-Loop: Review and approve sensitive tool calls from a unified inbox, Slack, or email\nMCP Server: Work with Tracecat through your own agent harness (Claude Code, Codex, OpenCode)\nFine-grained Access Control: RBAC, ABAC, OAuth2.0 scopes for humans and agents\nNo SSO Tax: SAML/OIDC support included in the open-source edition\n\nAgent Integration\nSecurity-focused AI agents can leverage Tracecat as their automation backbone. The platform’s MCP server enables agents built with Claude Code, Codex, or OpenCode to directly trigger workflows, manage cases, and query lookup tables. Agents can build prompt-to-automation pipelines for incident response, threat investigation, and compliance automation.\nDeployment\ngit clone https://github.com/TracecatHQ/tracecat.git\ncd tracecat\ndocker compose up -d\nSelf-host on Docker, Kubernetes, or AWS Fargate. Licensed under AGPL-3.0 with enterprise features available separately."
verification: security_reviewed
source: "https://github.com/TracecatHQ/tracecat"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "TracecatHQ/tracecat"
  github_stars: 3546
---

# Tracecat AI-Native Security Automation and SOAR Platform

Tracecat is an open-source security orchestration, automation, and response (SOAR) platform designed specifically for security teams and AI agents. Positioned as a self-hosted alternative to commercial platforms like Tines and Splunk SOAR, Tracecat provides a comprehensive automation toolkit that combines workflow orchestration, AI agents, case management, and data tables in a single unified platform.
Architecture and Technology
Tracecat is built on a modern stack with Python (FastAPI, SQLAlchemy, Pydantic) on the backend and Next.js with TypeScript on the frontend. Durable workflow execution is powered by Temporal, ensuring reliability and scale. All untrusted code and agent operations run inside nsjail sandboxes for security isolation. Data is stored in PostgreSQL with S3-compatible object storage for attachments.
Key Features

AI Agents: Build custom agents with prompts, tools, chat interfaces, and MCP server integration (remote HTTP/OAuth or local via npx/uvx)
Workflows: Low-code visual builder with complex control flow including if-conditions, loops, and durable execution via Temporal
Case Management: Track, automate, and resolve security incidents with agents and workflows
100+ Integrations: Pre-built connectors to enterprise tools via HTTP, SMTP, gRPC, OAuth, and more
Custom Registry: Turn custom Python scripts into agent tools and workflow steps synced from your Git repository
Sandboxed Execution: Run untrusted code and agents within nsjail sandboxes
Human-in-the-Loop: Review and approve sensitive tool calls from a unified inbox, Slack, or email
MCP Server: Work with Tracecat through your own agent harness (Claude Code, Codex, OpenCode)
Fine-grained Access Control: RBAC, ABAC, OAuth2.0 scopes for humans and agents
No SSO Tax: SAML/OIDC support included in the open-source edition

Agent Integration
Security-focused AI agents can leverage Tracecat as their automation backbone. The platform’s MCP server enables agents built with Claude Code, Codex, or OpenCode to directly trigger workflows, manage cases, and query lookup tables. Agents can build prompt-to-automation pipelines for incident response, threat investigation, and compliance automation.
Deployment
git clone https://github.com/TracecatHQ/tracecat.git
cd tracecat
docker compose up -d
Self-host on Docker, Kubernetes, or AWS Fargate. Licensed under AGPL-3.0 with enterprise features available separately.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/tracecat-ai-security-automation-soar-platform
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/tracecat-ai-security-automation-soar-platform` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tracecat-ai-security-automation-soar-platform/)
