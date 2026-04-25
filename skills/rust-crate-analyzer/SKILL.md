---
title: "Rust Crate Analyzer"
description: "Fetches crate metadata from the crates.io API and docs.rs API for Rust package discovery. Analyzes feature flags, dependency auditing via RustSec Advisory DB, and MSRV compatibility checking."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/rust-crate-analyzer/"
category:
  - "Library & API Reference"
framework:
  - "Codex"
---

# Rust Crate Analyzer

The Rust Crate Analyzer skill provides comprehensive Rust ecosystem intelligence by querying the crates.io REST API for crate metadata and the docs.rs API for documentation status. It retrieves version histories, download statistics, feature flag definitions, and dependency specifications from Cargo.toml metadata. The skill resolves dependency trees from crate manifests, respecting Cargo feature unification rules and optional dependency activation. It checks each dependency against the RustSec Advisory Database via the rustsec crate advisory feed for known vulnerabilities, providing CVSS scores and patch version recommendations. MSRV (Minimum Supported Rust Version) compatibility analysis checks whether dependency requirements are satisfiable with a target Rust toolchain version. Advanced features include feature flag dependency graphing showing which features activate which optional dependencies, build time estimation based on dependency count and complexity heuristics, and crate comparison mode with side-by-side API surface analysis from docs.rs. The skill monitors crates.io for new releases of watched crates, validates Cargo.toml against common anti-patterns like wildcard dependencies, and provides migration guidance when switching between alternative crates. Integration with cargo-deny configuration generation automates license and advisory policy enforcement.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/rust-crate-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/rust-crate-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/rust-crate-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crate-analyzer/)
