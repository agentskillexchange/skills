---
title: "Nylas Platform SDK for Unified Email Calendar and Contacts API"
description: "The Nylas platform provides a single set of REST APIs that abstract away the complexity of connecting to email, calendar, and contacts providers. Instead of building and maintaining separate integrations for Gmail, Microsoft Outlook, Exchange, Yahoo, and IMAP providers, developers use the Nylas SDK to interact with a unified API that handles provider-specific differences behind the scenes. How It Works Nylas acts as a middleware layer between your application and email/calendar providers. After authenticating a user through Nylas OAuth flow, you receive a grant ID that represents access to that user&#8217;s mailbox and calendar. All subsequent API calls use this grant ID to read, create, update, or delete emails, events, and contacts. The SDKs are available for Python ( pip install nylas ) and Node.js ( npm install nylas ), with full TypeScript support. Key Capabilities Unified Email API: Read threads, send messages, manage drafts, handle attachments, and search across all connected email providers through a single API. Calendar Management: Create, read, update, and delete events. Check free/busy availability across multiple calendars. Handle recurring events and RSVPs. Contacts Access: Read and manage contact records across connected providers. Real-time Webhooks: Receive notifications when new emails arrive, calendar events change, or contacts are updated. Provider Abstraction: Handles the differences between Google APIs, Microsoft Graph, Exchange EWS, and IMAP/SMTP protocols transparently. Integration Points The Python SDK uses dataclasses for type-safe request and response handling. Standard CRUD operations are available on each resource: nylas.calendars.list() , nylas.events.create() , nylas.messages.find() , etc. The Node.js SDK follows similar patterns with full TypeScript type definitions. Both SDKs support Nylas API v3 with OAuth 2.0 authentication flows. Agent Use Cases Email triage agents can read incoming messages, classify them, and draft responses using the unified email API. Calendar scheduling agents can check availability across multiple users and create meetings. Productivity agents can monitor for new emails matching specific criteria and trigger automated workflows. Contact enrichment agents can pull and update contact information across providers. The webhook system enables event-driven agent architectures that react to email and calendar changes in real time."
source: "https://github.com/nylas/nylas-python"
verification: "security_reviewed"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "nylas/nylas-python"
  github_stars: 106
---

# Nylas Platform SDK for Unified Email Calendar and Contacts API

The Nylas platform provides a single set of REST APIs that abstract away the complexity of connecting to email, calendar, and contacts providers. Instead of building and maintaining separate integrations for Gmail, Microsoft Outlook, Exchange, Yahoo, and IMAP providers, developers use the Nylas SDK to interact with a unified API that handles provider-specific differences behind the scenes. How It Works Nylas acts as a middleware layer between your application and email/calendar providers. After authenticating a user through Nylas OAuth flow, you receive a grant ID that represents access to that user&#8217;s mailbox and calendar. All subsequent API calls use this grant ID to read, create, update, or delete emails, events, and contacts. The SDKs are available for Python ( pip install nylas ) and Node.js ( npm install nylas ), with full TypeScript support. Key Capabilities Unified Email API: Read threads, send messages, manage drafts, handle attachments, and search across all connected email providers through a single API. Calendar Management: Create, read, update, and delete events. Check free/busy availability across multiple calendars. Handle recurring events and RSVPs. Contacts Access: Read and manage contact records across connected providers. Real-time Webhooks: Receive notifications when new emails arrive, calendar events change, or contacts are updated. Provider Abstraction: Handles the differences between Google APIs, Microsoft Graph, Exchange EWS, and IMAP/SMTP protocols transparently. Integration Points The Python SDK uses dataclasses for type-safe request and response handling. Standard CRUD operations are available on each resource: nylas.calendars.list() , nylas.events.create() , nylas.messages.find() , etc. The Node.js SDK follows similar patterns with full TypeScript type definitions. Both SDKs support Nylas API v3 with OAuth 2.0 authentication flows. Agent Use Cases Email triage agents can read incoming messages, classify them, and draft responses using the unified email API. Calendar scheduling agents can check availability across multiple users and create meetings. Productivity agents can monitor for new emails matching specific criteria and trigger automated workflows. Contact enrichment agents can pull and update contact information across providers. The webhook system enables event-driven agent architectures that react to email and calendar changes in real time.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nylas-sdk-email-calendar-contacts/)
