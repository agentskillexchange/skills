---
name: "Rust Crate Documentation Extractor"
description: "Extracts and indexes Rust crate documentation using cargo-doc, docs.rs API, and syn for AST parsing. Generates searchable API references with cross-crate linking and example extraction."
category: "Library & API Reference"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/rust-crate-documentation-extractor/"
---

# Rust Crate Documentation Extractor

Extracts and indexes Rust crate documentation using cargo-doc, docs.rs API, and syn for AST parsing. Generates searchable API references with cross-crate linking and example extraction.

## Overview

The Rust Crate Documentation Extractor builds comprehensive API reference indexes from Rust crate ecosystems by leveraging cargo-doc for HTML documentation generation and the docs.rs API for querying published crate documentation and metadata. It uses the syn crate for Rust AST parsing to extract function signatures, trait implementations, and module hierarchies programmatically. The skill generates structured JSON indexes of public API surfaces, enabling full-text search across multiple crates with proper cross-crate linking via rustdoc’s intra-doc link resolution. It extracts code examples from doc comments and validates them using cargo-test to ensure documentation accuracy. The extractor integrates with crates.io API for version history analysis, tracking API surface changes between releases using cargo-semver-checks for automated breaking change detection. It supports workspace-level documentation aggregation and generates dependency-aware API maps showing which traits are implemented by which types across the dependency graph.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill rust-crate-documentation-extractor
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill rust-crate-documentation-extractor -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill rust-crate-documentation-extractor -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill rust-crate-documentation-extractor -a codex
```

### OpenClaw

```bash
clawhub install rust-crate-documentation-extractor
```

## Source

- Marketplace: https://agentskillexchange.com/skills/rust-crate-documentation-extractor/
