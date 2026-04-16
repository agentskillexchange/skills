---
title: "write-good English Prose Linting for Technical Content"
description: "This skill uses write-good to flag vague, wordy, or hard-to-read English prose in documentation and content drafts. It is useful when a team wants lightweight style feedback inside editors, scripts, or CI checks."
verification: "security_reviewed"
source: "https://github.com/btford/write-good"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "btford/write-good"
  github_stars: 5065
  ase_npm_package: "write-good"
  npm_weekly_downloads: 49520
  license: "MIT"
---

# write-good English Prose Linting for Technical Content

write-good is a JavaScript linter for English prose that highlights patterns associated with weak or cluttered writing. This skill packages write-good into a documentation and content-review workflow for technical teams that want faster feedback on docs, READMEs, blog drafts, release notes, onboarding guides, and support content. Rather than replacing editorial judgment, the tool acts as an automated first pass that points out weasel words, passive constructions, repeated lexical patterns, too-wordy phrases, and readability issues before human review begins.

The skill is especially useful in repos where prose changes ship alongside code and where review bandwidth is limited. It shows how to run write-good against Markdown or text content, wire it into npm scripts, surface warnings in editor integrations, and use the findings to tighten documentation before publishing. Because the tool is small and scriptable, it works well in pull-request checks, docs QA routines, and local author workflows. Teams can combine it with broader documentation pipelines so that style warnings appear alongside spelling, Markdown, and link-validation checks.

Outputs usually include line-based warnings or lint messages that identify wording patterns worth revising, not final editorial decisions. Integration points include Node.js toolchains, documentation repos, static site builds, content review pipelines, and custom pre-commit or CI jobs. When the goal is clearer technical writing with less manual nitpicking, write-good gives teams an inexpensive automated filter that catches common prose problems early.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/write-good-english-prose-linting-technical-content/)
