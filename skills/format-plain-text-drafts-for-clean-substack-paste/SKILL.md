---
title: "Format plain-text drafts for clean Substack paste"
description: "Transforms raw draft text into paste-ready Substack HTML so an agent can preserve headings, emphasis, lists, and spacing without hand-formatting every paragraph. Use it when the job is preparing a finished newsletter draft for the editor, not when you just need general writing help."
slug: "format-plain-text-drafts-for-clean-substack-paste"
category:
  - "Content Writing &amp; SEO"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://github.com/openclaw/skills/tree/main/skills/maddiedreese/substack-formatter"
---

# Format plain-text drafts for clean Substack paste

Transforms raw draft text into paste-ready Substack HTML so an agent can preserve headings, emphasis, lists, and spacing without hand-formatting every paragraph. Use it when the job is preparing a finished newsletter draft for the editor, not when you just need general writing help.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install format-plain-text-drafts-for-clean-substack-paste
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This entry uses the substack-formatter skill from the openclaw/skills repository to turn plain text into HTML that pastes cleanly into the Substack editor. The agent behavior is specific: it takes a finished draft, restructures paragraphs, preserves emphasis, converts headers and lists into the tags Substack recognizes, and returns output that is ready for copy and paste. That makes it a skill-shaped workflow, not a generic writing tool listing.
Invoke this when you already have the words and the problem is publication formatting. A user should reach for it instead of using Substack normally when pasting markdown or plain text would otherwise lose bold text, italics, spacing, or list structure. It is especially useful in an agent workflow where the model has already drafted an essay, newsletter, or essay update and the last mile is making the editor accept the formatting cleanly.
The scope boundary matters. This is not “Substack” as a product listing, and it is not a general HTML converter. The job is narrowly about preparing text for the Substack editor with minimal voice changes. It does not manage subscribers, send newsletters, analyze performance, or replace Substack’s publishing product. It handles one concrete operator task inside a larger writing workflow.
Integration points are straightforward: the skill source includes formatter scripts, can be called from an OpenClaw skill flow, and fits naturally after content drafting and before final human review or paste into the Substack editor.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/format-plain-text-drafts-for-clean-substack-paste/)
