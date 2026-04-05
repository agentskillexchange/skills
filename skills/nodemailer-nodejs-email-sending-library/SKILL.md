---
name: "Nodemailer Node.js Email Sending Library with SMTP and Transport Support"
description: "Nodemailer is the most widely used Node.js library for sending emails, with 17k+ GitHub stars and 7 million weekly npm downloads. It supports SMTP, OAuth2, HTML content, attachments, embedded images, and custom transports for services like SES and SendGrid."
category: "Calendar, Email &amp; Productivity"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/nodemailer/nodemailer"
---
# Nodemailer Node.js Email Sending Library with SMTP and Transport Support

Nodemailer is the most widely used Node.js library for sending emails, with 17k+ GitHub stars and 7 million weekly npm downloads. It supports SMTP, OAuth2, HTML content, attachments, embedded images, and custom transports for services like SES and SendGrid.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nodemailer-nodejs-email-sending-library
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nodemailer-nodejs-email-sending-library -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nodemailer-nodejs-email-sending-library -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nodemailer-nodejs-email-sending-library -a codex
```

### OpenClaw

```bash
clawhub install nodemailer-nodejs-email-sending-library
```

## Details

Nodemailer is the standard email sending library for Node.js applications. With over 17,000 GitHub stars and 7 million weekly downloads on npm, it is the most widely adopted solution for programmatic email delivery in the JavaScript ecosystem. Licensed under MIT No Attribution (MIT-0), it can be used freely in any project.

How It Works
Nodemailer creates a transporter object configured with SMTP server details (host, port, authentication), then uses that transporter to send messages. A basic send requires only a from address, to address, subject, and body (plain text or HTML). The library handles SMTP connection pooling, TLS negotiation, and authentication automatically.

Transport Options
The built-in SMTP transport works with any standard mail server. For cloud email services, Nodemailer supports custom transports — community packages exist for Amazon SES, SendGrid, Mailgun, Postmark, and others. OAuth2 authentication is supported natively for Gmail and Microsoft 365 accounts, handling token refresh automatically. A JSON transport is available for testing, outputting messages as JSON objects instead of sending them.

Message Features
Messages can include HTML content with inline CSS, plain text fallbacks, file attachments (from buffers, streams, or file paths), embedded images referenced by Content-ID, calendar events (iCalendar), and custom headers. The address parser handles display names, groups, and multiple recipients. DKIM signing can be configured to authenticate outgoing messages.

Agent Integration
For AI agents that need to send emails as part of their workflows, Nodemailer provides the transport layer. Common agent use cases include sending notification emails when tasks complete, delivering reports as attachments, forwarding summaries to stakeholders, or implementing email-based approval workflows. The straightforward API makes it easy to wrap in a skill or tool function that agents can call with structured parameters.

Configuration and Debugging
Nodemailer includes built-in debug logging that traces the full SMTP conversation. The verify() method tests server connectivity without sending a message. Connection timeouts, TLS versions, and socket options are all configurable. For development, it integrates with Ethereal.email to generate test accounts that capture messages in a web inbox without delivering them.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nodemailer-nodejs-email-sending-library/)
