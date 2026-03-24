---
name: "Dependency Audit"
description: "Use this skill when you need to audit npm, pip, cargo, or Maven dependencies for known vulnerabilities and outdated packages. It runs the appropriate package manager audit command, parses the output, and presents a prioritized list of security issues with remediation steps."
category: "Security & Verification"
framework: "Claude Code"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/dependency-audit/"
---

# Dependency Audit

Use this skill when you need to audit npm, pip, cargo, or Maven dependencies for known vulnerabilities and outdated packages. It runs the appropriate package manager audit command, parses the output, and presents a prioritized list of security issues with remediation steps.

## Overview

Use this skill when you need to audit npm, pip, cargo, or Maven dependencies for known vulnerabilities and outdated packages. It runs the appropriate package manager audit command, parses the output, and presents a prioritized list of security issues with remediation steps.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dependency-audit
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dependency-audit -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dependency-audit -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dependency-audit -a codex
```

### OpenClaw

```bash
clawhub install dependency-audit
```

## Source

- Marketplace: https://agentskillexchange.com/skills/dependency-audit/
