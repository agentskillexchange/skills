---
title: Rust Crate Documentation Extractor
description: The Rust Crate Documentation Extractor builds comprehensive API reference
  indexes from Rust crate ecosystems by leveraging cargo-doc for HTML documentation
  generation and the docs.rs API for querying published crate documentation and metadata.
  It uses the syn crate for Rust AST parsing to extract function signatures, trait
  implementations, and module hierarchies programmatically. The skill generates structured
  JSON indexes of public API surfaces, enabling full-text search across multiple crates
  with proper cross-crate linking via rustdoc’s intra-doc link resolution. It extracts
  code examples from doc comments and validates them using cargo-test to ensure documentation
  accuracy. The extractor integrates with crates.io API for version history analysis,
  tracking API surface changes between releases using cargo-semver-checks for automated
  breaking change detection. It supports workspace-level documentation aggregation
  and generates dependency-aware API maps showing which traits are implemented by
  which types across the dependency graph.
verification: security_reviewed
source: https://agentskillexchange.com/skills/rust-crate-documentation-extractor/
category:
- Library &amp; API Reference
framework:
- Custom Agents
---

# Rust Crate Documentation Extractor

The Rust Crate Documentation Extractor builds comprehensive API reference indexes from Rust crate ecosystems by leveraging cargo-doc for HTML documentation generation and the docs.rs API for querying published crate documentation and metadata. It uses the syn crate for Rust AST parsing to extract function signatures, trait implementations, and module hierarchies programmatically. The skill generates structured JSON indexes of public API surfaces, enabling full-text search across multiple crates with proper cross-crate linking via rustdoc’s intra-doc link resolution. It extracts code examples from doc comments and validates them using cargo-test to ensure documentation accuracy. The extractor integrates with crates.io API for version history analysis, tracking API surface changes between releases using cargo-semver-checks for automated breaking change detection. It supports workspace-level documentation aggregation and generates dependency-aware API maps showing which traits are implemented by which types across the dependency graph.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crate-documentation-extractor/)
