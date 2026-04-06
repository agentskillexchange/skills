---
name: "Deepgram Podcast Chapter Generator"
description: "Submits podcast MP3 URLs to Deepgram Nova-2 with paragraph and summarize features, then clusters returned timestamps into logical chapters using a sliding-window topic boundary algorithm. Outputs YouTube-compatible chapter timestamps and an RSS-ready podcast:chapters JSON feed. Optionally posts chapters as a Notion database entry."
category: "Media &amp; Transcription"
framework: "ChatGPT Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/deepgram-podcast-chapter-generator/"
---
# Deepgram Podcast Chapter Generator

Submits podcast MP3 URLs to Deepgram Nova-2 with paragraph and summarize features, then clusters returned timestamps into logical chapters using a sliding-window topic boundary algorithm. Outputs YouTube-compatible chapter timestamps and an RSS-ready podcast:chapters JSON feed. Optionally posts chapters as a Notion database entry.

Deepgram Podcast Chapter Generator is built around Notion workspace and database platform. The underlying ecosystem is represented by makenotion/notion-sdk-js (5,562+ GitHub stars). It gives an agent a more technical and reliable way to work with the tool than a thin one-line wrapper, using stable interfaces like pages, databases.query, blocks.children, properties, relations, pagination and preserving the operational context that matters for real tasks.

In practice, the skill gives an agent a stable interface to notion so it can inspect state, run the right operation, and produce a result that fits into a larger engineering or operations pipeline. The original use case is clear: Submits podcast MP3 URLs to Deepgram Nova-2 with paragraph and summarize features, then clusters returned timestamps into logical chapters using a sliding-window topic boundary algorithm. Outputs YouTube-compatible chapter timestamps and an RSS-ready podcast:chapters JSON feed. Optionally posts chapters as a Notion database entry. The implementation typically relies on pages, databases.query, blocks.children, properties, relations, pagination, with configuration passed through environment variables, connection strings, service tokens, or workspace config depending on the upstream platform.

- Accesses pages, databases.query, blocks.children, properties, relations, pagination instead of scraping a UI, which makes runs easier to audit and retry.

- Supports structured inputs and outputs so another tool, agent, or CI step can consume the result.

- Can be wired into cron jobs, webhook handlers, MCP transports, or local CLI workflows depending on the skill format.

- Fits into broader integration points such as knowledge bases, task tracking, content sync, and structured note workflows.

For generator-style use cases, the skill turns a vague request into repeatable scaffolding with defaults that match the upstream toolchain rather than inventing ad hoc files. Key integration points include knowledge bases, task tracking, content sync, and structured note workflows. In a real environment that usually means passing credentials through env vars or app config, respecting rate limits and permission scopes, and returning structured artifacts that can be attached to tickets, pull requests, dashboards, or follow-up automations.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill deepgram-podcast-chapter-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill deepgram-podcast-chapter-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill deepgram-podcast-chapter-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill deepgram-podcast-chapter-generator -a codex
```

### OpenClaw

```bash
clawhub install deepgram-podcast-chapter-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-podcast-chapter-generator/)
