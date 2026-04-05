---
name: "Leantime Open Source Goals-Focused Project Management Platform"
description: "Leantime is an open-source project management system designed for non-project managers, with kanban boards, gantt charts, goal tracking, timesheets, and lean canvas tools. Built with ADHD, autism, and dyslexia accessibility in mind."
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/Leantime/leantime"
tool_ecosystem:
  tool: leantime
  github_repo: leantime/leantime
  github_stars: 9460
  license: AGPL-3.0
  maintained: true
---
# Leantime Open Source Goals-Focused Project Management Platform

Leantime is an open-source project management system designed for non-project managers, with kanban boards, gantt charts, goal tracking, timesheets, and lean canvas tools. Built with ADHD, autism, and dyslexia accessibility in mind.

## Overview

Leantime is an open-source, self-hosted project management platform that combines strategy, planning, and execution in an interface designed for non-project managers. It positions itself as an alternative to ClickUp, Monday, and Asana, with the simplicity of Trello but the feature depth of Jira.

Core Features

Task management is available via kanban boards, gantt charts, table views, list views, and calendar views. Projects get dashboards with reports and status updates. The platform includes goal and metrics tracking, milestone management, sprint management, and timetracking with timesheets. Strategic planning tools include Lean Canvas, Business Model Canvas, SWOT Analysis, and Risk Analysis.

Collaboration and Knowledge

Leantime includes wikis and docs for knowledge management, idea boards for brainstorming, retrospectives for team improvement, and file storage via S3 or local filesystem. Comments and discussions are available on every entity. Integrations with Slack, Mattermost, and Discord keep teams connected. The platform supports over 20 languages.

Technical Details

Leantime requires PHP 8.2+, MySQL 8.0+ or MariaDB 10.6+, and Apache or Nginx. It is available as a Docker image on Docker Hub (`docker pull leantime/leantime`) or as a traditional PHP installation from GitHub Releases. The platform supports LDAP and OIDC authentication, two-factor authentication, multiple user roles with per-project permissions, and is extendable via plugins and API. Licensed under AGPL-3.0.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill leantime-open-source-project-management-platform
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill leantime-open-source-project-management-platform -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill leantime-open-source-project-management-platform -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill leantime-open-source-project-management-platform -a codex
```

### OpenClaw

```bash
clawhub install leantime-open-source-project-management-platform
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/leantime-open-source-project-management-platform/)
