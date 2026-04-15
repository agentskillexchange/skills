---
title: "Feroxbuster Fast Recursive Content Discovery Tool in Rust"
description: "Feroxbuster is a high-performance content discovery tool written in Rust that performs forced browsing attacks to enumerate hidden files, directories, and endpoints on web servers. It features recursive scanning, smart filtering, and extensive output options."
verification: security_reviewed
source: "https://github.com/epi052/feroxbuster"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "epi052/feroxbuster"
  github_stars: 7645
---

# Feroxbuster Fast Recursive Content Discovery Tool in Rust

Feroxbuster is a fast, simple, recursive content discovery tool written in Rust by epi052. It performs forced browsing (also known as predictable resource location or directory enumeration) to find web resources that are not directly linked or referenced by the target application but may still be accessible and contain sensitive information such as source code, credentials, or internal network details.

How It Works
Feroxbuster uses brute force combined with wordlists to systematically probe target directories for unlinked content. What sets it apart from similar tools like dirb, dirbuster, or gobuster is its recursive scanning capability — when it discovers a new directory, it automatically begins scanning that directory with the same wordlist. This depth-first approach uncovers deeply nested resources that flat scanners miss entirely.

Key Features
The tool supports multiple HTTP methods, custom headers, cookie injection, proxy routing, rate limiting, response filtering by status code/size/word count/line count, automatic calibration to reduce false positives, and output in JSON, CSV, or plain text formats. It can resume interrupted scans, supports multiple target URLs in a single run, and integrates with configuration files (ferox-config.toml) for persistent settings. The --auto-tune flag dynamically adjusts request rates based on server responses to avoid overwhelming targets.

Agent Integration
AI agents can invoke feroxbuster via CLI: feroxbuster -u https://target.com -w /path/to/wordlist.txt -o results.json --json. The JSON output mode provides structured data that agents can parse for downstream analysis. Agents can chain feroxbuster with other tools: use it after subdomain enumeration to discover content on each subdomain, or before vulnerability scanning to identify hidden endpoints worth testing. The tool is available via apt (Kali), brew, cargo, winget, chocolatey, and direct binary downloads.

Installation
On Kali Linux: sudo apt install feroxbuster. Via Homebrew: brew install feroxbuster. Via Cargo: cargo install feroxbuster. Self-update is built in: feroxbuster --update. Comprehensive documentation is available at epi052.github.io/feroxbuster-docs.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/feroxbuster-content-discovery
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/feroxbuster-content-discovery` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/feroxbuster-content-discovery/)
