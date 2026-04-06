---
name: "Stalwart All-in-One Mail and Collaboration Server"
description: "Stalwart is an open-source mail and collaboration server written in Rust that provides JMAP, IMAP4, POP3, SMTP, CalDAV, CardDAV, and WebDAV support. It enables agents to deploy and manage self-hosted email infrastructure with built-in spam filtering, DKIM/DMARC/SPF authentication, and full calendar and contact synchronization."
category: "Calendar, Email &amp; Productivity"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/stalwartlabs/stalwart"
tool_ecosystem:
  github_repo: "https://github.com/stalwartlabs/stalwart"
  github_stars: 12164
---
# Stalwart All-in-One Mail and Collaboration Server

Stalwart is an open-source mail and collaboration server written in Rust that provides JMAP, IMAP4, POP3, SMTP, CalDAV, CardDAV, and WebDAV support. It enables agents to deploy and manage self-hosted email infrastructure with built-in spam filtering, DKIM/DMARC/SPF authentication, and full calendar and contact synchronization.

Stalwart is a comprehensive open-source mail and collaboration server written in Rust, designed to be secure, fast, robust, and scalable. It provides a unified platform for email, calendaring, contacts, and file storage through industry-standard protocols including JMAP, IMAP4rev2, POP3, SMTP, CalDAV, CardDAV, and WebDAV.

Core Capabilities

The server handles the complete email lifecycle with built-in DMARC, DKIM, SPF, and ARC support for message authentication, along with strong transport security through DANE, MTA-STS, and SMTP TLS reporting. Its spam and phishing filter includes LLM-driven filtering, statistical spam classification, DNS blocklist checking, and Pyzor collaborative filtering.

Collaboration Features

Beyond email, Stalwart provides CalDAV and JMAP for Calendars support for scheduling, CardDAV and JMAP for Contacts for address book management, and WebDAV with JMAP for File Storage for document sharing. All sharing features support fine-grained access controls via WebDAV ACL and JMAP Sharing.

Deployment and Integration

Stalwart supports pluggable storage backends including RocksDB, FoundationDB, PostgreSQL, MySQL, SQLite, and S3-compatible storage. Full-text search is available in 17 languages using built-in indexing or via Meilisearch, ElasticSearch, or OpenSearch. The server includes OpenID Connect authentication, OAuth 2.0 authorization, LDAP integration, two-factor authentication, and application passwords.

Observability and Management

The server provides OpenTelemetry and Prometheus metrics integration, webhooks for event-driven automation, a web-based administration dashboard with real-time monitoring, SMTP queue management, and DMARC/TLS-RPT report visualization. Cluster coordination supports Kafka, Redpanda, NATS, or Redis, with Kubernetes and Docker Swarm support for automated scaling.

Agent Integration Points

Agents can use Stalwart to provision and manage email accounts via its REST API, configure mail routing and filtering rules through Sieve scripting, manage calendars and contacts programmatically via CalDAV/CardDAV/JMAP, monitor server health through Prometheus metrics, and automate security configurations including TLS certificate provisioning with ACME.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stalwart-mail-collaboration-server
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stalwart-mail-collaboration-server -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stalwart-mail-collaboration-server -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stalwart-mail-collaboration-server -a codex
```

### OpenClaw

```bash
clawhub install stalwart-mail-collaboration-server
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stalwart-mail-collaboration-server/)
