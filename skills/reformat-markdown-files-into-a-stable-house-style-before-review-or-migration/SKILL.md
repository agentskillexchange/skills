---
name: "Reformat Markdown files into a stable house style before review or migration"
slug: "reformat-markdown-files-into-a-stable-house-style-before-review-or-migration"
description: "Runs mdformat to rewrite Markdown into a consistent CommonMark-oriented layout or check mode in CI. Use it when an agent needs deterministic Markdown diffs before review, migration, or bulk cleanup, not when it needs to generate new content or build a docs site."
github_stars: 758
verification: "security_reviewed"
source: "https://github.com/hukkin/mdformat"
author: "Taneli Hukkinen"
category: "Templates & Workflows"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "hukkin/mdformat"
  github_stars: 758
---

# Reformat Markdown files into a stable house style before review or migration

Runs mdformat to rewrite Markdown into a consistent CommonMark-oriented layout or check mode in CI. Use it when an agent needs deterministic Markdown diffs before review, migration, or bulk cleanup, not when it needs to generate new content or build a docs site.

## Prerequisites

Python 3, pipx or pip, command line

## Installation

Use the upstream install or setup path that matches your environment:
- pipx install mdformat
- pipx inject mdformat mdformat-gfm

Requirements and caveats from upstream:
- Mdformat is a Unix-style command-line tool as well as a Python library.
- require and enable an extension plugin (multiple
- require and enable a code formatter plugin (multiple

Basic usage or getting-started notes:
- bash
- <!-- end installing -->
- <!-- start cli-usage -->

- Source: https://github.com/hukkin/mdformat
- Extracted from upstream docs: https://raw.githubusercontent.com/hukkin/mdformat/HEAD/README.md

## Documentation

- https://mdformat.readthedocs.io/en/stable/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/reformat-markdown-files-into-a-stable-house-style-before-review-or-migration/)
