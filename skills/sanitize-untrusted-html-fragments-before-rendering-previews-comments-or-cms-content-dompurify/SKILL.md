---
title: "Sanitize untrusted HTML fragments before rendering previews, comments, or CMS content with DOMPurify"
description: "Use DOMPurify when an agent must accept HTML from users, rich text editors, imports, or model output but cannot safely render it as-is. The skill strips dangerous markup and unsafe attributes before the content is shown in previews, stored in CMS fields, or embedded in downstream pages."
verification: security_reviewed
source: "https://github.com/cure53/DOMPurify"
category:
  - "Security & Verification"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "cure53/DOMPurify"
  github_stars: 16854
---

# Sanitize untrusted HTML fragments before rendering previews, comments, or CMS content with DOMPurify

Use DOMPurify when an agent must accept HTML from users, rich text editors, imports, or model output but cannot safely render it as-is. The skill strips dangerous markup and unsafe attributes before the content is shown in previews, stored in CMS fields, or embedded in downstream pages.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/sanitize-untrusted-html-fragments-before-rendering-previews-comments-or-cms-content-dompurify/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/sanitize-untrusted-html-fragments-before-rendering-previews-comments-or-cms-content-dompurify
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/sanitize-untrusted-html-fragments-before-rendering-previews-comments-or-cms-content-dompurify`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sanitize-untrusted-html-fragments-before-rendering-previews-comments-or-cms-content-dompurify/)
