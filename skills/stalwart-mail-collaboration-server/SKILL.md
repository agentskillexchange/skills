---
title: "Stalwart All-in-One Mail and Collaboration Server"
description: "Stalwart is a comprehensive open-source mail and collaboration server written in Rust, designed to be secure, fast, robust, and scalable. It provides a unified platform for email, calendaring, contacts, and file storage through industry-standard protocols including JMAP, IMAP4rev2, POP3, SMTP, CalDAV, CardDAV, and WebDAV. Core Capabilities The server handles the complete email lifecycle with built-in DMARC, DKIM, SPF, and ARC support for message authentication, along with strong transport security through DANE, MTA-STS, and SMTP TLS reporting. Its spam and phishing filter includes LLM-driven filtering, statistical spam classification, DNS blocklist checking, and Pyzor collaborative filtering. Collaboration Features Beyond email, Stalwart provides CalDAV and JMAP for Calendars support for scheduling, CardDAV and JMAP for Contacts for address book management, and WebDAV with JMAP for File Storage for document sharing. All sharing features support fine-grained access controls via WebDAV ACL and JMAP Sharing. Deployment and Integration Stalwart supports pluggable storage backends including RocksDB, FoundationDB, PostgreSQL, MySQL, SQLite, and S3-compatible storage. Full-text search is available in 17 languages using built-in indexing or via Meilisearch, ElasticSearch, or OpenSearch. The server includes OpenID Connect authentication, OAuth 2.0 authorization, LDAP integration, two-factor authentication, and application passwords. Observability and Management The server provides OpenTelemetry and Prometheus metrics integration, webhooks for event-driven automation, a web-based administration dashboard with real-time monitoring, SMTP queue management, and DMARC/TLS-RPT report visualization. Cluster coordination supports Kafka, Redpanda, NATS, or Redis, with Kubernetes and Docker Swarm support for automated scaling. Agent Integration Points Agents can use Stalwart to provision and manage email accounts via its REST API, configure mail routing and filtering rules through Sieve scripting, manage calendars and contacts programmatically via CalDAV/CardDAV/JMAP, monitor server health through Prometheus metrics, and automate security configurations including TLS certificate provisioning with ACME."
source: "https://github.com/stalwartlabs/stalwart"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "stalwartlabs/stalwart"
  github_stars: 12164
---

# Stalwart All-in-One Mail and Collaboration Server

Stalwart is a comprehensive open-source mail and collaboration server written in Rust, designed to be secure, fast, robust, and scalable. It provides a unified platform for email, calendaring, contacts, and file storage through industry-standard protocols including JMAP, IMAP4rev2, POP3, SMTP, CalDAV, CardDAV, and WebDAV. Core Capabilities The server handles the complete email lifecycle with built-in DMARC, DKIM, SPF, and ARC support for message authentication, along with strong transport security through DANE, MTA-STS, and SMTP TLS reporting. Its spam and phishing filter includes LLM-driven filtering, statistical spam classification, DNS blocklist checking, and Pyzor collaborative filtering. Collaboration Features Beyond email, Stalwart provides CalDAV and JMAP for Calendars support for scheduling, CardDAV and JMAP for Contacts for address book management, and WebDAV with JMAP for File Storage for document sharing. All sharing features support fine-grained access controls via WebDAV ACL and JMAP Sharing. Deployment and Integration Stalwart supports pluggable storage backends including RocksDB, FoundationDB, PostgreSQL, MySQL, SQLite, and S3-compatible storage. Full-text search is available in 17 languages using built-in indexing or via Meilisearch, ElasticSearch, or OpenSearch. The server includes OpenID Connect authentication, OAuth 2.0 authorization, LDAP integration, two-factor authentication, and application passwords. Observability and Management The server provides OpenTelemetry and Prometheus metrics integration, webhooks for event-driven automation, a web-based administration dashboard with real-time monitoring, SMTP queue management, and DMARC/TLS-RPT report visualization. Cluster coordination supports Kafka, Redpanda, NATS, or Redis, with Kubernetes and Docker Swarm support for automated scaling. Agent Integration Points Agents can use Stalwart to provision and manage email accounts via its REST API, configure mail routing and filtering rules through Sieve scripting, manage calendars and contacts programmatically via CalDAV/CardDAV/JMAP, monitor server health through Prometheus metrics, and automate security configurations including TLS certificate provisioning with ACME.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stalwart-mail-collaboration-server/)
