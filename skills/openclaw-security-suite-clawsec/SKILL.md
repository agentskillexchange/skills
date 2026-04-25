---
title: "OpenClaw Security Suite (ClawSec)"
description: "Agent-layer security monitoring, drift detection, and integrity verification for OpenClaw environments. Protects cognitive architecture files, audits skill supply chains, and monitors CVE advisories."
verification: "security_reviewed"
source: "https://github.com/prompt-security/clawsec"
category:
  - "Security & Verification"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "prompt-security/clawsec"
  github_stars: 923
---

# OpenClaw Security Suite (ClawSec)

ClawSec is a security skill suite that protects your agent environment at the cognitive layer. It detects configuration drift in critical files like SOUL.md, monitors CVE advisories relevant to agent platforms, verifies skill integrity with checksums, and runs automated security audits. Best for Production OpenClaw deployments needing security monitoring Protecting against prompt injection and supply-chain attacks on installed skills Configuration drift detection for agent identity files Automated security audits with reporting How it differs from Healthcheck Security Hardening Healthcheck operates at the host/OS level — SSH, firewalls, system updates. ClawSec operates at the agent/cognitive layer — prompt integrity, skill supply chain, runtime behavior, and identity file protection. Install notes Install via npx clawhub@latest install clawsec-suite and follow setup prompts. Individual components (soul-guardian, audit-watchdog) can also be installed separately. Requires OpenClaw and the ClawHub CLI. Source: github.com/prompt-security/clawsec

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/openclaw-security-suite-clawsec/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/openclaw-security-suite-clawsec
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/openclaw-security-suite-clawsec`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openclaw-security-suite-clawsec/)
