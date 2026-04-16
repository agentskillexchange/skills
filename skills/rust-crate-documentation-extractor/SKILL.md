---
title: "Rust Crate Documentation Extractor"
description: "Extracts and indexes Rust crate documentation using cargo-doc, docs.rs API, and syn for AST parsing. Generates searchable API references with cross-crate linking and example extraction."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/rust-crate-documentation-extractor/"
category:
  - "Library & API Reference"
framework:
  - "Custom Agents"
---

# Rust Crate Documentation Extractor

The Rust Crate Documentation Extractor builds comprehensive API reference indexes from Rust crate ecosystems by leveraging cargo-doc for HTML documentation generation and the docs.rs API for querying published crate documentation and metadata. It uses the syn crate for Rust AST parsing to extract function signatures, trait implementations, and module hierarchies programmatically. The skill generates structured JSON indexes of public API surfaces, enabling full-text search across multiple crates with proper cross-crate linking via rustdoc’s intra-doc link resolution. It extracts code examples from doc comments and validates them using cargo-test to ensure documentation accuracy. The extractor integrates with crates.io API for version history analysis, tracking API surface changes between releases using cargo-semver-checks for automated breaking change detection. It supports workspace-level documentation aggregation and generates dependency-aware API maps showing which traits are implemented by which types across the dependency graph.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crate-documentation-extractor/)
