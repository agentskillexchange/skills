---
name: "Search and rewrite code with structural GritQL patterns before broad migrations"
slug: "search-and-rewrite-code-with-structural-gritql-patterns-before-broad-migrations"
description: "Use GritQL when an agent needs reviewable structural search and rewrite passes across a large codebase before a migration, policy cleanup, or API change, instead of relying on regex or hand edits."
github_stars: 4482
verification: "listed"
source: "https://github.com/biomejs/gritql"
author: "biomejs"
publisher_type: "community"
category: "Code Quality & Review"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "biomejs/gritql"
  github_stars: 4482
---

# Search and rewrite code with structural GritQL patterns before broad migrations

Use GritQL when an agent needs reviewable structural search and rewrite passes across a large codebase before a migration, policy cleanup, or API change, instead of relying on regex or hand edits.

## Prerequisites

Grit CLI, a local repository to search or rewrite, and a review loop for inspecting the diffs produced by structural patterns.

## Installation

Requirements and caveats from upstream:
- ♻️ Once you learn GritQL, you can use it to rewrite any [target language](https://docs.grit.io/language/target-languages): JavaScript/TypeScript, Python, JSON, Java, Terraform, Solidity, CSS, Markdown, YAML, Rust, Go,...
- Patterns can be combined to create complex queries, including [large refactors](https://github.com/getgrit/stdlib/blob/main/.grit/patterns/python/openai.md).
- Reading/writing a codemod requires mentally translating from AST names back to what source code actually looks like.

Basic usage or getting-started notes:
- Read the [documentation](https://docs.grit.io/language/overview), [interactive tutorial](https://docs.grit.io/tutorials/gritql), or run grit --help.
- sh
- Search for all your console.log calls by putting the desired pattern in backticks:

- Source: https://github.com/biomejs/gritql
- Extracted from upstream docs: https://raw.githubusercontent.com/biomejs/gritql/HEAD/README.md

## Documentation

- https://docs.grit.io/language/overview

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-and-rewrite-code-with-structural-gritql-patterns-before-broad-migrations/)
