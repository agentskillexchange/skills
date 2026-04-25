---
title: "MailDev SMTP Capture and Email Testing Server"
description: "MailDev is a local SMTP server with a web UI and REST API for capturing application email during development. It lets agents and test workflows inspect messages, attachments, and relay behavior without touching real inboxes."
verification: "security_reviewed"
source: "https://github.com/maildev/maildev"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "maildev/maildev"
  github_stars: 5892
---

# MailDev SMTP Capture and Email Testing Server

MailDev is an open source SMTP capture server designed for development and test environments. It listens on a local SMTP port, collects outgoing mail, and exposes the messages through a browser-based interface and a programmable API. That makes it a practical fit for agent-driven QA, integration testing, and product workflows where email output needs to be inspected but should not be delivered to real users. The upstream project supports both CLI and embedded Node.js usage. The simplest installation path is npm install -g maildev, followed by running maildev or starting its Docker image. By default it exposes an SMTP listener and a web interface, and it also supports outgoing relay settings, persistence directories, authentication options, and REST-based inspection. The repository documents how to run it in Node code via const MailDev = require("maildev") as well as how to wire it into automated test flows. For ASE, MailDev maps cleanly to jobs such as previewing transactional messages, validating password reset flows, checking generated HTML email, and asserting that an agent-triggered automation sent the right message to the right recipient. A skill for MailDev can wrap startup, polling the REST endpoints for captured messages, downloading MIME content, and optionally forwarding approved test messages through a configured relay. Because it is lightweight and well-known in the Node ecosystem, it is a solid building block for development-focused email workflows across multiple agent frameworks.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/maildev-smtp-capture-and-email-testing-server/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/maildev-smtp-capture-and-email-testing-server
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/maildev-smtp-capture-and-email-testing-server`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/maildev-smtp-capture-and-email-testing-server/)
