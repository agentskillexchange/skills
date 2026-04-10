---
name: Build and debug custom WordPress REST API endpoints with schema and permission
  guardrails
description: Uses the WordPress wp-rest-api skill to help an agent design, register,
  validate, and troubleshoot custom REST routes without skipping schema, auth, or
  permission_callback details. This is for agent-led endpoint work in plugins, themes,
  or core-adjacent codebases, not for browsing the WordPress REST API as a product
  catalog.
verification: listed
source: https://github.com/WordPress/agent-skills/tree/trunk/skills/wp-rest-api
category:
- WordPress &amp; CMS
framework:
- Multi-Framework
---
# Build and debug custom WordPress REST API endpoints with schema and permission guardrails

This entry is built from the official wp-rest-api skill in the WordPress/agent-skills repository. The underlying tool is not a generic SDK listing. It is a bounded agent workflow for building, extending, and debugging WordPress REST API routes in real codebases. The agent’s job here is concrete: locate existing REST usage, choose the right route strategy, register endpoints safely, define schemas and argument validation, wire up permission_callback, expose fields or meta when needed, and verify that the route behaves correctly under WordPress auth rules.
Use this when a user wants an agent to add a custom endpoint, expose a post type through REST, fix 401 or 403 failures, debug missing routes, or shape response payloads for a client app. That is the moment to invoke the skill instead of just “using WordPress normally.” The value is in the operator playbook: the agent follows a disciplined path through route registration, schema validation, permission checks, WP_REST_Request handling, and verification of discovery, pagination, and response links.
The scope boundary is clear. This is not a listing for WordPress itself, not a general REST API explainer, and not a catch-all CMS card. It only covers the job of implementing or troubleshooting WordPress REST behavior in code. Integration points include register_rest_route, WP_REST_Controller, register_rest_field, register_meta, CPT settings such as show_in_rest, and whichever auth mode the project uses, including cookies plus nonce or application passwords. Because the upstream source is official, actively maintained, documented, and release-backed, it clears the source and evidence gates cleanly.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/build-and-debug-custom-wordpress-rest-api-endpoints-with-schema-and-permission-guardrails/)
