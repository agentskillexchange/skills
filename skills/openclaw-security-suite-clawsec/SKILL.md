---
name: "OpenClaw Security Suite (ClawSec)"
description: "Agent-layer security monitoring, drift detection, and integrity verification for OpenClaw environments. Protects cognitive architecture files, audits skill supply chains, and monitors CVE advisories."
category: "Security &amp; Verification"
framework: "OpenClaw"
verification: security_reviewed
source: "https://github.com/prompt-security/clawsec"
tool_ecosystem:
  github_repo: "prompt-security/clawsec"
  github_stars: 867
---
# OpenClaw Security Suite (ClawSec)

Agent-layer security monitoring, drift detection, and integrity verification for OpenClaw environments. Protects cognitive architecture files, audits skill supply chains, and monitors CVE advisories.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill openclaw-security-suite-clawsec
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill openclaw-security-suite-clawsec -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill openclaw-security-suite-clawsec -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill openclaw-security-suite-clawsec -a codex
```

### OpenClaw

```bash
clawhub install openclaw-security-suite-clawsec
```

## Details

ClawSec is a security skill suite that protects your agent environment at the cognitive layer. It detects configuration drift in critical files like SOUL.md, monitors CVE advisories relevant to agent platforms, verifies skill integrity with checksums, and runs automated security audits.

Best for

Production OpenClaw deployments needing security monitoring
Protecting against prompt injection and supply-chain attacks on installed skills
Configuration drift detection for agent identity files
Automated security audits with reporting

How it differs from Healthcheck Security Hardening
Healthcheck operates at the host/OS level — SSH, firewalls, system updates. ClawSec operates at the agent/cognitive layer — prompt integrity, skill supply chain, runtime behavior, and identity file protection.

Install notes
Install via npx clawhub@latest install clawsec-suite and follow setup prompts. Individual components (soul-guardian, audit-watchdog) can also be installed separately. Requires OpenClaw and the ClawHub CLI.

Source: github.com/prompt-security/clawsec

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openclaw-security-suite-clawsec/)
