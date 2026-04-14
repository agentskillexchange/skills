---
title: "Rust Crate Documentation Extractor"
description: "Extracts and indexes Rust crate documentation using cargo-doc, docs.rs API, and syn for AST parsing. Generates searchable API references with cross-crate linking and example extraction."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/rust-crate-documentation-extractor/"
category:
  - "Library &amp; API Reference"
framework:
  - "Custom Agents"
---

# Rust Crate Documentation Extractor

The Rust Crate Documentation Extractor builds comprehensive API reference indexes from Rust crate ecosystems by leveraging cargo-doc for HTML documentation generation and the docs.rs API for querying published crate documentation and metadata. It uses the syn crate for Rust AST parsing to extract function signatures, trait implementations, and module hierarchies programmatically. The skill generates structured JSON indexes of public API surfaces, enabling full-text search across multiple crates with proper cross-crate linking via rustdoc’s intra-doc link resolution. It extracts code examples from doc comments and validates them using cargo-test to ensure documentation accuracy. The extractor integrates with crates.io API for version history analysis, tracking API surface changes between releases using cargo-semver-checks for automated breaking change detection. It supports workspace-level documentation aggregation and generates dependency-aware API maps showing which traits are implemented by which types across the dependency graph.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crate-documentation-extractor/)
