---
title: "Listmonk Self-Hosted Newsletter and Mailing List Manager"
description: "High-performance, self-hosted newsletter and mailing list manager packed into a single binary. Manages millions of subscribers with templated campaigns, analytics, and a REST API for programmatic email automation."
slug: "listmonk-self-hosted-newsletter-mailing-list"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://github.com/knadh/listmonk"
tool_ecosystem:
  github_repo: "knadh/listmonk"
  github_stars: 19404
listed: true
---

# Listmonk Self-Hosted Newsletter and Mailing List Manager

High-performance, self-hosted newsletter and mailing list manager packed into a single binary. Manages millions of subscribers with templated campaigns, analytics, and a REST API for programmatic email automation.

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
clawhub install listmonk-self-hosted-newsletter-mailing-list
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Listmonk is a standalone, self-hosted newsletter and mailing list manager built in Go, delivered as a single binary with a PostgreSQL backend. Published under the AGPL-3.0 license with 15,000+ GitHub stars, it provides a fast, feature-rich alternative to Mailchimp, ConvertKit, and other commercial email marketing platforms — with complete data ownership and no per-subscriber pricing.
The platform handles the full email campaign lifecycle: subscriber management with custom attributes and segmentation, campaign creation with a rich HTML template editor, scheduling and throttled sending, bounce processing, click and open tracking, and analytics dashboards. It supports both newsletter broadcasts and transactional email via its REST API, making it suitable for both marketing and application-driven email workflows.
Listmonk is designed to handle scale efficiently. It can manage millions of subscribers with its sliding-window message queue that throttles delivery to respect SMTP provider rate limits. The platform supports multiple SMTP servers with round-robin distribution, enabling high-throughput sending across multiple email providers. Campaign templates use Go’s template engine with variables for personalization, conditional content blocks, and dynamic subscriber attributes.
The REST API enables programmatic subscriber management (create, update, query, segment), campaign creation and scheduling, list management, template CRUD, and analytics retrieval. This makes it straightforward for AI agents to automate email workflows: adding subscribers from form submissions, triggering campaigns based on events, segmenting lists based on behavior data, and generating campaign performance reports. The API uses standard JSON over HTTP with token-based authentication.
Installation options include a single Docker Compose file (docker compose up -d), direct binary download from GitHub releases, or package manager installation. The built-in web UI provides a modern dashboard for managing all operations visually. Listmonk supports internationalization, S3-compatible media storage for email assets, and webhook integrations for delivery events. The project was originally developed by Zerodha, India’s largest stock broker, for their own email infrastructure needs.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/listmonk-self-hosted-newsletter-mailing-list/)
