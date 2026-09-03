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

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/azeemkafridi/bulkpublish-api/tree/main/skills/social-media-content-skills

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
