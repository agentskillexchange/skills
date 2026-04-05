---
name: "Windmill Open-Source Workflow Engine and Developer Platform"
description: "Open-source developer platform to turn scripts into webhooks, workflows, and UIs. Self-hostable alternative to Retool and Temporal, supporting Python, TypeScript, Go, Bash, SQL, and more. Includes a built-in MCP server for AI agent integration."
category: "Templates & Workflows"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/windmill-labs/windmill"
tool_ecosystem:
  tool: windmill
  github_repo: windmill-labs/windmill
  github_stars: 16115
---
# Windmill Open-Source Workflow Engine and Developer Platform

Open-source developer platform to turn scripts into webhooks, workflows, and UIs. Self-hostable alternative to Retool and Temporal, supporting Python, TypeScript, Go, Bash, SQL, and more. Includes a built-in MCP server for AI agent integration.

## Overview

Windmill is an open-source developer platform and workflow engine that turns scripts into production-ready webhooks, workflows, and internal UIs. Published under the AGPLv3 license with 16,000+ GitHub stars, it serves as a self-hostable alternative to Retool, Temporal, Airflow, and Pipedream, designed for building internal tools, data pipelines, and automation at scale.

The platform supports writing scripts in Python, TypeScript, Go, Bash, SQL, GraphQL, PowerShell, Rust, and PHP. Each script is automatically turned into a shareable UI with auto-generated forms, and scripts can be composed into flows represented as directed acyclic graphs (DAGs) that handle branching, retries, error handling, and approval steps. For more complex interfaces, Windmill provides a low-code app builder that can combine multiple scripts and flows into rich internal dashboards.

Windmill includes a built-in MCP server that exposes workspace resources to AI agents. This allows LLM-powered tools to trigger workflows, query execution history, manage resources and variables, and generate scripts through natural language. The MCP integration supports scoped tokens for fine-grained access control, letting teams safely expose specific workflows to AI assistants while restricting access to sensitive operations.

The workflow engine claims to be 13x faster than Apache Airflow, handling thousands of concurrent jobs with sub-second cold starts. Technical features include a built-in job queue with priority scheduling, worker groups for resource isolation, approval flows with Slack and email notifications, cron scheduling, webhook triggers, and OAuth2 integration for connecting to third-party services. Version control is first-class: workflows and scripts sync bidirectionally with Git repositories via CLI or direct GitHub/GitLab integration.

Deployment options include Docker Compose for single-node setups and Helm charts for Kubernetes clusters. The platform provides a hosted option at app.windmill.dev for testing, along with a script and workflow Hub at hub.windmill.dev with community-contributed templates for common integrations. Enterprise features include SSO/SAML, audit logging, and dedicated support from Windmill Labs.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill windmill-workflow-engine-developer-platform
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill windmill-workflow-engine-developer-platform -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill windmill-workflow-engine-developer-platform -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill windmill-workflow-engine-developer-platform -a codex
```

### OpenClaw

```bash
clawhub install windmill-workflow-engine-developer-platform
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/windmill-workflow-engine-developer-platform/)
