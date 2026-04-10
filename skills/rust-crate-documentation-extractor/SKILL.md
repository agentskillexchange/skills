---
title: "Rust Crate Documentation Extractor"
description: "Extracts and indexes Rust crate documentation using cargo-doc, docs.rs API, and syn for AST parsing. Generates searchable API references with cross-crate linking and example extraction."
slug: "rust-crate-documentation-extractor"
category:
  - "Library &amp; API Reference"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/rust-crate-documentation-extractor/"
listed: true
---

# Rust Crate Documentation Extractor

Extracts and indexes Rust crate documentation using cargo-doc, docs.rs API, and syn for AST parsing. Generates searchable API references with cross-crate linking and example extraction.

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
clawhub install rust-crate-documentation-extractor
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Rust Crate Documentation Extractor builds comprehensive API reference indexes from Rust crate ecosystems by leveraging cargo-doc for HTML documentation generation and the docs.rs API for querying published crate documentation and metadata. It uses the syn crate for Rust AST parsing to extract function signatures, trait implementations, and module hierarchies programmatically. The skill generates structured JSON indexes of public API surfaces, enabling full-text search across multiple crates with proper cross-crate linking via rustdoc’s intra-doc link resolution. It extracts code examples from doc comments and validates them using cargo-test to ensure documentation accuracy. The extractor integrates with crates.io API for version history analysis, tracking API surface changes between releases using cargo-semver-checks for automated breaking change detection. It supports workspace-level documentation aggregation and generates dependency-aware API maps showing which traits are implemented by which types across the dependency graph.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crate-documentation-extractor/)
