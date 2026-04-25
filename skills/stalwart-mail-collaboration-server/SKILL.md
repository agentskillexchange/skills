---
title: "Stalwart All-in-One Mail and Collaboration Server"
description: "Stalwart is an open-source mail and collaboration server written in Rust that provides JMAP, IMAP4, POP3, SMTP, CalDAV, CardDAV, and WebDAV support. It enables agents to deploy and manage self-hosted email infrastructure with built-in spam filtering, DKIM/DMARC/SPF authentication, and full calendar and contact synchronization."
verification: "security_reviewed"
source: "https://github.com/stalwartlabs/stalwart"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "stalwartlabs/stalwart"
  github_stars: 12164
---

# Stalwart All-in-One Mail and Collaboration Server

Stalwart is a comprehensive open-source mail and collaboration server written in Rust, designed to be secure, fast, robust, and scalable. It provides a unified platform for email, calendaring, contacts, and file storage through industry-standard protocols including JMAP, IMAP4rev2, POP3, SMTP, CalDAV, CardDAV, and WebDAV. Core Capabilities The server handles the complete email lifecycle with built-in DMARC, DKIM, SPF, and ARC support for message authentication, along with strong transport security through DANE, MTA-STS, and SMTP TLS reporting. Its spam and phishing filter includes LLM-driven filtering, statistical spam classification, DNS blocklist checking, and Pyzor collaborative filtering. Collaboration Features Beyond email, Stalwart provides CalDAV and JMAP for Calendars support for scheduling, CardDAV and JMAP for Contacts for address book management, and WebDAV with JMAP for File Storage for document sharing. All sharing features support fine-grained access controls via WebDAV ACL and JMAP Sharing. Deployment and Integration Stalwart supports pluggable storage backends including RocksDB, FoundationDB, PostgreSQL, MySQL, SQLite, and S3-compatible storage. Full-text search is available in 17 languages using built-in indexing or via Meilisearch, ElasticSearch, or OpenSearch. The server includes OpenID Connect authentication, OAuth 2.0 authorization, LDAP integration, two-factor authentication, and application passwords. Observability and Management The server provides OpenTelemetry and Prometheus metrics integration, webhooks for event-driven automation, a web-based administration dashboard with real-time monitoring, SMTP queue management, and DMARC/TLS-RPT report visualization. Cluster coordination supports Kafka, Redpanda, NATS, or Redis, with Kubernetes and Docker Swarm support for automated scaling. Agent Integration Points Agents can use Stalwart to provision and manage email accounts via its REST API, configure mail routing and filtering rules through Sieve scripting, manage calendars and contacts programmatically via CalDAV/CardDAV/JMAP, monitor server health through Prometheus metrics, and automate security configurations including TLS certificate provisioning with ACME.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/stalwart-mail-collaboration-server/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/stalwart-mail-collaboration-server
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/stalwart-mail-collaboration-server`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stalwart-mail-collaboration-server/)
