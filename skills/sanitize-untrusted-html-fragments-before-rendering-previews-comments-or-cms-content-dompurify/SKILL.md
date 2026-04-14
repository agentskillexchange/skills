---
title: "Sanitize untrusted HTML fragments before rendering previews, comments, or CMS content with DOMPurify"
description: "Use DOMPurify when an agent must accept HTML from users, rich text editors, imports, or model output but cannot safely render it as-is. The skill strips dangerous markup and unsafe attributes before the content is shown in previews, stored in CMS fields, or embedded in downstream pages."
verification: security_reviewed
source: "https://github.com/cure53/DOMPurify"
category:
  - "Security &amp; Verification"
tool_ecosystem:
  github_repo: "cure53/DOMPurify"
  github_stars: 16854
---

# Sanitize untrusted HTML fragments before rendering previews, comments, or CMS content with DOMPurify

Use DOMPurify when an agent must accept HTML from users, rich text editors, imports, or model output but cannot safely render it as-is. The skill strips dangerous markup and unsafe attributes before the content is shown in previews, stored in CMS fields, or embedded in downstream pages.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/sanitize-untrusted-html-fragments-before-rendering-previews-comments-or-cms-content-dompurify/)
