---
title: "Betterleaks Next-Generation Secrets Scanner"
description: "A fast, configurable secrets scanner built by the creator of Gitleaks and backed by Aikido Security. Betterleaks detects leaked passwords, API keys, and tokens in git repositories, directories, and stdin with CEL-based validation and parallelized scanning."
verification: "security_reviewed"
source: "https://github.com/betterleaks/betterleaks"
category:
  - "Security & Verification"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/betterleaks-secrets-scanner/)
