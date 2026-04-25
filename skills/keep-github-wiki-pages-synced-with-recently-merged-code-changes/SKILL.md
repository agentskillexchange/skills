---
title: "Keep GitHub wiki pages synced with recently merged code changes"
description: "This entry turns GitHub Next’s Agentic Wiki Writer into a documentation-maintenance workflow. The agent watches for recent merges, reads the PAGES.md template, updates only the relevant wiki pages, and opens follow-up changes when the source structure itself needs adjustment."
verification: "security_reviewed"
source: "https://github.com/githubnext/agentics/blob/main/docs/agentic-wiki-writer.md"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "githubnext/agentics"
  github_stars: 585
---

# Keep GitHub wiki pages synced with recently merged code changes

This entry is built from GitHub Next’s Agentic Wiki Writer workflow in the githubnext/agentics repository. The workflow is explicitly designed to keep a GitHub wiki synchronized with a codebase by using a PAGES.md template and the set of recently merged pull requests. That makes it a genuine agent workflow rather than a catalog card for GitHub wikis. The agent’s job is to detect whether merges happened, read or generate the wiki template, identify the files affected by those merges, and then rewrite only the wiki pages that should change. You invoke this when a repository wants living wiki documentation that tracks source changes without forcing maintainers to hand-edit every page after each merge. It is useful for internal architecture notes, onboarding guides, API overviews, and operational docs that live in the GitHub wiki instead of a separate site. The scope boundary is important: this entry is specifically about template-driven wiki synchronization against recent code changes. It is not a generic documentation platform listing, not a generic content generator, and not a broad “write docs for anything” promise. Integration points include GitHub Actions scheduling or manual dispatch, GitHub wiki support enabled on the repository, the gh CLI plus the gh-aw extension, and the .github/agentic-wiki/PAGES.md file that defines page structure. The upstream workflow also supports a regenerate-template input for the first run. Because it operates on a defined wiki target, a bounded template, and a recent-merge window, it stays narrow enough to be a real operator task instead of a dressed-up product description.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/keep-github-wiki-pages-synced-with-recently-merged-code-changes/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/keep-github-wiki-pages-synced-with-recently-merged-code-changes
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/keep-github-wiki-pages-synced-with-recently-merged-code-changes`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/keep-github-wiki-pages-synced-with-recently-merged-code-changes/)
