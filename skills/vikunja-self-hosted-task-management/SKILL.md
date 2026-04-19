---
title: "Vikunja Self-Hosted Task Management and Project Organization Platform"
description: "Vikunja is an open-source task management application built with Go on the backend and Vue.js on the frontend. It provides a comprehensive set of features for organizing tasks, projects, and workflows while keeping all data under your control through self-hosting. Core Capabilities Vikunja supports multiple task organization views including traditional lists, kanban boards, and Gantt charts. Tasks can be organized into projects with labels, priorities, due dates, reminders, assignees, and sub-tasks. The application provides a REST API that enables integration with AI agents and automation tools for programmatic task management. Technical Architecture The backend is a single Go binary that bundles the API server, web frontend, and background workers. It supports SQLite, MySQL, and PostgreSQL as database backends. Authentication supports local accounts, OpenID Connect, and LDAP. The CalDAV interface allows synchronization with calendar applications like Thunderbird, GNOME Calendar, and iOS/macOS Reminders. Deployment and Integration Vikunja ships as a single Docker image (vikunja/vikunja) making deployment straightforward. The REST API at /api/v1 exposes all task, project, label, and user management operations. Webhooks can trigger external actions on task events. The application also supports file attachments, link sharing for collaboration, and task comments. A hosted version is available at vikunja.cloud for users who prefer not to self-host. Agent Integration Points The REST API enables AI agents to create tasks from natural language, query project status, update task progress, and manage team workflows programmatically. An MCP server (vikunja-mcp) is also available for direct integration with Claude Desktop, OpenCode, Cursor, and other MCP-compatible clients, enabling conversational task management through AI assistants."
source: "https://github.com/go-vikunja/vikunja"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "go-vikunja/vikunja"
  github_stars: 3768
---

# Vikunja Self-Hosted Task Management and Project Organization Platform

Vikunja is an open-source task management application built with Go on the backend and Vue.js on the frontend. It provides a comprehensive set of features for organizing tasks, projects, and workflows while keeping all data under your control through self-hosting. Core Capabilities Vikunja supports multiple task organization views including traditional lists, kanban boards, and Gantt charts. Tasks can be organized into projects with labels, priorities, due dates, reminders, assignees, and sub-tasks. The application provides a REST API that enables integration with AI agents and automation tools for programmatic task management. Technical Architecture The backend is a single Go binary that bundles the API server, web frontend, and background workers. It supports SQLite, MySQL, and PostgreSQL as database backends. Authentication supports local accounts, OpenID Connect, and LDAP. The CalDAV interface allows synchronization with calendar applications like Thunderbird, GNOME Calendar, and iOS/macOS Reminders. Deployment and Integration Vikunja ships as a single Docker image (vikunja/vikunja) making deployment straightforward. The REST API at /api/v1 exposes all task, project, label, and user management operations. Webhooks can trigger external actions on task events. The application also supports file attachments, link sharing for collaboration, and task comments. A hosted version is available at vikunja.cloud for users who prefer not to self-host. Agent Integration Points The REST API enables AI agents to create tasks from natural language, query project status, update task progress, and manage team workflows programmatically. An MCP server (vikunja-mcp) is also available for direct integration with Claude Desktop, OpenCode, Cursor, and other MCP-compatible clients, enabling conversational task management through AI assistants.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vikunja-self-hosted-task-management/)
