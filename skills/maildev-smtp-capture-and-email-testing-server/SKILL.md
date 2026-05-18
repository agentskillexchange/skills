---
name: "MailDev SMTP Capture and Email Testing Server"
slug: "maildev-smtp-capture-and-email-testing-server"
description: "MailDev is a local SMTP server with a web UI and REST API for capturing application email during development. It lets agents and test workflows inspect messages, attachments, and relay behavior without touching real inboxes."
github_stars: 5892
verification: "security_reviewed"
source: "https://github.com/maildev/maildev"
author: "maildev"
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "maildev/maildev"
  github_stars: 5892
---

# MailDev SMTP Capture and Email Testing Server

MailDev is a local SMTP server with a web UI and REST API for capturing application email during development. It lets agents and test workflows inspect messages, attachments, and relay behavior without touching real inboxes.

## Installation

Use the upstream install or setup path that matches your environment:
- $ docker run -p 1080:1080 -p 1025:1025 maildev/maildev
- npm install
- npm run dev
- To lint your code before submitting your PR, run npm run lint.

Requirements and caveats from upstream:
- [![Docker Pulls](https://img.shields.io/docker/pulls/maildev/maildev)](https://hub.docker.com/r/maildev/maildev)
- **MailDev** is a simple way to test your project's generated email during development, with an easy to use web interface that runs on your machine built on top of [Node.js](http://www.nodejs.org).
- ## Docker Run

Basic usage or getting-started notes:
- | Options | Environment variable | Description |
- | -------------------------------- | -------------------------- | ----------------------------------------------------------------------------------------- |
- | -s, --smtp <port> | MAILDEV_SMTP_PORT | SMTP port to catch mail |

- Source: https://github.com/maildev/maildev
- Extracted from upstream docs: https://raw.githubusercontent.com/maildev/maildev/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/maildev-smtp-capture-and-email-testing-server/)
