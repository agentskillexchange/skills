---
title: "Generate stable URL slugs from multilingual titles before publishing pages, docs, or filenames"
description: "Use python-slugify when an agent has messy human titles and needs safe, repeatable slugs for URLs, filenames, or record IDs. This skill stays tightly focused on transliteration and normalization, not routing, redirects, or full publishing workflows."
verification: "security_reviewed"
source: "https://github.com/un33k/python-slugify"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "un33k/python-slugify"
  github_stars: 1604
---

# Generate stable URL slugs from multilingual titles before publishing pages, docs, or filenames

Tool: python-slugify

This skill gives an agent a clean, bounded way to turn human-written titles into stable machine-safe slugs. python-slugify is useful when titles include spaces, punctuation, accented characters, non-Latin scripts, or inconsistent separators and the next automation step needs a predictable string for a URL, filename, content key, or folder name. The agent behavior is straightforward: take raw text, normalize entities and punctuation, transliterate Unicode when needed, apply stopword and separator rules, honor length limits, and emit a slug that can be reused consistently across systems.

Invoke this skill before creating pages, docs, image filenames, knowledge-base articles, export bundles, or database records where the identifier needs to be readable and repeatable. It is particularly strong in multilingual publishing or ingestion workflows, where a basic lowercase-and-dashes helper often breaks on real-world input.

The scope boundary is what keeps this from becoming a generic product card. This skill does not publish the page, manage redirects, choose SEO keywords, or operate a CMS. It does one narrow job: convert source text into a slug under clear rules. That narrow boundary makes it easy to compose with site generators, CMS APIs, file storage jobs, content migration scripts, and naming conventions enforced elsewhere.

Typical integration points include WordPress or headless CMS creation flows, static-site generators, file packaging jobs, docs repositories, and import pipelines that need stable identifiers before writing records downstream.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-stable-url-slugs-from-multilingual-titles-before-publishing-pages-docs-or-filenames/)
