---
name: "Gutenberg block.json Schema Linter"
description: "Validates Gutenberg block.json files, asset handles, supports flags, transforms, and editor script registrations against the block metadata schema used by WordPress core. It helps catch registration mistakes before npm builds, plugin zips, or wp-env test runs reach QA."
category: "WordPress & CMS"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/gutenberg-block-json-schema-linter-20260324/"
---

# Gutenberg block.json Schema Linter

Validates Gutenberg block.json files, asset handles, supports flags, transforms, and editor script registrations against the block metadata schema used by WordPress core. It helps catch registration mistakes before npm builds, plugin zips, or wp-env test runs reach QA.

## Overview

This skill reviews **Gutenberg** block metadata with a focus on `block.json`, asset registration, and schema correctness. It checks required fields such as `name`, `title`, `category`, `attributes`, `supports`, and asset references like `editorScript`, `style`, or `render`. It also looks for mismatches between metadata and the actual JavaScript or PHP implementation, such as transform definitions that reference missing blocks, unsupported features exposed in the editor, or handles that are never registered. This is especially useful in block libraries that mix webpack builds, @wordpress/scripts, custom webpack/Vite pipelines, and PHP-rendered dynamic blocks.

The workflow can lint a single block, an entire plugin, or a monorepo of blocks, then emit a report with errors, warnings, and recommended fixes. It integrates well with npm scripts, GitHub Actions, wp-env, PHPUnit, Playwright editor tests, and release packaging steps that need predictable validation. The outputs may include a JSON diagnostics file, a human-readable Markdown summary, and a checklist for release engineering or code review. When used in CI/CD, it becomes a guardrail that catches schema regressions before a plugin ships to production. In practice, the skill functions like a block metadata API checker, build-time validator, and documentation helper rolled into one.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-json-schema-linter-20260324
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-json-schema-linter-20260324 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-json-schema-linter-20260324 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill gutenberg-block-json-schema-linter-20260324 -a codex
```

### OpenClaw

```bash
clawhub install gutenberg-block-json-schema-linter-20260324
```

## Source

- Marketplace: https://agentskillexchange.com/skills/gutenberg-block-json-schema-linter-20260324/
