---
title: Radicale Self-Hosted CalDAV and CardDAV Server
description: Radicale is a small but capable CalDAV and CardDAV server maintained
  by the Kozea team. It implements the CalDAV (RFC 4791) and CardDAV (RFC 6352) protocols,
  allowing any compatible client to synchronize calendars, to-do lists, journal entries,
  and contacts with a self-hosted server. Zero-Config Design Radicale works out of
  the box with no complicated setup. Install it with pip install radicale , run python
  -m radicale , and the server starts accepting CalDAV and CardDAV connections. All
  data is stored on the filesystem in a plain folder structure, making backups and
  migrations trivial. Protocol Support The server handles events, todos, journal entries,
  and business cards through CalDAV, CardDAV, and plain HTTP. It is compatible with
  a wide range of clients including GNOME Calendar, Thunderbird, DAVx5 (Android),
  Apple Calendar and Contacts, Evolution, and many others. Security and Access Control
  Radicale supports authentication to limit access and can secure connections with
  TLS. Its rights management plugin system allows fine-grained control over who can
  read or write specific collections. Plugin Architecture The server is extensible
  through plugins for authentication backends, rights management, storage engines,
  and web interfaces. This makes it adaptable to environments ranging from a single-user
  Raspberry Pi setup to a multi-user team deployment. Agent Integration For AI agents
  and automation workflows, Radicale provides a standards-based CalDAV/CardDAV endpoint
  that can be queried and modified programmatically. Agents can create calendar events,
  manage contacts, read availability data, and synchronize scheduling information
  using any CalDAV/CardDAV client library such as caldav (Python), ical.js, or vdirsyncer.
  Project Status Radicale has over 4,500 GitHub stars, is licensed under GPL-3.0,
  and runs on Linux, macOS, BSD, and Windows. It is written in Python and available
  via PyPI. Documentation is hosted at radicale.org.
verification: security_reviewed
source: https://github.com/Kozea/Radicale
category:
- Calendar, Email &amp; Productivity
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: kozea/radicale
  github_stars: 4535
---

# Radicale Self-Hosted CalDAV and CardDAV Server

Radicale is a small but capable CalDAV and CardDAV server maintained by the Kozea team. It implements the CalDAV (RFC 4791) and CardDAV (RFC 6352) protocols, allowing any compatible client to synchronize calendars, to-do lists, journal entries, and contacts with a self-hosted server. Zero-Config Design Radicale works out of the box with no complicated setup. Install it with pip install radicale , run python -m radicale , and the server starts accepting CalDAV and CardDAV connections. All data is stored on the filesystem in a plain folder structure, making backups and migrations trivial. Protocol Support The server handles events, todos, journal entries, and business cards through CalDAV, CardDAV, and plain HTTP. It is compatible with a wide range of clients including GNOME Calendar, Thunderbird, DAVx5 (Android), Apple Calendar and Contacts, Evolution, and many others. Security and Access Control Radicale supports authentication to limit access and can secure connections with TLS. Its rights management plugin system allows fine-grained control over who can read or write specific collections. Plugin Architecture The server is extensible through plugins for authentication backends, rights management, storage engines, and web interfaces. This makes it adaptable to environments ranging from a single-user Raspberry Pi setup to a multi-user team deployment. Agent Integration For AI agents and automation workflows, Radicale provides a standards-based CalDAV/CardDAV endpoint that can be queried and modified programmatically. Agents can create calendar events, manage contacts, read availability data, and synchronize scheduling information using any CalDAV/CardDAV client library such as caldav (Python), ical.js, or vdirsyncer. Project Status Radicale has over 4,500 GitHub stars, is licensed under GPL-3.0, and runs on Linux, macOS, BSD, and Windows. It is written in Python and available via PyPI. Documentation is hosted at radicale.org.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/radicale-self-hosted-caldav-carddav-server/)
