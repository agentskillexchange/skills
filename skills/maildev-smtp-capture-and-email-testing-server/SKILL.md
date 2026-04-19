---
title: "MailDev SMTP Capture and Email Testing Server"
description: "MailDev is an open source SMTP capture server designed for development and test environments. It listens on a local SMTP port, collects outgoing mail, and exposes the messages through a browser-based interface and a programmable API. That makes it a practical fit for agent-driven QA, integration testing, and product workflows where email output needs to be inspected but should not be delivered to real users. The upstream project supports both CLI and embedded Node.js usage. The simplest installation path is npm install -g maildev , followed by running maildev or starting its Docker image. By default it exposes an SMTP listener and a web interface, and it also supports outgoing relay settings, persistence directories, authentication options, and REST-based inspection. The repository documents how to run it in Node code via const MailDev = require(\"maildev\") as well as how to wire it into automated test flows. For ASE, MailDev maps cleanly to jobs such as previewing transactional messages, validating password reset flows, checking generated HTML email, and asserting that an agent-triggered automation sent the right message to the right recipient. A skill for MailDev can wrap startup, polling the REST endpoints for captured messages, downloading MIME content, and optionally forwarding approved test messages through a configured relay. Because it is lightweight and well-known in the Node ecosystem, it is a solid building block for development-focused email workflows across multiple agent frameworks."
source: "https://github.com/maildev/maildev"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "maildev/maildev"
  github_stars: 5892
---

# MailDev SMTP Capture and Email Testing Server

MailDev is an open source SMTP capture server designed for development and test environments. It listens on a local SMTP port, collects outgoing mail, and exposes the messages through a browser-based interface and a programmable API. That makes it a practical fit for agent-driven QA, integration testing, and product workflows where email output needs to be inspected but should not be delivered to real users. The upstream project supports both CLI and embedded Node.js usage. The simplest installation path is npm install -g maildev , followed by running maildev or starting its Docker image. By default it exposes an SMTP listener and a web interface, and it also supports outgoing relay settings, persistence directories, authentication options, and REST-based inspection. The repository documents how to run it in Node code via const MailDev = require("maildev") as well as how to wire it into automated test flows. For ASE, MailDev maps cleanly to jobs such as previewing transactional messages, validating password reset flows, checking generated HTML email, and asserting that an agent-triggered automation sent the right message to the right recipient. A skill for MailDev can wrap startup, polling the REST endpoints for captured messages, downloading MIME content, and optionally forwarding approved test messages through a configured relay. Because it is lightweight and well-known in the Node ecosystem, it is a solid building block for development-focused email workflows across multiple agent frameworks.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/maildev-smtp-capture-and-email-testing-server/)
