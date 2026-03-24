---
name: "Secret Scanner"
description: "Use this skill when you need to scan code, commits, or configuration files for accidentally committed secrets like API keys, passwords, and tokens. It runs tools like truffleHog or gitleaks and returns findings with file paths, line numbers, and severity levels."
category: "Security & Verification"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/secret-scanner/"
---

# Secret Scanner

Use this skill when you need to scan code, commits, or configuration files for accidentally committed secrets like API keys, passwords, and tokens. It runs tools like truffleHog or gitleaks and returns findings with file paths, line numbers, and severity levels.

## Overview

Use this skill when you need to scan code, commits, or configuration files for accidentally committed secrets like API keys, passwords, and tokens. It runs tools like truffleHog or gitleaks and returns findings with file paths, line numbers, and severity levels.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill secret-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill secret-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill secret-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill secret-scanner -a codex
```

### OpenClaw

```bash
clawhub install secret-scanner
```

## Source

- Marketplace: https://agentskillexchange.com/skills/secret-scanner/
