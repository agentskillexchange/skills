---
name: "Rust Crates.io Explorer"
description: "Searches the crates.io REST API for Rust crate metadata, version diffs, and feature flag documentation. Integrates with docs.rs API for inline rustdoc retrieval and lib.rs category browsing."
category: "Library & API Reference"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/rust-crates-io-explorer/"
---
# Rust Crates.io Explorer

Searches the crates.io REST API for Rust crate metadata, version diffs, and feature flag documentation. Integrates with docs.rs API for inline rustdoc retrieval and lib.rs category browsing.

## Overview

The Rust Crates.io Explorer skill enables fast discovery and analysis of Rust crates through the crates.io REST API. It retrieves crate metadata including version histories, feature flags, dependency requirements, and owner information.

The skill integrates with the docs.rs API for direct rustdoc retrieval, allowing inline access to struct definitions, trait implementations, and function signatures without leaving the development environment. It supports lib.rs category browsing for discovering crates by use case.

Key features include feature flag analysis showing which dependencies each feature enables, MSRV (Minimum Supported Rust Version) checking, and yanked version detection. The skill compares crate alternatives by download statistics, recent release activity, and reverse dependency counts, helping developers make informed choices for their Cargo.toml dependencies.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill rust-crates-io-explorer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill rust-crates-io-explorer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill rust-crates-io-explorer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill rust-crates-io-explorer -a codex
```

### OpenClaw

```bash
clawhub install rust-crates-io-explorer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crates-io-explorer/)
