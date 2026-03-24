---
name: "Substack Formatter"
description: "Convert plain text into Substack-ready HTML that preserves headings, emphasis, and lists on paste."
category: "Content Writing & SEO"
framework: "OpenClaw"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/substack-formatter/"
---

# Substack Formatter

Convert plain text into Substack-ready HTML that preserves headings, emphasis, and lists on paste.

## Overview

Substack Formatter turns rough plain text into HTML that pastes cleanly into the Substack editor. Instead of manually rebuilding headings, emphasis, spacing, and list structure after every paste, it handles the formatting layer so the writing workflow stays fast.

Best for

turning plain draft text into Substack-ready HTML

preserving bold, italic, headings, and bullets during paste

speeding up newsletter publishing workflows

Install notes

Install the skill in an OpenClaw workspace with Python available. The bundled formatter and copy helpers handle HTML generation and clipboard-friendly output for Substack.

**Source:** OpenClaw-compatible Substack formatter skill.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill substack-formatter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill substack-formatter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill substack-formatter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill substack-formatter -a codex
```

### OpenClaw

```bash
clawhub install substack-formatter
```

## Source

- Marketplace: https://agentskillexchange.com/skills/substack-formatter/
