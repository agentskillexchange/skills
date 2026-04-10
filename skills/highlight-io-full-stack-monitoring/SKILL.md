---
title: "Highlight.io Open Source Full-Stack Monitoring Platform"
description: "Highlight.io is an open-source full-stack monitoring platform combining session replay, error monitoring, logging, and distributed tracing in a single cohesive tool. Self-hostable via Docker, it provides complete application observability for frontend and backend."
slug: "highlight-io-full-stack-monitoring"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/highlight/highlight"
listed: true
---

# Highlight.io Open Source Full-Stack Monitoring Platform

Highlight.io is an open-source full-stack monitoring platform combining session replay, error monitoring, logging, and distributed tracing in a single cohesive tool. Self-hostable via Docker, it provides complete application observability for frontend and backend.

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
clawhub install highlight-io-full-stack-monitoring
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Highlight.io is an open-source, full-stack monitoring platform that combines session replay, error monitoring, logging, and distributed tracing into a single unified tool. Unlike traditional monitoring solutions that require separate tools for each concern, Highlight.io provides cohesive observability across the entire application stack.
What It Does
Highlight.io captures everything needed to understand application behavior and debug issues: DOM-based session replay showing exact user interactions, error tracking with full stack traces, structured logging with search and filtering, and distributed traces connecting frontend actions to backend operations.
Key Features
Session Replay: High-fidelity DOM-based replay powered by rrweb captures every user interaction and DOM change. See exactly what users experienced, including network requests, console logs, and errors in context.
Error Monitoring: Automatic error capture across frontend and backend with full stack traces, source map support, error grouping, and alert configuration. Errors are linked to the session where they occurred.
Logging: Structured log ingestion with powerful search, filtering, and correlation. Logs are automatically connected to traces and sessions for complete context during debugging.
Distributed Tracing: End-to-end request tracing from browser to backend services. Traces show the complete request lifecycle with timing breakdowns and error attribution.
Self-Hosted Deployment: Deploy with a single Docker command for hobby instances, or use the enterprise deployment guide for production-scale installations. All data stays on your infrastructure.
SDK Support
Highlight.io provides SDKs for JavaScript/TypeScript (React, Next.js, Vue, Angular), Python (Django, Flask, FastAPI), Go (net/http, Gin, GORM), Ruby (Rails), Java (Spring Boot), and Rust. Each SDK integrates with popular frameworks and provides automatic instrumentation.
How Agents Use It
AI agents responsible for application monitoring and incident response can use Highlight.io to investigate production issues. An agent can query error data via the API, correlate errors with session replays to understand user impact, search logs for related events, and trace requests across services to identify root causes. For DevOps agents, Highlight.io provides the observability data needed for automated diagnostics and alerting workflows.
Installation
git clone --recurse-submodules https://github.com/highlight/highlight
cd docker && ./run-hobby.sh
For the hosted version, install the client SDK:
npm install highlight.run
Integration Points
Highlight.io integrates with Slack, Discord, Linear, Jira, Clickup, Vercel, and other tools for alerting and workflow automation. It supports OpenTelemetry for trace and log ingestion, making it compatible with existing observability pipelines.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/highlight-io-full-stack-monitoring/)
