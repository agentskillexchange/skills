---
name: "PR Code Review Checklist Generator"
description: "Reads a GitHub pull request diff and generates a structured review checklist covering security, performance, test coverage, and style concerns specific to the changed files. Detects language and framework from the diff. Outputs ready-to-paste Markdown."
category: "Code Quality & Review"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/pr-code-review-checklist-generator/"
---

# PR Code Review Checklist Generator

Reads a GitHub pull request diff and generates a structured review checklist covering security, performance, test coverage, and style concerns specific to the changed files. Detects language and framework from the diff. Outputs ready-to-paste Markdown.

## Overview

Reads a GitHub pull request diff and generates a structured review checklist covering security, performance, test coverage, and style concerns specific to the changed files. Detects language and framework from the diff. Outputs ready-to-paste Markdown.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pr-code-review-checklist-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pr-code-review-checklist-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pr-code-review-checklist-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pr-code-review-checklist-generator -a codex
```

### OpenClaw

```bash
clawhub install pr-code-review-checklist-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/pr-code-review-checklist-generator/
