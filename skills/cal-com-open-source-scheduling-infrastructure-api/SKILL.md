---
name: Cal.com Open Source Scheduling Infrastructure and API
description: Integrate Cal.com&#8217;s open-source scheduling platform into AI agent
  workflows. Agents can programmatically create event types, check availability, book
  meetings, and manage scheduling infrastructure through Cal.com&#8217;s comprehensive
  REST API.
verification: security_reviewed
source: https://github.com/calcom/cal.com
category:
- Calendar, Email &amp; Productivity
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: calcom/cal.com
  github_stars: 40908
---
# Cal.com Open Source Scheduling Infrastructure and API

Cal.com is the leading open-source alternative to Calendly, providing scheduling infrastructure for individuals, businesses, and developers building scheduling platforms. With over 40,000 GitHub stars and an active contributor community, Cal.com offers a fully self-hostable, API-first scheduling engine that AI agents can integrate with directly.
What This Skill Enables
An agent skill built around Cal.com allows AI agents to manage the entire scheduling lifecycle programmatically. Through Cal.com's REST API (api.cal.com), agents can create and configure event types with custom durations, locations, and booking questions. They can query real-time availability across connected calendars (Google Calendar, Outlook, Apple Calendar), propose optimal meeting times, and create bookings on behalf of users.
Core Capabilities
The Cal.com API exposes endpoints for event type management, booking creation and cancellation, availability queries, webhook subscriptions, and team scheduling. Agents can automate complex scheduling workflows like round-robin assignment, collective scheduling where multiple team members must be available, and managed event types across an organization. The platform supports OAuth2 authentication and API key access for programmatic integration.
Integration Points
Cal.com integrates natively with Google Calendar, Microsoft Outlook, Apple Calendar, Zoom, Google Meet, Microsoft Teams, Stripe for paid bookings, and dozens of other services. Agents can leverage these integrations to coordinate across calendar providers, automatically set up video conferencing links, and process payments for consultation bookings. Webhooks enable real-time event-driven workflows when bookings are created, rescheduled, or cancelled.
Technical Details
The platform is built with Next.js and TypeScript in a Turborepo monorepo. It can be self-hosted via Docker or deployed on any Node.js hosting platform. The API follows RESTful conventions with JSON request/response formats. Rate limiting, pagination, and filtering are supported across all list endpoints. The cal.com npm packages (@calcom/embed-react, @calcom/embed-core) allow embedding scheduling widgets directly into applications.
Use Cases
AI agents can use this skill to build intelligent scheduling assistants that understand natural language requests like &#8220;schedule a 30-minute call with the design team next Tuesday afternoon&#8221; and translate them into Cal.com API calls. Agents can also monitor booking patterns, suggest optimal meeting times based on historical data, and automate rescheduling when conflicts arise.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cal-com-open-source-scheduling-infrastructure-api/)
