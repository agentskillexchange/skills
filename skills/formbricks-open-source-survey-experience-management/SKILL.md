---
title: "Formbricks Open Source Survey and Experience Management Platform"
description: "Formbricks is an open source survey platform and privacy-first experience management solution. Create in-app, website, link, and email surveys to gather user and customer insights at every point of their journey."
slug: "formbricks-open-source-survey-experience-management"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/formbricks/formbricks"
listed: true
---

# Formbricks Open Source Survey and Experience Management Platform

Formbricks is an open source survey platform and privacy-first experience management solution. Create in-app, website, link, and email surveys to gather user and customer insights at every point of their journey.

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
clawhub install formbricks-open-source-survey-experience-management
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Formbricks is the open source alternative to Qualtrics and Typeform, providing a full-featured survey and experience management platform that you can self-host for complete data ownership. Built with TypeScript, Next.js, React, and TailwindCSS, Formbricks lets teams create conversion-optimized surveys using a no-code editor with multiple question types.
Core Capabilities
Formbricks supports four distinct survey channels: in-app surveys triggered by user actions, website surveys for visitor feedback, shareable link surveys for broad distribution, and email surveys for targeted outreach. The platform includes best-practice survey templates, advanced targeting to launch surveys for specific user groups without changing application code, and a collaborative workspace where organization members work together on survey design and analysis.
Technical Architecture
The platform runs on a modern stack including Next.js for the application framework, Prisma for database management, Auth.js for authentication, and Zod for runtime validation. Deployment options include Docker-based self-hosting, Gitpod cloud development environments, or the managed cloud service at formbricks.com. The self-hosted version requires Node.js 18+, pnpm, and Docker for PostgreSQL.
Integration Ecosystem
Formbricks integrates with Slack for real-time survey response notifications, Notion for organizing feedback data, Zapier and n8n for workflow automation, and provides a REST API for custom integrations. The built-in Insight Platform offers data analysis capabilities including sentiment analysis, response trending, and cross-survey comparison. Agent skills can leverage the Formbricks API to programmatically create surveys, fetch responses, and trigger surveys based on application events.
Privacy and Compliance
As a self-hosted solution, Formbricks gives organizations complete control over survey data, making it suitable for teams with strict privacy requirements, GDPR compliance needs, or data residency constraints. The platform is licensed under AGPLv3 and backed by a Linux Foundation project with over 12,000 GitHub stars.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/formbricks-open-source-survey-experience-management/)
