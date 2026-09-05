---
name: "Constrain coding-agent over-defense with HERO"
slug: "constrain-coding-agent-over-defense-with-hero"
description: "Paste HERO's scope-limits contract into always-loaded agent config so coding agents keep fixes proportionate and avoid unnecessary hashing, edge-case hardening, rubric loops, and overbuild."
github_stars: 397
verification: "security_reviewed"
source: "https://github.com/wanshuiyin/HERO-Anti-OverDefense"
author: "wanshuiyin"
publisher_type: "individual"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "wanshuiyin/HERO-Anti-OverDefense"
  github_stars: 397
---

# Constrain coding-agent over-defense with HERO

Paste HERO's scope-limits contract into always-loaded agent config so coding agents keep fixes proportionate and avoid unnecessary hashing, edge-case hardening, rubric loops, and overbuild.

## Prerequisites

A coding-agent host that loads persistent instruction files, such as Codex AGENTS.md, Claude Code CLAUDE.md, Antigravity AGENTS.md, GitHub Copilot copilot-instructions.md, Cursor rules, Windsurf rules, or Gemini CLI GEMINI.md

## Installation

Install or set up from the source-backed instructions:

Copy the canonical scope-limits block from RULES.md into the instruction file your agent host loads automatically. For Codex and Antigravity use AGENTS.md in the project root; for Claude Code use CLAUDE.md; for GitHub Copilot use .github/copilot-instructions.md; for Cursor, Windsurf, and Gemini CLI use the host-specific files documented in hosts/README.md. Keep the case catalogue out of the loaded prompt and quote cases only when calibrating a disputed behavior.

- Source: https://github.com/wanshuiyin/HERO-Anti-OverDefense

## Usage and Verification

Pilot in a disposable repository. Review the upstream RULES.md before copying; preserve existing project instructions, security requirements, and approval boundaries. Record the upstream revision you reviewed so a later update can be compared deliberately.

Start a new agent session and ask for a read-only plan to correct one typo in a test document. Check that the host loads the intended instruction file, the plan stays within that document, and the agent does not propose unrelated infrastructure or remove required tests. Compare with the same task before adding HERO. This is a suggested local acceptance exercise, not an upstream benchmark or proof of reliability.

Inspect the instruction-file diff before keeping the change. Remove only the added HERO block if behavior worsens. Scope restraint must not suppress disclosure of errors or weaken mandatory safety checks.

## Documentation

- https://github.com/wanshuiyin/HERO-Anti-OverDefense

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/constrain-coding-agent-over-defense-with-hero/)
