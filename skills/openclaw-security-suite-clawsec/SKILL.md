---
title: "OpenClaw Security Suite (ClawSec)"
description: "ClawSec is a security skill suite that protects your agent environment at the cognitive layer. It detects configuration drift in critical files like SOUL.md, monitors CVE advisories relevant to agent platforms, verifies skill integrity with checksums, and runs automated security audits.\nBest for\n\nProduction OpenClaw deployments needing security monitoring\nProtecting against prompt injection and supply-chain attacks on installed skills\nConfiguration drift detection for agent identity files\nAutomated security audits with reporting\n\nHow it differs from Healthcheck Security Hardening\nHealthcheck operates at the host/OS level — SSH, firewalls, system updates. ClawSec operates at the agent/cognitive layer — prompt integrity, skill supply chain, runtime behavior, and identity file protection.\nInstall notes\nInstall via npx clawhub@latest install clawsec-suite and follow setup prompts. Individual components (soul-guardian, audit-watchdog) can also be installed separately. Requires OpenClaw and the ClawHub CLI.\nSource: github.com/prompt-security/clawsec"
verification: security_reviewed
source: "https://github.com/prompt-security/clawsec"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "prompt-security/clawsec"
  github_stars: 900
---

# OpenClaw Security Suite (ClawSec)

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

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/openclaw-security-suite-clawsec
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/openclaw-security-suite-clawsec` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openclaw-security-suite-clawsec/)
