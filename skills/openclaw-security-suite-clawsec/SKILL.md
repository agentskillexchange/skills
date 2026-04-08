---
title: OpenClaw Security Suite (ClawSec)
description: 'ClawSec is a security skill suite that protects your agent environment
  at the cognitive layer. It detects configuration drift in critical files like SOUL.md,
  monitors CVE advisories relevant to agent platforms, verifies skill integrity with
  checksums, and runs automated security audits. Best for Production OpenClaw deployments
  needing security monitoring Protecting against prompt injection and supply-chain
  attacks on installed skills Configuration drift detection for agent identity files
  Automated security audits with reporting How it differs from Healthcheck Security
  Hardening Healthcheck operates at the host/OS level — SSH, firewalls, system updates.
  ClawSec operates at the agent/cognitive layer — prompt integrity, skill supply chain,
  runtime behavior, and identity file protection. Install notes Install via npx clawhub@latest
  install clawsec-suite and follow setup prompts. Individual components (soul-guardian,
  audit-watchdog) can also be installed separately. Requires OpenClaw and the ClawHub
  CLI. Source: github.com/prompt-security/clawsec'
verification: security_reviewed
source: https://github.com/prompt-security/clawsec
category:
- Security &amp; Verification
framework:
- OpenClaw
tool_ecosystem:
  github_repo: prompt-security/clawsec
  github_stars: 867
---

# OpenClaw Security Suite (ClawSec)

ClawSec is a security skill suite that protects your agent environment at the cognitive layer. It detects configuration drift in critical files like SOUL.md, monitors CVE advisories relevant to agent platforms, verifies skill integrity with checksums, and runs automated security audits. Best for Production OpenClaw deployments needing security monitoring Protecting against prompt injection and supply-chain attacks on installed skills Configuration drift detection for agent identity files Automated security audits with reporting How it differs from Healthcheck Security Hardening Healthcheck operates at the host/OS level — SSH, firewalls, system updates. ClawSec operates at the agent/cognitive layer — prompt integrity, skill supply chain, runtime behavior, and identity file protection. Install notes Install via npx clawhub@latest install clawsec-suite and follow setup prompts. Individual components (soul-guardian, audit-watchdog) can also be installed separately. Requires OpenClaw and the ClawHub CLI. Source: github.com/prompt-security/clawsec

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openclaw-security-suite-clawsec/)
