---
name: "Extract structured data and attachments from raw email with MailParser"
slug: "extract-structured-data-and-attachments-from-raw-email-mailparser"
description: "Use MailParser when an agent receives raw RFC822 or MIME email and needs a normalized result with headers, text, HTML, addresses, and attachments. This is for email ingestion and handoff workflows, not for acting as a mailbox client or delivery platform."
github_stars: 1666
verification: "security_reviewed"
source: "https://github.com/nodemailer/mailparser"
author: "Andris Reinman"
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "nodemailer/mailparser"
  github_stars: 1666
  npm_package: "mailparser"
  npm_weekly_downloads: 13679456
---

# Extract structured data and attachments from raw email with MailParser

Use MailParser when an agent receives raw RFC822 or MIME email and needs a normalized result with headers, text, HTML, addresses, and attachments. This is for email ingestion and handoff workflows, not for acting as a mailbox client or delivery platform.

## Prerequisites

Node.js

## Installation

Use the upstream install or setup path that matches your environment:
- $ npm install mailparser

Requirements and caveats from upstream:
- Advanced email parser for Node.js. Everything is handled as a stream which should make it able to parse even very large messages (100MB+) with relatively low overhead.
- const mailparser = require('mailparser');

Basic usage or getting-started notes:
- This module is in maintenance mode. It will continue to receive security updates and critical bug fixes, but no new features or feature changes will be added. For new projects, please consider using [PostalMime](https...
- First install the module from npm:
- next import the mailparser object into your script:

- Source: https://github.com/nodemailer/mailparser
- Extracted from upstream docs: https://raw.githubusercontent.com/nodemailer/mailparser/HEAD/README.md

## Documentation

- https://github.com/nodemailer/mailparser#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-structured-data-and-attachments-from-raw-email-mailparser/)
