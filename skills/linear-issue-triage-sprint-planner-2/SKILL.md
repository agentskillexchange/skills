---
name: Linear Issue Triage &amp; Sprint Planner
description: Queries the Linear GraphQL API to list open issues by team, priority,
  and cycle, then applies configurable triage rules to auto-assign or escalate. Generates
  sprint plan drafts scored against velocity and team capacity from Linear projectMilestone
  and workflowState data.
verification: security_reviewed
source: https://agentskillexchange.com/skills/linear-issue-triage-sprint-planner-2/
category:
- Integrations &amp; Connectors
framework:
- Claude Code
---
# Linear Issue Triage & Sprint Planner

Linear Issue Triage & Sprint Planner is built around GraphQL API ecosystem. The underlying ecosystem is represented by graphql/graphql-js (20,335+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like queries, mutations, schema introspection, fragments, pagination, subscriptions and preserving the operational context that matters for real tasks.
In practice, the skill gives an agent a stable interface to graphql so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Queries the Linear GraphQL API to list open issues by team, priority, and cycle, then applies configurable triage rules to auto-assign or escalate. Generates sprint plan drafts scored against velocity and team capacity from Linear projectMilestone and workflowState data. The implementation typically relies on queries, mutations, schema introspection, fragments, pagination, subscriptions, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

Accesses queries, mutations, schema introspection, fragments, pagination, subscriptions instead of scraping a UI, which makes runs easier to audit and retry.
Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.
Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.
Fits into broader integration points such as typed API access, schema exploration, and integration workflows.

As a runbook-style skill, the value is not just tool access but operational sequencing: check the right signals first, reduce alert noise, and produce a summary that another engineer can act on immediately. Key integration points include typed API access, schema exploration, and integration workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/linear-issue-triage-sprint-planner-2/)
