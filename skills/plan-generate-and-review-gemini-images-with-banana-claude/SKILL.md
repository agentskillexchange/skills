---
name: "Plan, generate and review Gemini images in Claude Code with Banana Claude"
slug: "plan-generate-and-review-gemini-images-with-banana-claude"
description: "Turn a visual brief into an approved Gemini image or edit from Claude Code, then inspect the saved pixels against explicit acceptance checks."
verification: "security_reviewed"
source: "https://github.com/AgriciDaniel/banana-claude/tree/main/skills/banana"
author: "AgriciDaniel"
publisher_type: "Community"
category: "Image & Creative Automation"
framework: "Claude Code"
---

# Plan, generate and review Gemini images in Claude Code with Banana Claude

Turn a visual brief into an approved Gemini image or edit from Claude Code, then inspect the saved pixels against explicit acceptance checks.

## Prerequisites

Claude Code 2.1.199+; Python 3.11+ (python3); bundled Banana Claude MCP process; billing-enabled Google AI project and Gemini API key

## Installation

Install or set up from the source-backed instructions:

Requirements: Claude Code 2.1.199+, Python 3.11+ with python3 on PATH, and a Gemini API key for a billing-enabled Google AI project. In Claude Code, run: /plugin marketplace add AgriciDaniel/banana-claude /plugin install banana-claude@banana-claude-marketplace /plugin enable banana-claude@banana-claude-marketplace /reload-plugins Supply google_ai_api_key through the sensitive plugin configuration prompt; do not put the key in chat or a command. Start with /banana-claude:banana generate followed by the visual brief. The plugin installs disabled and requires explicit enabling. Review the offline plan before approving any paid provider attempt. Existing 1.4.1 or 2.1.0 users must follow the upstream upgrade guide before enabling version 3.

- Source: https://github.com/AgriciDaniel/banana-claude/tree/main/skills/banana

## Documentation

- https://github.com/AgriciDaniel/banana-claude/blob/main/docs/guide.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/plan-generate-and-review-gemini-images-with-banana-claude/)
