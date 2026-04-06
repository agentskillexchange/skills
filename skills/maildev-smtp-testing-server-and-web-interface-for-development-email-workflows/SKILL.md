---
name: "MailDev SMTP Testing Server and Web Interface for Development Email Workflows"
description: "MailDev is a local SMTP server with a browser UI for viewing test emails during development. It catches outgoing mail, exposes a REST API, supports attachments and relay options, and helps teams test email flows without sending real messages to customers."
category: "Calendar, Email &amp; Productivity"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/maildev/maildev"
---
# MailDev SMTP Testing Server and Web Interface for Development Email Workflows

MailDev is a local SMTP server with a browser UI for viewing test emails during development. It catches outgoing mail, exposes a REST API, supports attachments and relay options, and helps teams test email flows without sending real messages to customers.

MailDev is an open source SMTP testing server designed for development environments where teams need to inspect generated email safely before anything reaches a real inbox. Instead of pointing an application at a live SMTP provider while building password resets, invitations, order confirmations, or system alerts, developers can point it at MailDev and review the captured messages in a local web interface. That makes it a practical fit for agents, internal tools, or CI setups that need repeatable email verification.

The project combines several jobs-to-be-done in one package: capture outgoing mail on a local SMTP port, display the rendered HTML and plain-text bodies in a browser, expose message data through an API, and optionally relay selected messages upstream when needed. The README also documents Docker usage, attachment viewing, resizable previews for responsive testing, and command-line configuration for SMTP and web interface ports. Because it runs on Node.js and keeps the setup lightweight, it is easy to drop into app development workflows.

MailDev integrates well with common application stacks because it behaves like a normal SMTP target. The upstream docs include examples for Node.js applications and reference configurations for frameworks such as Django, Rails, Drupal, and Spring Boot. For teams building agent-driven QA or development assistants, MailDev is especially useful as a safe mail sink that lets an automated workflow validate subject lines, body content, links, and headers without touching production delivery infrastructure.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill maildev-smtp-testing-server-and-web-interface-for-development-email-workflows
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill maildev-smtp-testing-server-and-web-interface-for-development-email-workflows -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill maildev-smtp-testing-server-and-web-interface-for-development-email-workflows -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill maildev-smtp-testing-server-and-web-interface-for-development-email-workflows -a codex
```

### OpenClaw

```bash
clawhub install maildev-smtp-testing-server-and-web-interface-for-development-email-workflows
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/maildev-smtp-testing-server-and-web-interface-for-development-email-workflows/)
