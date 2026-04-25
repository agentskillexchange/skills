---
title: "Extract structured data and attachments from raw email with MailParser"
description: "Use MailParser when an agent receives raw RFC822 or MIME email and needs a normalized result with headers, text, HTML, addresses, and attachments. This is for email ingestion and handoff workflows, not for acting as a mailbox client or delivery platform."
verification: "security_reviewed"
source: "https://github.com/nodemailer/mailparser"
category:
  - "Calendar, Email & Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "nodemailer/mailparser"
  github_stars: 1666
---

# Extract structured data and attachments from raw email with MailParser

Tool used: MailParser from the Nodemailer project (nodemailer/mailparser). This skill gives an agent a clear job: take a raw email message, parse it into structured fields, and hand the result to downstream automation. That means extracting sender and recipient metadata, subject, timestamps, plain text, HTML bodies, inline references, and attachments in a form another workflow can trust. The agent behavior is practical: normalize messy inbound email into data that can be indexed, summarized, classified, stored, or routed. Invoke this skill when the input is an actual raw message source such as an .eml file, a webhook payload containing MIME content, a forwarded support message, or a mailbox export that needs machine processing. This is the moment when “just open the email app” stops being enough. A user uses the product normally to read or send mail. An agent uses this skill when the job is to convert transport-level email data into structured artifacts for another system. The scope boundary is what keeps this entry out of generic SDK territory. MailParser does not send email, manage campaigns, sync inboxes, or replace an email provider. It parses raw messages. That bounded behavior makes it a real skill-shaped building block for ticket ingestion, attachment extraction, compliance archiving, lead intake, and mailbox-to-database pipelines. Integration points include SMTP capture tools, inbound email webhooks, help desk ingestion flows, storage systems, and LLM summarization or classification steps that depend on clean message structure first.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/extract-structured-data-and-attachments-from-raw-email-mailparser/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/extract-structured-data-and-attachments-from-raw-email-mailparser
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/extract-structured-data-and-attachments-from-raw-email-mailparser`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/extract-structured-data-and-attachments-from-raw-email-mailparser/)
