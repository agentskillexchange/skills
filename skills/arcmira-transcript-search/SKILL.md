---
name: "Arcmira: YouTube Transcript Search"
slug: "arcmira-transcript-search"
description: "Search indexed YouTube and podcast transcripts through Arcmira MCP. Return quoted passages, speaker attribution when available, and timestamped links to the recordings."
category: "Media & Transcription"
framework: "MCP"
verification: listed
source: "https://github.com/arcmira/arcmira/blob/25db4091b7b959149754c5f783197885279a5c0f/skills/arcmira/SKILL.md"
---

# Arcmira: YouTube Transcript Search

Use [Arcmira](https://arcmira.com) when a user wants to find what a speaker said across indexed YouTube videos and podcasts. Ask which topic, show or time period matters if the request leaves it unclear.

## Find and cite a passage

1. Call `arcmira_describe` to get the current arguments and response fields. For a topic search, start with the user's words. If you need to restrict results to a person or channel, resolve its name and use the returned ID.
2. Use `arcmira_execute_read` to call `arcmira.search` with the query, date window and a small result limit. For example, look for three passages discussing GPU financing in the last 60 days.
3. Read the surrounding lines before quoting a passage. Return the exact words, show, publication date and timestamped source link. Include the speaker's name when the source identifies them. If the search returns no matches, report the query and date window you checked.

Arcmira requires an account. Metered reads use credits from your plan, then your configured on-demand budget. A Premium transcript read can start transcription for the whole video. Check the quote and respect the user's instructions about usage. Create a monitor through `arcmira_execute_write` only when the user asks for monitoring and confirms the scope. Delivered alerts use credits. See [plans and usage](https://arcmira.com/docs/usage-and-billing).

## Installation

Connect the hosted endpoint `https://mcp.arcmira.com/mcp` in your MCP client and sign in with Arcmira. Follow the [client setup guide](https://arcmira.com/docs/mcp-server) and use the [API docs](https://arcmira.com/docs) for the HTTP interface.

For the complete upstream skill collection, including quote discovery, company monitoring, show comparison, person research and sponsor research, check out the reviewed revision:

```sh
git clone https://github.com/arcmira/arcmira.git arcmira-sdk
git -C arcmira-sdk checkout --detach 25db4091b7b959149754c5f783197885279a5c0f
```

For Claude Code, run this from the project where you want the skills. Start with a project that has no existing skills with these names:

```sh
mkdir -p .claude/skills
cp -R arcmira-sdk/skills/. .claude/skills/
```

This catalog guide adapts the [upstream transcript research skill](https://github.com/arcmira/arcmira/blob/25db4091b7b959149754c5f783197885279a5c0f/skills/arcmira/SKILL.md) into a standalone search procedure. The SDK and its skills use the accompanying [Apache License 2.0](LICENSE). The [MCP implementation](https://github.com/arcmira/mcp) and hosted service have separate terms.
