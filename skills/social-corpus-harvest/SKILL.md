---
name: "Social Corpus Harvest"
slug: "social-corpus-harvest"
description: "Collects a human-verified person, creator, brand, or organization's self-authored public Xiaohongshu, Douyin, and Weibo posts through OpenCLI into a local Markdown dataset with stable source URLs, author checks, capture timestamps, and a provenance manifest. Use for public-content archives, knowledge bases, RAG ingestion, content audits, research datasets, and consented AI data preparation."
github_stars: 0
verification: "listed"
source: "https://github.com/yuwanpai2004-create/codex-skills"
author: "yuwanpai2004-create"
category: "Research & Scraping"
framework: "Codex"
tool_ecosystem:
  github_repo: "yuwanpai2004-create/codex-skills"
  github_stars: 0
---

# Social Corpus Harvest

Social Corpus Harvest is a reusable Codex workflow backed by the open-source
`yuwanpai2004-create/codex-skills` repository. It combines Agent Reach, OpenCLI,
the official OpenCLI Chrome extension, and bundled Python orchestration to
collect public posts from Xiaohongshu, Douyin, and Weibo. The workflow verifies
the target account before collection, strips temporary signed URL parameters,
checks authorship where the platform adapter permits it, and writes one
Markdown file per post plus a machine-readable source manifest.

Use it when scattered public posts need to become a traceable local archive,
knowledge base, RAG source, content-analysis dataset, migration package, or
consented AI persona/training candidate set. Do not use it to guess accounts,
collect private content, copy comments or fan edits, bypass platform
challenges, or obtain passwords, cookies, session tokens, or CAPTCHA answers.
Downloading or transcribing audio/video requires a separate user decision.
Collection does not itself grant republication, commercial-use, or
model-training rights.

## Installation

Install or set up from the source-backed instructions:

npx skills add yuwanpai2004-create/codex-skills --skill social-corpus-harvest -a codex

- Source: https://github.com/yuwanpai2004-create/codex-skills

## Prerequisites

- Python 3.10 or newer.
- Chrome controlled by the user.
- User approval before installing user-local Agent Reach, Node.js, or OpenCLI
  dependencies.
- The official OpenCLI Chrome extension and an explicit user login for each
  selected platform.
- Exact profile links and human-recorded account-verification evidence.

The bootstrap never uses `sudo`, never stores browser credentials, and fails
closed when the Browser Bridge or required adapter commands are unavailable.

## Workflow

1. Run `python scripts/bootstrap.py check --json`.
2. With user approval, run `python scripts/bootstrap.py install` if required.
3. Connect the official extension and let the user complete platform login.
4. Create `corpus/social_profiles.json` with
   `scripts/init_profile_map.py`, including verifier and evidence fields.
5. Run `scripts/harvest_social_corpus.py <OUT_DIR> --name <SUBJECT> --dry-run`.
6. Review the planned platforms and limits, then rerun without `--dry-run`.
7. Resolve every failed platform, spot-check Markdown against source URLs, and
   retain `corpus/public_social/source_manifest.json` with the dataset.

The complete upstream skill includes setup guidance, dependency pins, profile
schema documentation, collection scripts, and recovery behavior.
