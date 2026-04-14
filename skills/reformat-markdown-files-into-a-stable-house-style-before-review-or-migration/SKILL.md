---
title: "Reformat Markdown files into a stable house style before review or migration"
description: "Runs mdformat to rewrite Markdown into a consistent CommonMark-oriented layout or check mode in CI. Use it when an agent needs deterministic Markdown diffs before review, migration, or bulk cleanup, not when it needs to generate new content or build a docs site."
verification: security_reviewed
source: "https://github.com/hukkin/mdformat"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "hukkin/mdformat"
  github_stars: 758
---

# Reformat Markdown files into a stable house style before review or migration

This skill uses mdformat, the CommonMark-compliant Markdown formatter maintained in the hukkin/mdformat project, to normalize Markdown files into a consistent style before humans or downstream agents review them. An agent invokes it after content already exists but before a docs migration, repository-wide cleanup, pre-commit enforcement, or large pull request where noisy formatting diffs would otherwise hide the real changes. The tool can rewrite files in place or run in check mode, which makes it a good fit for both interactive cleanup and CI gating.

The key boundary is that this is a formatting skill, not a writing skill. The agent is not using mdformat to invent documentation, restructure information architecture, lint every style issue, or run a full static-site build. It is using mdformat to produce stable Markdown output so later review and automation steps operate on cleaner files. That distinction matters, because without it the entry would collapse into a generic formatter listing. Here the agent job is specific: stabilize Markdown presentation before review, migration, or repository-wide cleanup.

Useful integration points include pre-commit hooks, bulk docs refactors, generated Markdown cleanup, and CI checks that need reproducible formatting. The upstream project exposes a maintained official repository, published package metadata on PyPI, standalone documentation, and an active release stream. The upstream quick start uses pipx install mdformat, with optional plugins for GitHub Flavored Markdown and other extensions when needed.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reformat-markdown-files-into-a-stable-house-style-before-review-or-migration/)
