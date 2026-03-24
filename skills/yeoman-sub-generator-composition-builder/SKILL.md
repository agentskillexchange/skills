---
name: "Yeoman Sub-Generator Composition Builder"
description: "Orchestrates Yeoman generator composition by chaining sub-generators via the Yeoman Environment API. Manages yo run loops, priority queues, and cross-generator dependency resolution."
category: "41"
framework: "35"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/yeoman-sub-generator-composition-builder/"
---

# Yeoman Sub-Generator Composition Builder

Orchestrates Yeoman generator composition by chaining sub-generators via the Yeoman Environment API. Manages yo run loops, priority queues, and cross-generator dependency resolution.

## Overview

The Yeoman Sub-Generator Composition Builder automates complex project generation workflows by orchestrating multiple Yeoman sub-generators through the yeoman-environment API. It uses the composeWith() method to chain generators in dependency order, managing the Yeoman run loop priority queue to ensure initializing, prompting, configuring, writing, and install phases execute correctly across composed generators. The skill resolves generator dependencies from the npm registry, checking for locally installed generators via yo –generators and installing missing ones on demand. It handles cross-generator conflict resolution using the Yeoman conflicter with configurable merge strategies for shared files like package.json and tsconfig.json. The skill supports both local generators in the generators/ directory and published npm generator packages prefixed with generator-. It can replay stored answers from .yo-rc.json for reproducible scaffolding and manages the Yeoman storage API for persisting configuration across sub-generator boundaries.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill yeoman-sub-generator-composition-builder
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill yeoman-sub-generator-composition-builder -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill yeoman-sub-generator-composition-builder -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill yeoman-sub-generator-composition-builder -a codex
```

### OpenClaw

```bash
clawhub install yeoman-sub-generator-composition-builder
```

## Source

- Marketplace: https://agentskillexchange.com/skills/yeoman-sub-generator-composition-builder/
