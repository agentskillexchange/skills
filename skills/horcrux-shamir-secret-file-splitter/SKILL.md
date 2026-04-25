---
title: "Horcrux Shamir Secret Sharing File Encryption and Splitting Tool"
description: "Horcrux splits files into encrypted fragments using Shamir Secret Sharing, so you can distribute pieces across locations and reconstruct the original with a configurable threshold — no password required."
verification: "security_reviewed"
source: "https://github.com/jesseduffield/horcrux"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "jesseduffield/horcrux"
  github_stars: 5041
---

# Horcrux Shamir Secret Sharing File Encryption and Splitting Tool

Overview
Horcrux is a command-line tool by Jesse Duffield (creator of Lazygit and Lazydocker) that splits files into encrypted fragments using Shamir’s Secret Sharing Scheme. Instead of protecting a file with a single password you might forget, you split it into N pieces and define a threshold of how many pieces are needed to reconstruct the original. For example, split a file into 5 horcruxes where any 3 can reconstruct it.

How It Works
Horcrux generates a random encryption key using Go’s crypto/rand, encrypts the file with that key, then uses Hashicorp Vault’s Shamir implementation to split the key into N shares with a configurable threshold. Each horcrux file contains one key share plus the encrypted data. To reconstruct, you only need the threshold number of horcruxes in the same directory and run horcrux bind.

Commands
The tool has two primary commands. horcrux split diary.txt prompts for the total number of horcruxes and the threshold needed for reconstruction, then creates numbered files like diary_1_of_5.horcrux. horcrux bind scans the current directory for horcrux files and reconstructs the original if enough shares are present.

Use Cases
Horcrux is ideal for encrypting sensitive files like diaries, private keys, or credentials where you want distributed trust — no single location compromise reveals the data. It works well for transmitting files across multiple channels to reduce interception risk. Security teams can use it to split backup encryption keys across team members or physical locations.

Installation
Install via Homebrew: brew install jesseduffield/horcrux/horcrux. Via Scoop on Windows: scoop bucket add extras; scoop install horcrux. Binary releases are available on GitHub for Linux, macOS, and Windows. The tool is written in Go and ships as a single binary with no dependencies.

Agent Integration
Agents managing secrets, backup keys, or sensitive documents can use horcrux to implement distributed trust patterns. An agent can split a critical credential into shares distributed across different storage backends, ensuring no single compromise exposes the secret. The CLI interface is straightforward for automated workflows.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/horcrux-shamir-secret-file-splitter/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/horcrux-shamir-secret-file-splitter
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/horcrux-shamir-secret-file-splitter`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/horcrux-shamir-secret-file-splitter/)
