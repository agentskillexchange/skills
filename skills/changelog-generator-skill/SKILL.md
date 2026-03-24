---
name: "Changelog Generator Skill"
description: "Use this skill to parse git commit history and automatically generate a structured CHANGELOG.md following the Keep a Changelog convention. It categorizes commits into Added, Changed, Fixed, Deprecated, Removed, and Security sections. Trigger when preparing a release and needing to document changes since the last version."
category: "Developer Tools"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/changelog-generator-skill/"
---

# Changelog Generator Skill

Use this skill to parse git commit history and automatically generate a structured CHANGELOG.md following the Keep a Changelog convention. It categorizes commits into Added, Changed, Fixed, Deprecated, Removed, and Security sections. Trigger when preparing a release and needing to document changes since the last version.

## Overview

Use this skill to parse git commit history and automatically generate a structured CHANGELOG.md following the Keep a Changelog convention. It categorizes commits into Added, Changed, Fixed, Deprecated, Removed, and Security sections. Trigger when preparing a release and needing to document changes since the last version.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill changelog-generator-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill changelog-generator-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill changelog-generator-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill changelog-generator-skill -a codex
```

### OpenClaw

```bash
clawhub install changelog-generator-skill
```

## Source

- Marketplace: https://agentskillexchange.com/skills/changelog-generator-skill/
