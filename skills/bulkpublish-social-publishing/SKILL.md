---
name: "BulkPublish Social Publishing"
slug: "bulkpublish-social-publishing"
description: "Adapt, review, schedule, and publish approved social content across multiple platforms through the BulkPublish API and hosted MCP."
verification: "listed"
source: "https://github.com/azeemkafridi/bulkpublish-api/tree/main/skills/social-media-content-skills"
category: "Integrations & Connectors"
framework: "MCP"
---

# BulkPublish Social Publishing

Use this skill when an agent needs to move social content from a reviewed draft into an approved, scheduled, or published multi-platform campaign. BulkPublish supplies the API and hosted MCP layer for the operational handoff. The skill is useful for content teams, growth operators, and agent builders who need a repeatable approval boundary instead of ad hoc platform calls. It covers preparation, platform adaptation, scheduling, execution, and verification while keeping credentials and account details outside the skill.

## References

- BulkPublish API repository: https://github.com/azeemkafridi/bulkpublish-api
- BulkPublish MCP documentation: https://app.bulkpublish.com/docs
- Hosted MCP endpoint: https://mcp.bulkpublish.com/mcp
- Source social-media content skills: https://github.com/azeemkafridi/bulkpublish-api/tree/main/skills/social-media-content-skills

## Installation

Create a BulkPublish account and obtain an API key from Settings > Developer. Connect only the social channels approved for this pilot. Use an MCP client that supports Streamable HTTP and an authorization header.

Add `https://mcp.bulkpublish.com/mcp` as the remote MCP endpoint in your client's connection settings. Configure the `Authorization` header as `Bearer <your BulkPublish API key>` using the client's secret store. Never put the real key in the endpoint URL, a shared configuration file, or a screenshot. If your client cannot supply this header, use the upstream documented local-server route instead; authentication remains mandatory.

Load this skill through your agent's documented instructions mechanism. Connecting the MCP server supplies tools; it does not automatically load this workflow or authorize publishing.

- Source: https://github.com/azeemkafridi/bulkpublish-api/tree/main/skills/social-media-content-skills

## Verification

Reconnect the client and inspect the available tools. First request only `list_channels`, then compare the returned channel IDs and accounts with the approved dashboard connections. Tool discovery alone is not proof of authenticated access. Treat a 401 or an unexpected account as a failed setup and stop.

Do not create a draft, schedule a post, upload media, or publish during this connection check. Continue to the workflow below only after the user approves the exact payload and targets. See the [upstream MCP configuration guide](https://github.com/azeemkafridi/bulkpublish-api/blob/main/mcp-server/README.md) for client-specific options.

## Workflow

1. Collect the approved source copy, media, links, target platforms and accounts, timezone, and requested schedule.
2. Adapt content per platform while preserving approved claims, disclosures, consent, links, and brand constraints.
3. Show the exact per-platform payload, media, account targets, and schedule to the user.
4. Wait for explicit approval of that exact payload and target set before using a create, schedule, or publish tool.
5. Use BulkPublish's API or hosted MCP to execute the approved operation.
6. Retrieve each resulting status and report platform, account, scheduled time, identifier, URL, and errors.

## Safety and failure handling

- Publishing and scheduling are external side effects; never infer approval from an earlier draft or a different target set.
- Never invent account IDs, media URLs, permissions, delivery results, or analytics.
- If an external call times out, retrieve its status before retrying so the operation is not duplicated.
- Report partial success per platform and leave failed targets unsent unless the user explicitly approves a retry.
- Preserve platform disclosures, opt-outs, copyright notes, and human review requirements.

## Output

Return a compact status table with platform, account, operation, status, schedule, identifier, public URL when available, and unresolved follow-up actions.
