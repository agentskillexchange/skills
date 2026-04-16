---
title: "Leantime Open Source Goals-Focused Project Management Platform"
description: "Leantime is an open-source project management system designed for non-project managers, with kanban boards, gantt charts, goal tracking, timesheets, and lean canvas tools. Built with ADHD, autism, and dyslexia accessibility in mind."
verification: "security_reviewed"
source: "https://github.com/Leantime/leantime"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Multi-Framework"
---

# Leantime Open Source Goals-Focused Project Management Platform

Leantime is an open-source, self-hosted project management platform that combines strategy, planning, and execution in an interface designed for non-project managers. It positions itself as an alternative to ClickUp, Monday, and Asana, with the simplicity of Trello but the feature depth of Jira.


Core Features
Task management is available via kanban boards, gantt charts, table views, list views, and calendar views. Projects get dashboards with reports and status updates. The platform includes goal and metrics tracking, milestone management, sprint management, and timetracking with timesheets. Strategic planning tools include Lean Canvas, Business Model Canvas, SWOT Analysis, and Risk Analysis.


Collaboration and Knowledge
Leantime includes wikis and docs for knowledge management, idea boards for brainstorming, retrospectives for team improvement, and file storage via S3 or local filesystem. Comments and discussions are available on every entity. Integrations with Slack, Mattermost, and Discord keep teams connected. The platform supports over 20 languages.


Technical Details
Leantime requires PHP 8.2+, MySQL 8.0+ or MariaDB 10.6+, and Apache or Nginx. It is available as a Docker image on Docker Hub (docker pull leantime/leantime) or as a traditional PHP installation from GitHub Releases. The platform supports LDAP and OIDC authentication, two-factor authentication, multiple user roles with per-project permissions, and is extendable via plugins and API. Licensed under AGPL-3.0.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/leantime-open-source-project-management-platform/)
