---
title: "Betterleaks Next-Generation Secrets Scanner"
description: "A fast, configurable secrets scanner built by the creator of Gitleaks and backed by Aikido Security. Betterleaks detects leaked passwords, API keys, and tokens in git repositories, directories, and stdin with CEL-based validation and parallelized scanning."
slug: "betterleaks-secrets-scanner"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Code"
verification: "security_reviewed"
source: "https://github.com/betterleaks/betterleaks"
tool_ecosystem:
  github_repo: "betterleaks/betterleaks"
  github_stars: 712
---

# Betterleaks Next-Generation Secrets Scanner

A fast, configurable secrets scanner built by the creator of Gitleaks and backed by Aikido Security. Betterleaks detects leaked passwords, API keys, and tokens in git repositories, directories, and stdin with CEL-based validation and parallelized scanning.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install betterleaks-secrets-scanner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Betterleaks is an open-source secrets detection tool that scans git repositories, directories, and standard input for leaked credentials including passwords, API keys, tokens, and other sensitive data. Built by Zach Rice, the original creator of Gitleaks (26 million+ downloads), Betterleaks represents the next generation of the tool with significant improvements in speed, configurability, and detection accuracy.
The scanner uses regex-based pattern matching combined with a token efficiency filter that reduces false positives by evaluating whether detected strings actually look like real secrets rather than test data or documentation examples. For confirmed detections, Betterleaks supports CEL (Common Expression Language) based validation rules that can fire HTTP requests to verify whether a detected secret is actually live and active, rather than revoked or expired.
Performance is a core design goal. Betterleaks supports parallelized git scanning through the --git-workers flag, distributing commit analysis across multiple threads for faster results on large repositories. Benchmarks against Gitleaks show measurably faster scan times on real-world repos. The tool also supports switching between regex engines (stdlib and RE2) for different performance characteristics.
Configuration uses TOML files with a syntax compatible with existing Gitleaks configurations, providing a smooth migration path. The default rule set ships with expanded coverage compared to Gitleaks, detecting secrets from a wider range of services and platforms. Developers can extend rules with custom patterns, allowlists, and validation logic.
Installation is available through Homebrew, Fedora DNF, Docker (via GHCR), or building from source. The CLI provides three scanning modes: git for repository history, dir for file system scanning, and stdin for pipeline integration. Output includes the secret location, matched rule, entropy score, commit metadata, and author information for git scans.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/betterleaks-secrets-scanner/)
