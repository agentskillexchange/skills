---
title: "Turn captured WARC pages into clean text and language-tagged records with warc2text"
description: "Best for: research and archive workflows where web captures already exist as WARC files and the next step is turning them into usable text outputs. warc2text extracts plain text, HTML, metadata, and language information from WARC records. It can emit structured outputs, split multilingual content, and write language-organized results to disk. That makes it a sharp post-capture transformation skill rather than a generic scraping listing. When to invoke it Invoke this skill after collection, when an agent needs to convert archived WARC payloads into text-rich records for indexing, filtering, QA, or downstream NLP work. Scope boundary This is not a general archive platform listing. The skill boundary is a single conversion workflow: ingest WARC files, extract text and metadata, optionally classify language, and emit structured output files. Install notes Build or install warc2text with the documented system dependencies. Choose an output folder and desired output types. Run warc2text -o output_dir ... input.warc.gz against the capture set."
source: "https://github.com/bitextor/warc2text"
verification: "listed"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "bitextor/warc2text"
  github_stars: 23
---

# Turn captured WARC pages into clean text and language-tagged records with warc2text

Best for: research and archive workflows where web captures already exist as WARC files and the next step is turning them into usable text outputs. warc2text extracts plain text, HTML, metadata, and language information from WARC records. It can emit structured outputs, split multilingual content, and write language-organized results to disk. That makes it a sharp post-capture transformation skill rather than a generic scraping listing. When to invoke it Invoke this skill after collection, when an agent needs to convert archived WARC payloads into text-rich records for indexing, filtering, QA, or downstream NLP work. Scope boundary This is not a general archive platform listing. The skill boundary is a single conversion workflow: ingest WARC files, extract text and metadata, optionally classify language, and emit structured output files. Install notes Build or install warc2text with the documented system dependencies. Choose an output folder and desired output types. Run warc2text -o output_dir ... input.warc.gz against the capture set.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/turn-captured-warc-pages-into-clean-text-and-language-tagged-records-with-warc2text/)
