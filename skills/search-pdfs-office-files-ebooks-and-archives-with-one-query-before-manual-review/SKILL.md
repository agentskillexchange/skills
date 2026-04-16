---
title: "Search PDFs, Office files, ebooks, and archives with one query before manual review"
description: "Uses ripgrep-all to run one full-text search across mixed document and archive formats so an agent can find evidence without separately extracting every file type first. Best when a workflow has PDFs, Office documents, ebooks, media sidecars, or compressed bundles that need fast on-demand search."
verification: "security_reviewed"
source: "https://github.com/phiresky/ripgrep-all"
category:
  - "Research &amp; Scraping"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/search-pdfs-office-files-ebooks-and-archives-with-one-query-before-manual-review/)
