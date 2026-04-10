---
title: "Vikunja Self-Hosted Task Management and Project Organization Platform"
description: "Vikunja is an open-source, self-hosted task management application written in Go with a Vue.js frontend. It provides lists, kanban boards, Gantt charts, and CalDAV sync for organizing personal and team projects with full data ownership."
slug: "vikunja-self-hosted-task-management"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/go-vikunja/vikunja"
tool_ecosystem:
  github_repo: "go-vikunja/vikunja"
  github_stars: 3768
listed: true
---

# Vikunja Self-Hosted Task Management and Project Organization Platform

Vikunja is an open-source, self-hosted task management application written in Go with a Vue.js frontend. It provides lists, kanban boards, Gantt charts, and CalDAV sync for organizing personal and team projects with full data ownership.

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
clawhub install vikunja-self-hosted-task-management
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Vikunja is an open-source task management application built with Go on the backend and Vue.js on the frontend. It provides a comprehensive set of features for organizing tasks, projects, and workflows while keeping all data under your control through self-hosting.
Core Capabilities
Vikunja supports multiple task organization views including traditional lists, kanban boards, and Gantt charts. Tasks can be organized into projects with labels, priorities, due dates, reminders, assignees, and sub-tasks. The application provides a REST API that enables integration with AI agents and automation tools for programmatic task management.
Technical Architecture
The backend is a single Go binary that bundles the API server, web frontend, and background workers. It supports SQLite, MySQL, and PostgreSQL as database backends. Authentication supports local accounts, OpenID Connect, and LDAP. The CalDAV interface allows synchronization with calendar applications like Thunderbird, GNOME Calendar, and iOS/macOS Reminders.
Deployment and Integration
Vikunja ships as a single Docker image (vikunja/vikunja) making deployment straightforward. The REST API at /api/v1 exposes all task, project, label, and user management operations. Webhooks can trigger external actions on task events. The application also supports file attachments, link sharing for collaboration, and task comments. A hosted version is available at vikunja.cloud for users who prefer not to self-host.
Agent Integration Points
The REST API enables AI agents to create tasks from natural language, query project status, update task progress, and manage team workflows programmatically. An MCP server (vikunja-mcp) is also available for direct integration with Claude Desktop, OpenCode, Cursor, and other MCP-compatible clients, enabling conversational task management through AI assistants.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vikunja-self-hosted-task-management/)
