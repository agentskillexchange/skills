---
name: Format plain-text drafts for clean Substack paste
description: Transforms raw draft text into paste-ready Substack HTML so an agent
  can preserve headings, emphasis, lists, and spacing without hand-formatting every
  paragraph. Use it when the job is preparing a finished newsletter draft for the
  editor, not when you just need general writing help.
verification: security_reviewed
source: https://github.com/openclaw/skills/tree/main/skills/maddiedreese/substack-formatter
category:
- Content Writing &amp; SEO
framework:
- OpenClaw
---
# Format plain-text drafts for clean Substack paste

This entry uses the substack-formatter skill from the openclaw/skills repository to turn plain text into HTML that pastes cleanly into the Substack editor. The agent behavior is specific: it takes a finished draft, restructures paragraphs, preserves emphasis, converts headers and lists into the tags Substack recognizes, and returns output that is ready for copy and paste. That makes it a skill-shaped workflow, not a generic writing tool listing.
Invoke this when you already have the words and the problem is publication formatting. A user should reach for it instead of using Substack normally when pasting markdown or plain text would otherwise lose bold text, italics, spacing, or list structure. It is especially useful in an agent workflow where the model has already drafted an essay, newsletter, or essay update and the last mile is making the editor accept the formatting cleanly.
The scope boundary matters. This is not “Substack” as a product listing, and it is not a general HTML converter. The job is narrowly about preparing text for the Substack editor with minimal voice changes. It does not manage subscribers, send newsletters, analyze performance, or replace Substack’s publishing product. It handles one concrete operator task inside a larger writing workflow.
Integration points are straightforward: the skill source includes formatter scripts, can be called from an OpenClaw skill flow, and fits naturally after content drafting and before final human review or paste into the Substack editor.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/format-plain-text-drafts-for-clean-substack-paste/)
