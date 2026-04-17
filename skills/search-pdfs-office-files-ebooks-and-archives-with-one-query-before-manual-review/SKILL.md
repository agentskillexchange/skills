---
title: "Search PDFs, Office files, ebooks, and archives with one query before manual review"
description: "This skill wraps `ripgrep-all` (`rga`) as a bounded retrieval workflow for heterogeneous document collections. An agent should invoke it when the working set includes PDFs, Office files, ebooks, archives, or other non-plain-text assets and the immediate goal is to locate evidence, names, phrases, IDs, or other keywords before doing deeper review. That makes it useful for investigations, due diligence, compliance sweeps, migration audits, support triage, and any research task where the fastest next step is finding which files are relevant.\nThe scope boundary keeps this from collapsing into a generic search product listing. This skill is not a hosted index, document-management system, or general desktop search replacement. The agent is using the upstream CLI to run targeted searches across a local corpus on demand, relying on `ripgrep-all` adapters to extract searchable text from supported formats. If the task needs long-lived indexing, semantic retrieval, or a full knowledge base, the agent should use a different tool.\nIntegration points are practical and agent-friendly. Point the workflow at a directory of attachments, exports, or archive dumps, run `rga` with the search term, then pass matching paths and snippets into summarization, escalation, tagging, or evidence-pack generation. Upstream documentation shows installation through package managers such as Homebrew (`brew install rga`) or Cargo (`cargo install –locked ripgrep_all`). The README also documents adapter dependencies like `ripgrep`, `pandoc`, `poppler`, and `ffmpeg`, which expand the file types the agent can search in one pass."
verification: security_reviewed
source: "https://github.com/phiresky/ripgrep-all"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "phiresky/ripgrep-all"
  github_stars: 9573
---

# Search PDFs, Office files, ebooks, and archives with one query before manual review

This skill wraps `ripgrep-all` (`rga`) as a bounded retrieval workflow for heterogeneous document collections. An agent should invoke it when the working set includes PDFs, Office files, ebooks, archives, or other non-plain-text assets and the immediate goal is to locate evidence, names, phrases, IDs, or other keywords before doing deeper review. That makes it useful for investigations, due diligence, compliance sweeps, migration audits, support triage, and any research task where the fastest next step is finding which files are relevant.
The scope boundary keeps this from collapsing into a generic search product listing. This skill is not a hosted index, document-management system, or general desktop search replacement. The agent is using the upstream CLI to run targeted searches across a local corpus on demand, relying on `ripgrep-all` adapters to extract searchable text from supported formats. If the task needs long-lived indexing, semantic retrieval, or a full knowledge base, the agent should use a different tool.
Integration points are practical and agent-friendly. Point the workflow at a directory of attachments, exports, or archive dumps, run `rga` with the search term, then pass matching paths and snippets into summarization, escalation, tagging, or evidence-pack generation. Upstream documentation shows installation through package managers such as Homebrew (`brew install rga`) or Cargo (`cargo install –locked ripgrep_all`). The README also documents adapter dependencies like `ripgrep`, `pandoc`, `poppler`, and `ffmpeg`, which expand the file types the agent can search in one pass.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/search-pdfs-office-files-ebooks-and-archives-with-one-query-before-manual-review
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/search-pdfs-office-files-ebooks-and-archives-with-one-query-before-manual-review` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-pdfs-office-files-ebooks-and-archives-with-one-query-before-manual-review/)
