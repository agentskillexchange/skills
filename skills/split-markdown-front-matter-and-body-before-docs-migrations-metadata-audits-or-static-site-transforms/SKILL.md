---
title: "Split Markdown front matter and body before docs migrations, metadata audits, or static-site transforms"
description: "Use gray-matter when an agent needs to open Markdown or content files, extract structured front matter, and pass clean body text plus metadata into the next step. This skill is for parsing and rewriting front matter safely, not for running a full CMS or static site generator."
verification: security_reviewed
source: "https://github.com/jonschlinkert/gray-matter"
category:
  - "Content Writing & SEO"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jonschlinkert/gray-matter"
  github_stars: 4415
---

# Split Markdown front matter and body before docs migrations, metadata audits, or static-site transforms

Tool: gray-matter

This skill is for agents that need to split a content file into two dependable parts: structured metadata and the real body content. gray-matter is a mature parser used across Markdown and static-site workflows, and it is a good fit when an agent has to inspect or transform files that begin with YAML front matter, or in some cases JSON, TOML, or other supported formats. The agent behavior here is concrete: open a file or string, extract the front matter into structured fields, preserve the main body without the metadata wrapper, and optionally write updated front matter back out after linting, migration, or normalization.

Invoke this skill when the job is things like migrating docs between systems, auditing missing metadata fields, generating reports from Markdown collections, or updating front matter keys in bulk before a build. It is especially useful when another downstream step needs clean separation between metadata and content instead of brittle regex scraping.

The scope boundary matters. This is not a CMS, not a site generator, and not a content strategy tool. It does not decide what your taxonomy should be, publish pages, build routes, or render a website. It only handles the bounded file-parsing step around front matter and content, which is exactly why it works as a reusable agent skill.

Common integration points include Markdown repos, docs automation, static-site pipelines, content QA jobs, migration scripts, and any agent flow that needs structured metadata before further transformation.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/split-markdown-front-matter-and-body-before-docs-migrations-metadata-audits-or-static-site-transforms
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/split-markdown-front-matter-and-body-before-docs-migrations-metadata-audits-or-static-site-transforms` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/split-markdown-front-matter-and-body-before-docs-migrations-metadata-audits-or-static-site-transforms/)
