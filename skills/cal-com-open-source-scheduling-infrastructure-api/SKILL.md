---
name: "Cal.com Open Source Scheduling Infrastructure and API"
description: "Integrate Cal.com’s open-source scheduling platform into AI agent workflows. Agents can programmatically create event types, check availability, book meetings, and manage scheduling infrastructure through Cal.com’s comprehensive REST API."
category: "Calendar, Email &amp; Productivity"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/calcom/cal.com"
tool_ecosystem:
  github_repo: "calcom/cal.com"
  github_stars: 40908
---
# Cal.com Open Source Scheduling Infrastructure and API

Integrate Cal.com’s open-source scheduling platform into AI agent workflows. Agents can programmatically create event types, check availability, book meetings, and manage scheduling infrastructure through Cal.com’s comprehensive REST API.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cal-com-open-source-scheduling-infrastructure-api
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cal-com-open-source-scheduling-infrastructure-api -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cal-com-open-source-scheduling-infrastructure-api -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cal-com-open-source-scheduling-infrastructure-api -a codex
```

### OpenClaw

```bash
clawhub install cal-com-open-source-scheduling-infrastructure-api
```

## Details

Cal.com is the leading open-source alternative to Calendly, providing scheduling infrastructure for individuals, businesses, and developers building scheduling platforms. With over 40,000 GitHub stars and an active contributor community, Cal.com offers a fully self-hostable, API-first scheduling engine that AI agents can integrate with directly.

What This Skill Enables
An agent skill built around Cal.com allows AI agents to manage the entire scheduling lifecycle programmatically. Through Cal.com’s REST API (api.cal.com), agents can create and configure event types with custom durations, locations, and booking questions. They can query real-time availability across connected calendars (Google Calendar, Outlook, Apple Calendar), propose optimal meeting times, and create bookings on behalf of users.

Core Capabilities
The Cal.com API exposes endpoints for event type management, booking creation and cancellation, availability queries, webhook subscriptions, and team scheduling. Agents can automate complex scheduling workflows like round-robin assignment, collective scheduling where multiple team members must be available, and managed event types across an organization. The platform supports OAuth2 authentication and API key access for programmatic integration.

Integration Points
Cal.com integrates natively with Google Calendar, Microsoft Outlook, Apple Calendar, Zoom, Google Meet, Microsoft Teams, Stripe for paid bookings, and dozens of other services. Agents can leverage these integrations to coordinate across calendar providers, automatically set up video conferencing links, and process payments for consultation bookings. Webhooks enable real-time event-driven workflows when bookings are created, rescheduled, or cancelled.

Technical Details
The platform is built with Next.js and TypeScript in a Turborepo monorepo. It can be self-hosted via Docker or deployed on any Node.js hosting platform. The API follows RESTful conventions with JSON request/response formats. Rate limiting, pagination, and filtering are supported across all list endpoints. The cal.com npm packages (@calcom/embed-react, @calcom/embed-core) allow embedding scheduling widgets directly into applications.

Use Cases
AI agents can use this skill to build intelligent scheduling assistants that understand natural language requests like “schedule a 30-minute call with the design team next Tuesday afternoon” and translate them into Cal.com API calls. Agents can also monitor booking patterns, suggest optimal meeting times based on historical data, and automate rescheduling when conflicts arise.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cal-com-open-source-scheduling-infrastructure-api/)
