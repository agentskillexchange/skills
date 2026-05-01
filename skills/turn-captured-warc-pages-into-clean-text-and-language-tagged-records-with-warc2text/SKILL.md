---
title: "Turn captured WARC pages into clean text and language-tagged records with warc2text"
description: "Use warc2text when an agent already has WARC captures and needs readable text, language identification, and exportable records for review, search, or corpus building instead of re-crawling pages."
verification: "security_reviewed"
source: "https://github.com/bitextor/warc2text"
category:
  - "Data Extraction & Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bitextor/warc2text"
  github_stars: 23
---

# Turn captured WARC pages into clean text and language-tagged records with warc2text

Best for: research and archive workflows where web captures already exist as WARC files and the next step is turning them into usable text outputs.

warc2text extracts plain text, HTML, metadata, and language information from WARC records. It can emit structured outputs, split multilingual content, and write language-organized results to disk. That makes it a sharp post-capture transformation skill rather than a generic scraping listing.

When to invoke it
Invoke this skill after collection, when an agent needs to convert archived WARC payloads into text-rich records for indexing, filtering, QA, or downstream NLP work.

Scope boundary
This is not a general archive platform listing. The skill boundary is a single conversion workflow: ingest WARC files, extract text and metadata, optionally classify language, and emit structured output files.

Install notes

- Build or install warc2text with the documented system dependencies.

- Choose an output folder and desired output types.

- Run warc2text -o output_dir ... input.warc.gz against the capture set.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/turn-captured-warc-pages-into-clean-text-and-language-tagged-records-with-warc2text/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/turn-captured-warc-pages-into-clean-text-and-language-tagged-records-with-warc2text
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/turn-captured-warc-pages-into-clean-text-and-language-tagged-records-with-warc2text`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-captured-warc-pages-into-clean-text-and-language-tagged-records-with-warc2text/)
