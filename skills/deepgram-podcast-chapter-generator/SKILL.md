---
title: "Deepgram Podcast Chapter Generator"
description: "Submits podcast MP3 URLs to Deepgram Nova-2 with paragraph and summarize features, then clusters returned timestamps into logical chapters using a sliding-window topic boundary algorithm. Outputs YouTube-compatible chapter timestamps and an RSS-ready podcast:chapters JSON feed. Optionally posts chapters as a Notion database entry."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/deepgram-podcast-chapter-generator/"
category:
  - "Media & Transcription"
framework:
  - "ChatGPT Agents"
---

# Deepgram Podcast Chapter Generator

Submits podcast MP3 URLs to Deepgram Nova-2 with paragraph and summarize features, then clusters returned timestamps into logical chapters using a sliding-window topic boundary algorithm. Outputs YouTube-compatible chapter timestamps and an RSS-ready podcast:chapters JSON feed. Optionally posts chapters as a Notion database entry.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/deepgram-podcast-chapter-generator/)
