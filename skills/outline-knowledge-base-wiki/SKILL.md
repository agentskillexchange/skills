---
name: "Outline Open Source Team Knowledge Base and Wiki Platform"
description: "Outline is a fast, collaborative knowledge base for teams built with React and Node.js. It provides real-time editing, Markdown support, and a rich API for integration with Slack, authentication providers, and custom workflows."
verification: security_reviewed
source: "https://github.com/outline/outline"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
---

# Outline Open Source Team Knowledge Base and Wiki Platform

Outline is a modern, open-source knowledge base and wiki platform designed for growing teams that need a fast, beautiful, and collaborative documentation environment. Built with React on the frontend and Node.js on the backend, Outline delivers real-time collaborative editing with Markdown compatibility, making it easy for teams to create, organize, and share internal documentation.
At its core, Outline provides a structured document hierarchy with collections, nested documents, and powerful full-text search. The editor supports rich Markdown with slash commands, embeds, tables, code blocks, and media. Multiple team members can edit the same document simultaneously with changes synced in real time through WebSocket connections.
For agent integration, Outline exposes a comprehensive REST API that covers document CRUD operations, collection management, user administration, and search. The API uses Bearer token authentication and returns JSON responses, making it straightforward to build automation workflows. Agents can programmatically create documents, update content, query collections, and manage team knowledge through the API.
Outline integrates natively with Slack for notifications and unfurling, supports SSO through OIDC, SAML, Google, and Microsoft authentication providers, and can be self-hosted using Docker. The platform also supports webhooks for event-driven automation, enabling agents to react to document changes, new comments, or collection updates.
Key features for agent workflows include the ability to import and export documents in Markdown format, programmatic template management, revision history access through the API, and structured collection organization that maps well to knowledge management tasks. The search API supports full-text queries with filtering by collection, user, and date range.
Outline requires Node.js 18+, PostgreSQL, and Redis for self-hosted deployments. A hosted version is available at getoutline.com for teams that prefer managed infrastructure.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/outline-knowledge-base-wiki/)
