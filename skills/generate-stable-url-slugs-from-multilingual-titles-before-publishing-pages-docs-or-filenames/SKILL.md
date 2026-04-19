---
title: "Generate stable URL slugs from multilingual titles before publishing pages, docs, or filenames"
description: "Tool: python-slugify This skill gives an agent a clean, bounded way to turn human-written titles into stable machine-safe slugs. python-slugify is useful when titles include spaces, punctuation, accented characters, non-Latin scripts, or inconsistent separators and the next automation step needs a predictable string for a URL, filename, content key, or folder name. The agent behavior is straightforward: take raw text, normalize entities and punctuation, transliterate Unicode when needed, apply stopword and separator rules, honor length limits, and emit a slug that can be reused consistently across systems. Invoke this skill before creating pages, docs, image filenames, knowledge-base articles, export bundles, or database records where the identifier needs to be readable and repeatable. It is particularly strong in multilingual publishing or ingestion workflows, where a basic lowercase-and-dashes helper often breaks on real-world input. The scope boundary is what keeps this from becoming a generic product card. This skill does not publish the page, manage redirects, choose SEO keywords, or operate a CMS. It does one narrow job: convert source text into a slug under clear rules. That narrow boundary makes it easy to compose with site generators, CMS APIs, file storage jobs, content migration scripts, and naming conventions enforced elsewhere. Typical integration points include WordPress or headless CMS creation flows, static-site generators, file packaging jobs, docs repositories, and import pipelines that need stable identifiers before writing records downstream."
source: "https://github.com/un33k/python-slugify"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "un33k/python-slugify"
  github_stars: 1604
---

# Generate stable URL slugs from multilingual titles before publishing pages, docs, or filenames

Tool: python-slugify This skill gives an agent a clean, bounded way to turn human-written titles into stable machine-safe slugs. python-slugify is useful when titles include spaces, punctuation, accented characters, non-Latin scripts, or inconsistent separators and the next automation step needs a predictable string for a URL, filename, content key, or folder name. The agent behavior is straightforward: take raw text, normalize entities and punctuation, transliterate Unicode when needed, apply stopword and separator rules, honor length limits, and emit a slug that can be reused consistently across systems. Invoke this skill before creating pages, docs, image filenames, knowledge-base articles, export bundles, or database records where the identifier needs to be readable and repeatable. It is particularly strong in multilingual publishing or ingestion workflows, where a basic lowercase-and-dashes helper often breaks on real-world input. The scope boundary is what keeps this from becoming a generic product card. This skill does not publish the page, manage redirects, choose SEO keywords, or operate a CMS. It does one narrow job: convert source text into a slug under clear rules. That narrow boundary makes it easy to compose with site generators, CMS APIs, file storage jobs, content migration scripts, and naming conventions enforced elsewhere. Typical integration points include WordPress or headless CMS creation flows, static-site generators, file packaging jobs, docs repositories, and import pipelines that need stable identifiers before writing records downstream.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/generate-stable-url-slugs-from-multilingual-titles-before-publishing-pages-docs-or-filenames/)
