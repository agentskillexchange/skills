---
title: "Rust Crate Analyzer"
description: "The Rust Crate Analyzer skill provides comprehensive Rust ecosystem intelligence by querying the crates.io REST API for crate metadata and the docs.rs API for documentation status. It retrieves version histories, download statistics, feature flag definitions, and dependency specifications from Cargo.toml metadata.\nThe skill resolves dependency trees from crate manifests, respecting Cargo feature unification rules and optional dependency activation. It checks each dependency against the RustSec Advisory Database via the rustsec crate advisory feed for known vulnerabilities, providing CVSS scores and patch version recommendations. MSRV (Minimum Supported Rust Version) compatibility analysis checks whether dependency requirements are satisfiable with a target Rust toolchain version.\nAdvanced features include feature flag dependency graphing showing which features activate which optional dependencies, build time estimation based on dependency count and complexity heuristics, and crate comparison mode with side-by-side API surface analysis from docs.rs. The skill monitors crates.io for new releases of watched crates, validates Cargo.toml against common anti-patterns like wildcard dependencies, and provides migration guidance when switching between alternative crates. Integration with cargo-deny configuration generation automates license and advisory policy enforcement."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/rust-crate-analyzer/"
framework:
  - "Codex"
---

# Rust Crate Analyzer

The Rust Crate Analyzer skill provides comprehensive Rust ecosystem intelligence by querying the crates.io REST API for crate metadata and the docs.rs API for documentation status. It retrieves version histories, download statistics, feature flag definitions, and dependency specifications from Cargo.toml metadata.
The skill resolves dependency trees from crate manifests, respecting Cargo feature unification rules and optional dependency activation. It checks each dependency against the RustSec Advisory Database via the rustsec crate advisory feed for known vulnerabilities, providing CVSS scores and patch version recommendations. MSRV (Minimum Supported Rust Version) compatibility analysis checks whether dependency requirements are satisfiable with a target Rust toolchain version.
Advanced features include feature flag dependency graphing showing which features activate which optional dependencies, build time estimation based on dependency count and complexity heuristics, and crate comparison mode with side-by-side API surface analysis from docs.rs. The skill monitors crates.io for new releases of watched crates, validates Cargo.toml against common anti-patterns like wildcard dependencies, and provides migration guidance when switching between alternative crates. Integration with cargo-deny configuration generation automates license and advisory policy enforcement.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/rust-crate-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/rust-crate-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crate-analyzer/)
