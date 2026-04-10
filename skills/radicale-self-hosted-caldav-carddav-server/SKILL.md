---
title: "Radicale Self-Hosted CalDAV and CardDAV Server"
description: "Radicale is a lightweight, self-hosted CalDAV and CardDAV server written in Python. It shares calendars, to-do lists, journal entries, and contacts over standard protocols with zero-config setup, file-based storage, optional authentication, TLS support, and a plugin architecture."
slug: "radicale-self-hosted-caldav-carddav-server"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/Kozea/Radicale"
listed: true
---

# Radicale Self-Hosted CalDAV and CardDAV Server

Radicale is a lightweight, self-hosted CalDAV and CardDAV server written in Python. It shares calendars, to-do lists, journal entries, and contacts over standard protocols with zero-config setup, file-based storage, optional authentication, TLS support, and a plugin architecture.

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
clawhub install radicale-self-hosted-caldav-carddav-server
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Radicale is a small but capable CalDAV and CardDAV server maintained by the Kozea team. It implements the CalDAV (RFC 4791) and CardDAV (RFC 6352) protocols, allowing any compatible client to synchronize calendars, to-do lists, journal entries, and contacts with a self-hosted server.
Zero-Config Design
Radicale works out of the box with no complicated setup. Install it with pip install radicale, run python -m radicale, and the server starts accepting CalDAV and CardDAV connections. All data is stored on the filesystem in a plain folder structure, making backups and migrations trivial.
Protocol Support
The server handles events, todos, journal entries, and business cards through CalDAV, CardDAV, and plain HTTP. It is compatible with a wide range of clients including GNOME Calendar, Thunderbird, DAVx5 (Android), Apple Calendar and Contacts, Evolution, and many others.
Security and Access Control
Radicale supports authentication to limit access and can secure connections with TLS. Its rights management plugin system allows fine-grained control over who can read or write specific collections.
Plugin Architecture
The server is extensible through plugins for authentication backends, rights management, storage engines, and web interfaces. This makes it adaptable to environments ranging from a single-user Raspberry Pi setup to a multi-user team deployment.
Agent Integration
For AI agents and automation workflows, Radicale provides a standards-based CalDAV/CardDAV endpoint that can be queried and modified programmatically. Agents can create calendar events, manage contacts, read availability data, and synchronize scheduling information using any CalDAV/CardDAV client library such as caldav (Python), ical.js, or vdirsyncer.
Project Status
Radicale has over 4,500 GitHub stars, is licensed under GPL-3.0, and runs on Linux, macOS, BSD, and Windows. It is written in Python and available via PyPI. Documentation is hosted at radicale.org.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/radicale-self-hosted-caldav-carddav-server/)
