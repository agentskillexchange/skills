---
name: "write-good English Prose Linting for Technical Content"
slug: "write-good-english-prose-linting-technical-content"
description: "This skill uses write-good to flag vague, wordy, or hard-to-read English prose in documentation and content drafts. It is useful when a team wants lightweight style feedback inside editors, scripts, or CI checks."
github_stars: 5065
verification: "security_reviewed"
source: "https://github.com/btford/write-good"
category: "Content Writing & SEO"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "btford/write-good"
  github_stars: 5065
  npm_package: "write-good"
  npm_weekly_downloads: 49520
---

# write-good English Prose Linting for Technical Content

This skill uses write-good to flag vague, wordy, or hard-to-read English prose in documentation and content drafts. It is useful when a team wants lightweight style feedback inside editors, scripts, or CI checks.

## Installation

Use the upstream install or setup path that matches your environment:
- npm install write-good
- npm install -g write-good
- If you have npm version 5.2.0 or later installed, you can use npx to run write-good without installing it:
- npx write-good *.md

Requirements and caveats from upstream:
- var writeGood = require('write-good');
- var schreibGut = require('schreib-gut');
- write-good takes a [glob](https://github.com/isaacs/node-glob) and prints suggestions to stdout:

Basic usage or getting-started notes:
- Like this, you can check non-English documents, for example with the linter extension for German, [schreib-gut](https://github.com/TimKam/schreib-gut):
- For example, normally only would be picked up as a bad word to use, but you might want to exempt read-only from that:
- You can run just specific checks like this:

- Source: https://github.com/btford/write-good
- Extracted from upstream docs: https://raw.githubusercontent.com/btford/write-good/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/write-good-english-prose-linting-technical-content/)
