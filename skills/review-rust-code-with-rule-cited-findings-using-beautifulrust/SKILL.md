---
name: "Review Rust code with rule-cited findings using BeautifulRust"
slug: "review-rust-code-with-rule-cited-findings-using-beautifulrust"
description: "Review a Rust file, crate or diff with scoped tool checks and prioritized findings that cite source rules, locations and concrete fixes."
github_stars: 1293
verification: "security_reviewed"
source: "https://github.com/morganlinton/BeautifulRust"
author: "morganlinton"
publisher_type: "community"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "morganlinton/BeautifulRust"
  github_stars: 1293
---

# Review Rust code with rule-cited findings using BeautifulRust

Review a Rust file, crate or diff with scoped tool checks and prioritized findings that cite source rules, locations and concrete fixes.

## Prerequisites

Agent Skills-compatible coding agent; Git for manual installation; Rust toolchain and Cargo for optional mechanical checks

## Installation

Install or set up from the source-backed instructions:

Clone the upstream repository and select the inspected revision: git clone https://github.com/morganlinton/BeautifulRust.git cd BeautifulRust git checkout --detach 58757ee890da9b3c8d5b785adc7a8d53cce27307 Install the complete rust-best-practices, rust-review and rust-port folders, including references, into your agent's supported skills directory following the pinned README. For a runtime using the shared user skills directory: mkdir -p ~/.agents/skills cp -R skills/rust-best-practices skills/rust-review skills/rust-port ~/.agents/skills/ For Claude Code use ~/.claude/skills/ instead. Check for existing folders before copying; restart or reload the agent, then request a review of a specific Rust file, crate or diff. Rust and Cargo are needed for tool checks; reading-only review remains supported when unavailable.

- Source: https://github.com/morganlinton/BeautifulRust

## Documentation

- https://github.com/morganlinton/BeautifulRust/blob/58757ee890da9b3c8d5b785adc7a8d53cce27307/skills/rust-review/SKILL.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-rust-code-with-rule-cited-findings-using-beautifulrust/)
