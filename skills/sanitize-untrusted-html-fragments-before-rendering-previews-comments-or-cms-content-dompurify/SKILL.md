---
title: "Sanitize untrusted HTML fragments before rendering previews, comments, or CMS content with DOMPurify"
slug: "sanitize-untrusted-html-fragments-before-rendering-previews-comments-or-cms-content-dompurify"
verification: "listed"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
source: "https://github.com/cure53/DOMPurify"
tool_ecosystem:
  github_repo: "cure53/DOMPurify"
  github_stars: 16851
---

# Sanitize untrusted HTML fragments before rendering previews, comments, or CMS content with DOMPurify

Use DOMPurify when an agent must accept HTML from users, rich text editors, imports, or model output but cannot safely render it as-is. The skill strips dangerous markup and unsafe attributes before the content is shown in previews, stored in CMS fields, or embedded in downstream pages.

## Installation

Choose the method that fits your setup:

1. Clone or download this repo and copy the skill folder into your local skills directory.
2. Install from the Agent Skill Exchange repo with your preferred Git workflow.
3. Add the skill folder as a git submodule if you manage skills as dependencies.
4. Copy the files manually into a local custom-skills directory for testing.
5. Use any marketplace or sync tooling you already have for pulling ASE skills.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sanitize-untrusted-html-fragments-before-rendering-previews-comments-or-cms-content-dompurify/)
