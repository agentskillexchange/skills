---
title: "Sanitize untrusted HTML fragments before rendering previews, comments, or CMS content with DOMPurify"
slug: "sanitize-untrusted-html-fragments-before-rendering-previews-comments-or-cms-content-dompurify"
verification: security_reviewed
source: "https://github.com/cure53/DOMPurify"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "cure53/DOMPurify"
  github_stars: 16854
---
# Sanitize untrusted HTML fragments before rendering previews, comments, or CMS content with DOMPurify

Use DOMPurify when an agent must accept HTML from users, rich text editors, imports, or model output but cannot safely render it as-is. The skill strips dangerous markup and unsafe attributes before the content is shown in previews, stored in CMS fields, or embedded in downstream pages.

## Installation

Choose the method that fits your setup:

1. Install from Agent Skill Exchange
2. Clone or download the upstream project
3. Install with the upstream package manager
4. Add the skill to your local skills directory
5. Follow the upstream documentation for environment-specific setup

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sanitize-untrusted-html-fragments-before-rendering-previews-comments-or-cms-content-dompurify/)
