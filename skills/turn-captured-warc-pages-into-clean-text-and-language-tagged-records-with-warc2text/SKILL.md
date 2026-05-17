---
name: "Turn captured WARC pages into clean text and language-tagged records with warc2text"
slug: "turn-captured-warc-pages-into-clean-text-and-language-tagged-records-with-warc2text"
description: "Use warc2text when an agent already has WARC captures and needs readable text, language identification, and exportable records for review, search, or corpus building instead of re-crawling pages."
github_stars: 23
verification: "security_reviewed"
source: "https://github.com/bitextor/warc2text"
author: "Bitextor contributors"
publisher_type: "open_source_project"
category: "Data Extraction & Transformation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "bitextor/warc2text"
  github_stars: 23
---

# Turn captured WARC pages into clean text and language-tagged records with warc2text

Use warc2text when an agent already has WARC captures and needs readable text, language identification, and exportable records for review, search, or corpus building instead of re-crawling pages.

## Prerequisites

warc2text build or binary, WARC input files, local output storage

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

Install command or upstream instructions:

```
Install the documented build dependencies, build or install warc2text, then run `warc2text -o <output_folder> [options] <warc_file>...` to emit text, HTML, and metadata outputs from archived captures.
```

## Documentation

- https://github.com/bitextor/warc2text

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-captured-warc-pages-into-clean-text-and-language-tagged-records-with-warc2text/)
