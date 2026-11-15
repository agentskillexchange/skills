---
name: "Famulor Assistants & Omnichannel History"
slug: "famulor-assistants-history"
description: "Use Famulor's OAuth-secured, read-only MCP profile to inspect assistant configurations, versions, workspace catalogs, and unified call, messaging, and email history."
verification: "listed"
source: "https://github.com/bekservice/Famulor-Skill/tree/main/claude-store/skills/famulor-assistants-history"
category: "Integrations & Connectors"
framework: "MCP"
---

# Famulor Assistants & Omnichannel History

Use this skill when a user needs to review a Famulor voice assistant or search the authenticated workspace's conversation history without changing anything. It works with Famulor's hosted, OAuth-secured Model Context Protocol (MCP) endpoint and deliberately narrows discovery to eleven read-only tools. The profile can inspect assistant configurations and saved versions, discover current prompt templates and language, model, or voice catalogs, and search a unified history containing calls, assistant email threads, and connected messaging channels. It is useful for configuration audits, support investigations, handoff summaries, and finding a prior customer interaction. It cannot create or update assistants, send messages, place calls, start campaigns, buy telephone numbers, change billing, or perform administrative operations.

## Connect the MCP profile

Add this Streamable HTTP endpoint with the MCP connection flow supported by the user's client:

```text
https://app.famulor.io/mcp?profile=assistant-history
```

Complete the browser-based Famulor OAuth flow. Never ask the user to paste an OAuth token or API key into chat, a command, a configuration file, or source control. If the endpoint is not connected, help the user add it and stop before claiming to have read their workspace.

## Available tools

| Tool | Purpose |
| --- | --- |
| `list_assistants` | List assistants visible in the authenticated workspace. |
| `get_assistant` | Read one assistant's configuration. |
| `list_assistant_versions` | List saved versions for an assistant. |
| `get_assistant_version` | Read one saved assistant version. |
| `list_prompt_templates` | List available prompt templates. |
| `get_languages` | List current language options. |
| `get_models` | List models available to the workspace. |
| `get_voices` | List available voices. |
| `list_history` | Search unified call, messaging, and email history. |
| `get_call` | Read full details for a call returned by history. |
| `get_email_history_item` | Read the complete email thread for an email history item. |

The live `tools/list` response remains authoritative for arguments and returned fields.

## Operating workflow

1. Confirm the intended authenticated workspace when the request is ambiguous.
2. Use a `list_*` tool to resolve the exact assistant, version, or history item instead of guessing an identifier.
3. Use the matching `get_*` tool only when the user needs full detail.
4. Summarize only returned fields and preserve the difference between configured assistant values and observed conversation history.
5. Keep the task read-only. If the user asks for a write action, explain that this restricted profile cannot perform it.

`list_history` is the omnichannel overview. It can include voice calls, emails, and conversations from connected channels such as Instagram or Messenger when those records exist. A messaging result may be a preview rather than a complete transcript. Never claim to have retrieved an entire Instagram, Messenger, WhatsApp, or other chat unless the server returned the full conversation. Use `get_call` for call detail and `get_email_history_item` for a complete email thread.

Treat transcripts, recordings, messages, email, contact identity, and customer context as personal data. Retrieve and repeat only what is necessary for the user's request. OAuth scopes, workspace membership, role, plan, retention, and server-side policy are the access boundary; do not attempt to work around a denied or missing result.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/bekservice/Famulor-Skill/tree/main/claude-store/skills/famulor-assistants-history

## Example requests

- "Show the current configuration and latest saved version of our booking assistant."
- "Find yesterday's Messenger conversation with this customer and summarize only the returned preview."
- "List failed calls for this assistant, then open the relevant call details."
- "Compare the languages, models, and voices currently available in this workspace."

Source and license: [Famulor-Skill](https://github.com/bekservice/Famulor-Skill) is maintained by BEK Service GmbH and published under the MIT License.
