---
title: "Rust Crate Documentation Indexer"
description: "The Rust Crate Documentation Indexer skill creates searchable API reference indices from Rust crate documentation. It processes rustdoc JSON output format (&#8211;output-format json) for structured documentation extraction, uses cargo-doc for local documentation generation, and queries the docs.rs API for published crate documentation retrieval. The skill extracts comprehensive API surface information including trait definitions with associated types and default implementations, generic type parameter bounds with where clause constraints, and lifetime annotation documentation with elision rule explanations. It maps trait implementation chains using impl Trait for Type syntax and auto-trait derivations (Send, Sync, Unpin) for thread safety documentation. Advanced features include feature flag documentation extraction from Cargo.toml with conditional compilation analysis for #[cfg(feature = &#8220;&#8230;&#8221;)] gated APIs, example code extraction and validation using cargo-test for doc-test verification, and cross-crate dependency documentation linking via the crates.io API. The skill generates searchable indices with fuzzy matching support via the nucleo crate, produces compatibility matrices for MSRV (Minimum Supported Rust Version) tracking, and identifies unsafe code blocks with safety invariant documentation requirements."
source: "https://agentskillexchange.com/skills/rust-crate-documentation-indexer-2/"
verification: "security_reviewed"
category:
  - "Library &amp; API Reference"
framework:
  - "Gemini"
---

# Rust Crate Documentation Indexer

The Rust Crate Documentation Indexer skill creates searchable API reference indices from Rust crate documentation. It processes rustdoc JSON output format (&#8211;output-format json) for structured documentation extraction, uses cargo-doc for local documentation generation, and queries the docs.rs API for published crate documentation retrieval. The skill extracts comprehensive API surface information including trait definitions with associated types and default implementations, generic type parameter bounds with where clause constraints, and lifetime annotation documentation with elision rule explanations. It maps trait implementation chains using impl Trait for Type syntax and auto-trait derivations (Send, Sync, Unpin) for thread safety documentation. Advanced features include feature flag documentation extraction from Cargo.toml with conditional compilation analysis for #[cfg(feature = &#8220;&#8230;&#8221;)] gated APIs, example code extraction and validation using cargo-test for doc-test verification, and cross-crate dependency documentation linking via the crates.io API. The skill generates searchable indices with fuzzy matching support via the nucleo crate, produces compatibility matrices for MSRV (Minimum Supported Rust Version) tracking, and identifies unsafe code blocks with safety invariant documentation requirements.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crate-documentation-indexer-2/)
