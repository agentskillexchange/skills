---
name: "Nylas Platform SDK for Unified Email Calendar and Contacts API"
description: "Nylas provides REST APIs and SDKs for Python and Node.js that offer unified access to email, calendar, and contacts across all major providers including Gmail, Outlook, and Exchange. Build email and scheduling integrations without managing individual provider APIs."
category: "Calendar, Email & Productivity"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/nylas/nylas-python"
---
# Nylas Platform SDK for Unified Email Calendar and Contacts API

Nylas provides REST APIs and SDKs for Python and Node.js that offer unified access to email, calendar, and contacts across all major providers including Gmail, Outlook, and Exchange. Build email and scheduling integrations without managing individual provider APIs.

## Overview

The Nylas platform provides a single set of REST APIs that abstract away the complexity of connecting to email, calendar, and contacts providers. Instead of building and maintaining separate integrations for Gmail, Microsoft Outlook, Exchange, Yahoo, and IMAP providers, developers use the Nylas SDK to interact with a unified API that handles provider-specific differences behind the scenes.

How It Works

Nylas acts as a middleware layer between your application and email/calendar providers. After authenticating a user through Nylas OAuth flow, you receive a grant ID that represents access to that user’s mailbox and calendar. All subsequent API calls use this grant ID to read, create, update, or delete emails, events, and contacts. The SDKs are available for Python (`pip install nylas`) and Node.js (`npm install nylas`), with full TypeScript support.

Key Capabilities

- Unified Email API: Read threads, send messages, manage drafts, handle attachments, and search across all connected email providers through a single API.

- Calendar Management: Create, read, update, and delete events. Check free/busy availability across multiple calendars. Handle recurring events and RSVPs.

- Contacts Access: Read and manage contact records across connected providers.

- Real-time Webhooks: Receive notifications when new emails arrive, calendar events change, or contacts are updated.

- Provider Abstraction: Handles the differences between Google APIs, Microsoft Graph, Exchange EWS, and IMAP/SMTP protocols transparently.

Integration Points

The Python SDK uses dataclasses for type-safe request and response handling. Standard CRUD operations are available on each resource: `nylas.calendars.list()`, `nylas.events.create()`, `nylas.messages.find()`, etc. The Node.js SDK follows similar patterns with full TypeScript type definitions. Both SDKs support Nylas API v3 with OAuth 2.0 authentication flows.

Agent Use Cases

Email triage agents can read incoming messages, classify them, and draft responses using the unified email API. Calendar scheduling agents can check availability across multiple users and create meetings. Productivity agents can monitor for new emails matching specific criteria and trigger automated workflows. Contact enrichment agents can pull and update contact information across providers. The webhook system enables event-driven agent architectures that react to email and calendar changes in real time.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill nylas-sdk-email-calendar-contacts
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill nylas-sdk-email-calendar-contacts -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill nylas-sdk-email-calendar-contacts -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill nylas-sdk-email-calendar-contacts -a codex
```

### OpenClaw

```bash
clawhub install nylas-sdk-email-calendar-contacts
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nylas-sdk-email-calendar-contacts/)
