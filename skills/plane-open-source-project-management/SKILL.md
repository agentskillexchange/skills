---
name: Plane Open Source Project Management Platform
description: Plane is an open-source project management platform that serves as a
  self-hostable alternative to Jira, Linear, and ClickUp. It provides issue tracking,
  sprint cycles, product roadmaps, collaborative documents, and project analytics
  with a modern interface and full data ownership.
category: "Calendar, Email &amp; Productivity"
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/makeplane/plane"
tool_ecosystem:
  github_repo: "https://github.com/makeplane/plane"
  github_stars: 47285
---
# Plane Open Source Project Management Platform

Plane is an open-source project management platform that serves as a self-hostable alternative to Jira, Linear, and ClickUp. It provides issue tracking, sprint cycles, product roadmaps, collaborative documents, and project analytics with a modern interface and full data ownership.

What Plane Does

Plane is a full-featured project management platform built for engineering and product teams. It covers the core workflow loop: create work items, organize them into sprints (cycles), group them into feature modules, and track progress with analytics dashboards. The platform includes a document editor with AI capabilities (Pages), customizable views with saved filters, and triage workflows for incoming work.

Why It Matters for Agents

Plane provides a REST API and webhooks that enable agents to create, update, and query project data programmatically. An agent can triage incoming issues, update sprint progress, generate status reports from live data, or automate repetitive project management tasks like backlog grooming. Because Plane is self-hosted, all project data stays under your control — no third-party API rate limits or data residency concerns.

Key Features

- Work items: Rich text editor with file uploads, sub-properties, and cross-references between issues

- Cycles (sprints): Time-boxed iterations with burn-down charts and velocity tracking

- Modules: Group related work items into feature-scoped containers for complex projects

- Views: Custom filtered views that can be saved and shared across the team

- Pages: Collaborative documents with AI features for capturing and organizing project knowledge

- Analytics: Real-time project insights with trend visualization and blocker identification

- Self-hostable: Deploy via Docker Compose or Kubernetes with full data ownership

- Cloud option: Hosted version at app.plane.so for teams that prefer managed infrastructure

Integration Points

Plane connects to development workflows through GitHub and GitLab integrations for linking commits and PRs to work items. The REST API supports CRUD operations on all core entities (projects, issues, cycles, modules). Webhooks enable event-driven automation — for example, notifying a Slack channel when a sprint completes or triggering a deployment pipeline when all issues in a module are closed.

Install Notes

Self-host with Docker Compose following the guide at developers.plane.so. Kubernetes deployment is also supported. For managed hosting, sign up at app.plane.so. Instance configuration is managed through God Mode for administrators.

Source: github.com/makeplane/plane

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill plane-open-source-project-management
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill plane-open-source-project-management -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill plane-open-source-project-management -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill plane-open-source-project-management -a codex
```

### OpenClaw

```bash
clawhub install plane-open-source-project-management
```


## Source

- [GitHub](https://github.com/makeplane/plane)
