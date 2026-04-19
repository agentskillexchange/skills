---
title: "Format plain-text drafts for clean Substack paste"
description: "This entry uses the substack-formatter skill from the openclaw/skills repository to turn plain text into HTML that pastes cleanly into the Substack editor. The agent behavior is specific: it takes a finished draft, restructures paragraphs, preserves emphasis, converts headers and lists into the tags Substack recognizes, and returns output that is ready for copy and paste. That makes it a skill-shaped workflow, not a generic writing tool listing. Invoke this when you already have the words and the problem is publication formatting. A user should reach for it instead of using Substack normally when pasting markdown or plain text would otherwise lose bold text, italics, spacing, or list structure. It is especially useful in an agent workflow where the model has already drafted an essay, newsletter, or essay update and the last mile is making the editor accept the formatting cleanly. The scope boundary matters. This is not “Substack” as a product listing, and it is not a general HTML converter. The job is narrowly about preparing text for the Substack editor with minimal voice changes. It does not manage subscribers, send newsletters, analyze performance, or replace Substack’s publishing product. It handles one concrete operator task inside a larger writing workflow. Integration points are straightforward: the skill source includes formatter scripts, can be called from an OpenClaw skill flow, and fits naturally after content drafting and before final human review or paste into the Substack editor."
source: "https://github.com/openclaw/skills/tree/main/skills/maddiedreese/substack-formatter"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "openclaw/skills"
  github_stars: 4086
---

# Format plain-text drafts for clean Substack paste

This entry uses the substack-formatter skill from the openclaw/skills repository to turn plain text into HTML that pastes cleanly into the Substack editor. The agent behavior is specific: it takes a finished draft, restructures paragraphs, preserves emphasis, converts headers and lists into the tags Substack recognizes, and returns output that is ready for copy and paste. That makes it a skill-shaped workflow, not a generic writing tool listing. Invoke this when you already have the words and the problem is publication formatting. A user should reach for it instead of using Substack normally when pasting markdown or plain text would otherwise lose bold text, italics, spacing, or list structure. It is especially useful in an agent workflow where the model has already drafted an essay, newsletter, or essay update and the last mile is making the editor accept the formatting cleanly. The scope boundary matters. This is not “Substack” as a product listing, and it is not a general HTML converter. The job is narrowly about preparing text for the Substack editor with minimal voice changes. It does not manage subscribers, send newsletters, analyze performance, or replace Substack’s publishing product. It handles one concrete operator task inside a larger writing workflow. Integration points are straightforward: the skill source includes formatter scripts, can be called from an OpenClaw skill flow, and fits naturally after content drafting and before final human review or paste into the Substack editor.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/format-plain-text-drafts-for-clean-substack-paste/)
