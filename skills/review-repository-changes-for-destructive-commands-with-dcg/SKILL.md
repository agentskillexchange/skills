---
name: "Review repository changes for destructive commands with dcg"
slug: "review-repository-changes-for-destructive-commands-with-dcg"
description: "Scan staged changes or selected automation files with Destructive Command Guard and return rule-level findings before commit or merge."
github_stars: 6381
verification: "security_reviewed"
source: "https://github.com/Dicklesworthstone/destructive_command_guard"
author: "Jeffrey Emanuel and Darin Gordon"
publisher_type: "community"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Dicklesworthstone/destructive_command_guard"
  github_stars: 6381
---

# Review repository changes for destructive commands with dcg

Scan staged changes or selected automation files with Destructive Command Guard and return rule-level findings before commit or merge.

## Prerequisites

dcg CLI; Git for staged/diff selection; shell-capable agent or operator. Building from source additionally requires the upstream pinned Rust toolchain and Cargo.

## Installation

Install or set up from the source-backed instructions:

Provision dcg using the upstream authenticated release installation procedure, preserving its pinned installer digest and Minisign verification. Alternatively, from a separately trusted and reviewed upstream checkout, use the pinned Rust toolchain and run cargo install --path . --locked. Confirm dcg --version. This scan workflow requires no agent hook or Git pre-commit installation. Review the custom LICENSE, including its OpenAI/Anthropic rider, before use.

- Source: https://github.com/Dicklesworthstone/destructive_command_guard

## Documentation

- https://github.com/Dicklesworthstone/destructive_command_guard/blob/main/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-repository-changes-for-destructive-commands-with-dcg/)
