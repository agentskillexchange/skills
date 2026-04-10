---
name: "Zammad Open Source Web-Based Helpdesk and Ticketing System"
description: "Zammad is a self-hosted, open-source helpdesk and customer support system with email, chat, phone, Twitter, and Telegram channel integration. It provides a REST and GraphQL API for ticket management, user administration, and workflow automation."
verification: security_reviewed
source: "https://github.com/zammad/zammad"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
---

# Zammad Open Source Web-Based Helpdesk and Ticketing System

Zammad is an open-source web-based helpdesk and customer support system built with Ruby on Rails and Vue.js. With over 5,500 GitHub stars and active development under the AGPL-3.0 license, it provides a feature-complete alternative to commercial helpdesk solutions like Zendesk and Freshdesk. Zammad aggregates customer communications from email, web forms, chat, phone (CTI), Twitter, Telegram, and SMS into a unified ticket management interface.
API Architecture
Zammad exposes both a comprehensive REST API and a GraphQL API for programmatic access. The REST API covers tickets, users, organizations, groups, tags, text modules, macros, triggers, and reporting. Every operation available in the web UI is accessible via API, enabling full automation of helpdesk workflows. The GraphQL API provides a modern query interface for mobile apps and single-page applications. Authentication supports API tokens, OAuth2, and session-based auth.
Ticket Workflow Automation
The platform includes a powerful automation engine with triggers (event-based rules), schedulers (time-based rules), and macros (manual batch actions). Triggers fire on ticket creation, update, or time-based conditions, executing actions like auto-assignment, tagging, notification, and state changes. SLA management tracks first-response times, update intervals, and resolution deadlines with escalation chains. These automations are configurable via the API, allowing AI agents to programmatically create and modify workflow rules.
Self-Hosted Deployment
Zammad can be deployed via Docker Compose, DEB/RPM packages for Debian/Ubuntu/RHEL/SUSE, or compiled from source. It requires PostgreSQL or MySQL as the database backend and Elasticsearch for full-text search and reporting. Redis is used for caching and WebSocket support. The platform supports LDAP/Active Directory integration for user management, S/MIME and PGP for email encryption, and custom object creation for extending the data model without code changes.
Agent Integration Use Cases
AI coding agents can integrate Zammad to automate customer support operations: creating tickets from external events, classifying and routing incoming tickets using NLP analysis, generating response suggestions based on knowledge base articles, tracking SLA compliance metrics, bulk-updating tickets based on criteria, and building custom reporting dashboards from ticket data. The combination of REST API, GraphQL, and webhook triggers provides flexible integration points for intelligent support automation.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/zammad-open-source-helpdesk-ticketing-system/)
