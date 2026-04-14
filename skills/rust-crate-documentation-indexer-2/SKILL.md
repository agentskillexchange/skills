---
title: "Rust Crate Documentation Indexer"
description: "Indexes Rust crate documentation from docs.rs using rustdoc JSON output and cargo-doc. Extracts trait implementations, generic bounds, and lifetime annotations for searchable API reference."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/rust-crate-documentation-indexer-2/"
category:
  - "Library &amp; API Reference"
framework:
  - "Gemini"
---

# Rust Crate Documentation Indexer

The Rust Crate Documentation Indexer skill creates searchable API reference indices from Rust crate documentation. It processes rustdoc JSON output format (–output-format json) for structured documentation extraction, uses cargo-doc for local documentation generation, and queries the docs.rs API for published crate documentation retrieval.

The skill extracts comprehensive API surface information including trait definitions with associated types and default implementations, generic type parameter bounds with where clause constraints, and lifetime annotation documentation with elision rule explanations. It maps trait implementation chains using impl Trait for Type syntax and auto-trait derivations (Send, Sync, Unpin) for thread safety documentation.

Advanced features include feature flag documentation extraction from Cargo.toml with conditional compilation analysis for #[cfg(feature = “…”)] gated APIs, example code extraction and validation using cargo-test for doc-test verification, and cross-crate dependency documentation linking via the crates.io API. The skill generates searchable indices with fuzzy matching support via the nucleo crate, produces compatibility matrices for MSRV (Minimum Supported Rust Version) tracking, and identifies unsafe code blocks with safety invariant documentation requirements.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crate-documentation-indexer-2/)
