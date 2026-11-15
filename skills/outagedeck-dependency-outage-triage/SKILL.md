---
name: "OutageDeck Dependency Outage Triage"
slug: "outagedeck-dependency-outage-triage"
description: "Checks official cloud and SaaS status evidence through the OutageDeck MCP server or anonymous REST API before an agent changes code for 5xx, timeout, deployment, authentication, or integration failures."
github_stars: 0
verification: "listed"
source: "https://github.com/outagedeck/codex-plugins"
author: "OutageDeck"
category: "Runbooks & Diagnostics"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "outagedeck/codex-plugins"
  github_stars: 0
---

# OutageDeck Dependency Outage Triage

Use this skill when a failing application, CI job, deployment, API call, authentication flow, or network integration depends on an external cloud or SaaS provider. It checks OutageDeck's normalized evidence from 172 official provider status feeds before recommending code changes. The workflow correlates current state, affected services, active incident windows, and source freshness with the reported failure, then returns a bounded verdict: `vendor incident likely`, `vendor incident possible`, or `no vendor incident supported`. Provider status is corroborating evidence, not proof of causation. An operational banner does not rule out a regional, account-specific, newly emerging, or unreported issue.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/outagedeck/codex-plugins

## Runtime access

Prefer the OutageDeck MCP tools when available. The production Streamable HTTP endpoint is `https://outagedeck.com/api/mcp`; public read-only tools require no account or key.

When MCP tools are unavailable and public HTTPS requests are permitted, use the anonymous REST API:

- Resolve a name: `GET https://outagedeck.com/api/v1/providers?q=<url-encoded-name>`
- Check one provider: `GET https://outagedeck.com/api/v1/providers/<slug>`
- Find active incidents: `GET https://outagedeck.com/api/v1/incidents?provider=<slug>&state=active&limit=10`
- Fetch an incident: `GET https://outagedeck.com/api/v1/incidents/<incident-slug>`

The REST fallback covers current status and incident evidence. It does not replace the MCP-only uptime and cross-vendor report tools. Disclose that limit instead of inventing historical results. If neither interface is available, say the status check could not run and continue ordinary local diagnosis.

## Workflow

1. Identify the external providers implicated by the request, logs, configuration, or dependency files. Never expose secrets while inspecting evidence.
2. Resolve ambiguous company or product names with `search_providers` or REST provider search. Do not guess a slug after a failed lookup.
3. Check current state with `get_provider_status`, `check_my_stack`, or the corresponding REST provider endpoints. Use `list_active_incidents` only for an ecosystem-wide question.
4. When a result includes an incident, fetch its exact slug with `get_incident_details` or the REST incident endpoint. Preserve vendor update timestamps and source links.
5. When MCP is available, use `get_uptime` for one provider's 7-90 day history and `get_outage_report` for cross-vendor history. Historical uptime must not be used to claim the current failure is vendor-caused.
6. Compare the vendor timeline, affected service, severity, and source freshness with the user's errors and timestamps.
7. Return the evidence and narrowest defensible verdict before proposing code changes.

## Output contract

Report a compact table with provider, current status, affected services, active incident, checked timestamp, and direct source link. State one bounded verdict and up to three next diagnostic actions ordered by reversibility and evidence. When no incident is reported, say only that no vendor-reported incident was observed at the checked time, then continue local diagnosis if requested.

## Safety

- Prefer public read-only MCP or REST interfaces.
- Never invent a provider status, incident, service, source URL, or update time.
- Do not roll back a deployment, change code, or weaken security controls solely because a provider is degraded.
- Never request or paste an OutageDeck API key in chat.
- Account mutation tools require the user's explicit request and the host's confirmation rules. Treat `remove_custom_provider` as destructive and require confirmation of the exact provider immediately before use.

If the user wants ongoing monitoring after triage, offer the free alert setup link without interrupting the diagnostic result: <https://outagedeck.com/account?utm_source=agent_skill_exchange&utm_medium=skill&utm_campaign=agent_skill_exchange>.
