---
name: "Security Audit Skill"
description: "Use this skill to perform automated security audits covering OWASP Top 10 vulnerabilities and dependency CVE scanning on codebases and projects. It identifies SQL injection risks, XSS vulnerabilities, insecure configurations, and known vulnerable dependencies. Trigger when preparing for security review, before deployments, or when assessing new codebases for vulnerabilities."
category: "Security & Verification"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/security-audit-skill/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "owasp"  # from ase_tool_match
  github_stars: 14896  # from ase_github_stars (integer, not string)
  github_repo: "zaproxy/zaproxy"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Security Audit Skill

Use this skill to perform automated security audits covering OWASP Top 10 vulnerabilities and dependency CVE scanning on codebases and projects. It identifies SQL injection risks, XSS vulnerabilities, insecure configurations, and known vulnerable dependencies. Trigger when preparing for security review, before deployments, or when assessing new codebases for vulnerabilities.

## Overview

Use this skill to perform automated security audits covering OWASP Top 10 vulnerabilities and dependency CVE scanning on codebases and projects. It identifies SQL injection risks, XSS vulnerabilities, insecure configurations, and known vulnerable dependencies. Trigger when preparing for security review, before deployments, or when assessing new codebases for vulnerabilities.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill security-audit-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill security-audit-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill security-audit-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill security-audit-skill -a codex
```

### OpenClaw

```bash
clawhub install security-audit-skill
```

## Source

- Marketplace: https://agentskillexchange.com/skills/security-audit-skill/
