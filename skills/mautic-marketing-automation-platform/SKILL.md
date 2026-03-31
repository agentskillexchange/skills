---
name: "Mautic Open Source Marketing Automation Platform"
description: "Mautic is the world's largest open-source marketing automation platform with 7.9K+ GitHub stars. It provides email campaign management, lead scoring, contact segmentation, landing pages, and multi-channel marketing automation with a full REST API for programmatic control."
category: "Calendar, Email &amp; Productivity"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/mautic/mautic"
tool_ecosystem:
  tool: mautic
  github_repo: mautic/mautic
  github_stars: 9377
  maintained: true
---
# Mautic Open Source Marketing Automation Platform

Mautic is the world's largest open-source marketing automation platform with 7.9K+ GitHub stars. It provides email campaign management, lead scoring, contact segmentation, landing pages, and multi-channel marketing automation with a full REST API for programmatic control.

## Overview

Mautic is a comprehensive open-source marketing automation platform that empowers businesses to manage email campaigns, track contacts, score leads, and automate multi-channel marketing workflows. With over 7,900 GitHub stars and an active community, it is the most widely adopted open-source alternative to commercial platforms like HubSpot and Marketo.

Core Capabilities
The platform provides a visual campaign builder for creating automated marketing workflows, email template management with drag-and-drop editing, contact and company management with custom fields, lead scoring based on behavior and demographics, and dynamic content personalization. It supports multi-channel delivery across email, SMS, web notifications, and social media.

REST API and Integration
Mautic exposes a comprehensive REST API for managing contacts, companies, campaigns, emails, forms, segments, and assets programmatically. Agents can create and send email campaigns, manage contact lists, trigger automation workflows, update lead scores, and query analytics data through the API. OAuth2 and Basic authentication are supported for secure API access.

Segmentation and Automation
The segmentation engine allows creating dynamic contact segments based on behavior, demographics, page visits, email engagement, and custom field values. Campaign automation supports conditional branching, time delays, multi-step workflows, A/B testing, and integration with external systems via webhooks and the plugin API.

Deployment and Architecture
Mautic is built on Symfony and requires PHP 8.0+ and MySQL/MariaDB. It can be self-hosted on any standard LAMP/LEMP stack or deployed via Docker. The platform supports multi-tenancy, DDEV for local development, and includes a plugin system for extending functionality with CRM integrations, social media connectors, and custom workflow actions.

Agent Use Cases
Agents can leverage Mautic to automate email outreach campaigns, manage and segment contact databases, track website visitor behavior, score and qualify leads based on engagement, generate marketing performance reports, and orchestrate multi-step nurture sequences without relying on proprietary SaaS platforms.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill mautic-marketing-automation-platform
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill mautic-marketing-automation-platform -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill mautic-marketing-automation-platform -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill mautic-marketing-automation-platform -a codex
```

### OpenClaw

```bash
clawhub install mautic-marketing-automation-platform
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mautic-marketing-automation-platform/)
