---
title: "Rust Crates.io Explorer"
description: "Searches the crates.io REST API for Rust crate metadata, version diffs, and feature flag documentation. Integrates with docs.rs API for inline rustdoc retrieval and lib.rs category browsing."
slug: "rust-crates-io-explorer"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/rust-crates-io-explorer/"
---

# Rust Crates.io Explorer

Searches the crates.io REST API for Rust crate metadata, version diffs, and feature flag documentation. Integrates with docs.rs API for inline rustdoc retrieval and lib.rs category browsing.

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
clawhub install rust-crates-io-explorer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Rust Crates.io Explorer skill enables fast discovery and analysis of Rust crates through the crates.io REST API. It retrieves crate metadata including version histories, feature flags, dependency requirements, and owner information.
The skill integrates with the docs.rs API for direct rustdoc retrieval, allowing inline access to struct definitions, trait implementations, and function signatures without leaving the development environment. It supports lib.rs category browsing for discovering crates by use case.
Key features include feature flag analysis showing which dependencies each feature enables, MSRV (Minimum Supported Rust Version) checking, and yanked version detection. The skill compares crate alternatives by download statistics, recent release activity, and reverse dependency counts, helping developers make informed choices for their Cargo.toml dependencies.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crates-io-explorer/)
