---
title: Rust Crate Docs Scanner
description: The Rust Crate Docs Scanner skill processes Rust crate documentation
  by leveraging rustdoc JSON output format (unstable) and cargo doc --document-private-items
  for comprehensive API indexing. It parses the structured JSON to extract all public
  items, trait implementations, and type relationships. This skill resolves the complete
  public API surface of a crate, including re-exports from dependencies, blanket trait
  implementations, and auto-derived trait impls. It uses cargo metadata to build the
  dependency graph and links cross-crate references to their docs.rs pages. For procedural
  macros and derive macros, the skill analyzes the macro expansion patterns and documents
  the generated code structures. It handles attribute macros, function-like macros,
  and custom derive implementations with their helper attributes. Output formats include
  structured JSON indexes for agent queries, markdown reference pages with syntax-highlighted
  code blocks, and compatibility matrices showing minimum supported Rust versions
  (MSRV) per API item. The skill also generates feature flag documentation showing
  which APIs are gated behind optional Cargo features.
verification: security_reviewed
source: https://agentskillexchange.com/skills/rust-crate-docs-scanner/
category:
- Library &amp; API Reference
framework:
- Custom Agents
---

# Rust Crate Docs Scanner

The Rust Crate Docs Scanner skill processes Rust crate documentation by leveraging rustdoc JSON output format (unstable) and cargo doc --document-private-items for comprehensive API indexing. It parses the structured JSON to extract all public items, trait implementations, and type relationships. This skill resolves the complete public API surface of a crate, including re-exports from dependencies, blanket trait implementations, and auto-derived trait impls. It uses cargo metadata to build the dependency graph and links cross-crate references to their docs.rs pages. For procedural macros and derive macros, the skill analyzes the macro expansion patterns and documents the generated code structures. It handles attribute macros, function-like macros, and custom derive implementations with their helper attributes. Output formats include structured JSON indexes for agent queries, markdown reference pages with syntax-highlighted code blocks, and compatibility matrices showing minimum supported Rust versions (MSRV) per API item. The skill also generates feature flag documentation showing which APIs are gated behind optional Cargo features.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crate-docs-scanner/)
