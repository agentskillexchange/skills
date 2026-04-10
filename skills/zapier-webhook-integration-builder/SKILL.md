---
name: "Zapier Webhook Integration Builder"
description: "Creates and manages Zapier integrations using the Zapier Platform CLI and REST Hooks API. Builds custom triggers, actions, and searches with OAuth2 authentication flows."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/zapier-webhook-integration-builder/"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Custom Agents"
---

# Zapier Webhook Integration Builder

The Zapier Webhook Integration Builder automates the creation of custom Zapier integrations using the Zapier Platform CLI and Platform API. It scaffolds new integration projects with zapier init, generates trigger definitions using REST Hook subscriptions for real-time event delivery, and builds action modules with proper request/response mapping. The skill handles OAuth2 authentication setup including token refresh flows, session auth configurations, and API key injection patterns. Using the Zapier Platform CLI, it runs local testing with zapier test, validates integration schemas, and manages version promotion through zapier promote. The builder generates proper input field definitions with dynamic dropdowns powered by custom search endpoints, implements deduplication logic for polling triggers, and handles file upload/download actions with proper streaming. It configures error handling with custom error messages, implements rate limiting retry logic, and manages environment variables through zapier env. Advanced features include middleware setup for request/response transformation, bulk operation support for high-volume actions, and automated integration testing against sandbox APIs.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/zapier-webhook-integration-builder/)
