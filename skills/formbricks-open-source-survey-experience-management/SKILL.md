---
title: "Formbricks Open Source Survey and Experience Management Platform"
description: "Formbricks is an open source survey platform and privacy-first experience management solution. Create in-app, website, link, and email surveys to gather user and customer insights at every point of their journey."
verification: "security_reviewed"
source: "https://github.com/formbricks/formbricks"
category:
  - "Integrations & Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "formbricks/formbricks"
  github_stars: 12057
---

# Formbricks Open Source Survey and Experience Management Platform

Formbricks is the open source alternative to Qualtrics and Typeform, providing a full-featured survey and experience management platform that you can self-host for complete data ownership. Built with TypeScript, Next.js, React, and TailwindCSS, Formbricks lets teams create conversion-optimized surveys using a no-code editor with multiple question types.

Core Capabilities
Formbricks supports four distinct survey channels: in-app surveys triggered by user actions, website surveys for visitor feedback, shareable link surveys for broad distribution, and email surveys for targeted outreach. The platform includes best-practice survey templates, advanced targeting to launch surveys for specific user groups without changing application code, and a collaborative workspace where organization members work together on survey design and analysis.

Technical Architecture
The platform runs on a modern stack including Next.js for the application framework, Prisma for database management, Auth.js for authentication, and Zod for runtime validation. Deployment options include Docker-based self-hosting, Gitpod cloud development environments, or the managed cloud service at formbricks.com. The self-hosted version requires Node.js 18+, pnpm, and Docker for PostgreSQL.

Integration Ecosystem
Formbricks integrates with Slack for real-time survey response notifications, Notion for organizing feedback data, Zapier and n8n for workflow automation, and provides a REST API for custom integrations. The built-in Insight Platform offers data analysis capabilities including sentiment analysis, response trending, and cross-survey comparison. Agent skills can leverage the Formbricks API to programmatically create surveys, fetch responses, and trigger surveys based on application events.

Privacy and Compliance
As a self-hosted solution, Formbricks gives organizations complete control over survey data, making it suitable for teams with strict privacy requirements, GDPR compliance needs, or data residency constraints. The platform is licensed under AGPLv3 and backed by a Linux Foundation project with over 12,000 GitHub stars.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/formbricks-open-source-survey-experience-management/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/formbricks-open-source-survey-experience-management
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/formbricks-open-source-survey-experience-management`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/formbricks-open-source-survey-experience-management/)
