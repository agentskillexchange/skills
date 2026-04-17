---
title: "Betterleaks Next-Generation Secrets Scanner"
description: "Betterleaks is an open-source secrets detection tool that scans git repositories, directories, and standard input for leaked credentials including passwords, API keys, tokens, and other sensitive data. Built by Zach Rice, the original creator of Gitleaks (26 million+ downloads), Betterleaks represents the next generation of the tool with significant improvements in speed, configurability, and detection accuracy.\nThe scanner uses regex-based pattern matching combined with a token efficiency filter that reduces false positives by evaluating whether detected strings actually look like real secrets rather than test data or documentation examples. For confirmed detections, Betterleaks supports CEL (Common Expression Language) based validation rules that can fire HTTP requests to verify whether a detected secret is actually live and active, rather than revoked or expired.\nPerformance is a core design goal. Betterleaks supports parallelized git scanning through the --git-workers flag, distributing commit analysis across multiple threads for faster results on large repositories. Benchmarks against Gitleaks show measurably faster scan times on real-world repos. The tool also supports switching between regex engines (stdlib and RE2) for different performance characteristics.\nConfiguration uses TOML files with a syntax compatible with existing Gitleaks configurations, providing a smooth migration path. The default rule set ships with expanded coverage compared to Gitleaks, detecting secrets from a wider range of services and platforms. Developers can extend rules with custom patterns, allowlists, and validation logic.\nInstallation is available through Homebrew, Fedora DNF, Docker (via GHCR), or building from source. The CLI provides three scanning modes: git for repository history, dir for file system scanning, and stdin for pipeline integration. Output includes the secret location, matched rule, entropy score, commit metadata, and author information for git scans."
verification: security_reviewed
source: "https://github.com/betterleaks/betterleaks"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "betterleaks/betterleaks"
  github_stars: 712
---

# Betterleaks Next-Generation Secrets Scanner

Betterleaks is an open-source secrets detection tool that scans git repositories, directories, and standard input for leaked credentials including passwords, API keys, tokens, and other sensitive data. Built by Zach Rice, the original creator of Gitleaks (26 million+ downloads), Betterleaks represents the next generation of the tool with significant improvements in speed, configurability, and detection accuracy.
The scanner uses regex-based pattern matching combined with a token efficiency filter that reduces false positives by evaluating whether detected strings actually look like real secrets rather than test data or documentation examples. For confirmed detections, Betterleaks supports CEL (Common Expression Language) based validation rules that can fire HTTP requests to verify whether a detected secret is actually live and active, rather than revoked or expired.
Performance is a core design goal. Betterleaks supports parallelized git scanning through the --git-workers flag, distributing commit analysis across multiple threads for faster results on large repositories. Benchmarks against Gitleaks show measurably faster scan times on real-world repos. The tool also supports switching between regex engines (stdlib and RE2) for different performance characteristics.
Configuration uses TOML files with a syntax compatible with existing Gitleaks configurations, providing a smooth migration path. The default rule set ships with expanded coverage compared to Gitleaks, detecting secrets from a wider range of services and platforms. Developers can extend rules with custom patterns, allowlists, and validation logic.
Installation is available through Homebrew, Fedora DNF, Docker (via GHCR), or building from source. The CLI provides three scanning modes: git for repository history, dir for file system scanning, and stdin for pipeline integration. Output includes the secret location, matched rule, entropy score, commit metadata, and author information for git scans.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/betterleaks-secrets-scanner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/betterleaks-secrets-scanner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/betterleaks-secrets-scanner/)
