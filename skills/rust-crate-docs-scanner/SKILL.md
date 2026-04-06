---
name: "Rust Crate Docs Scanner"
description: "Scans Rust crate documentation using rustdoc JSON output and cargo-doc metadata. Indexes public API surfaces including traits, impls, and derive macros with cross-crate dependency linking via docs.rs integration."
category: "Library & API Reference"
framework: "Custom Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/rust-crate-docs-scanner/"
---
# Rust Crate Docs Scanner

Scans Rust crate documentation using rustdoc JSON output and cargo-doc metadata. Indexes public API surfaces including traits, impls, and derive macros with cross-crate dependency linking via docs.rs integration.

The Rust Crate Docs Scanner skill processes Rust crate documentation by leveraging rustdoc JSON output format (unstable) and cargo doc --document-private-items for comprehensive API indexing. It parses the structured JSON to extract all public items, trait implementations, and type relationships.



This skill resolves the complete public API surface of a crate, including re-exports from dependencies, blanket trait implementations, and auto-derived trait impls. It uses cargo metadata to build the dependency graph and links cross-crate references to their docs.rs pages.



For procedural macros and derive macros, the skill analyzes the macro expansion patterns and documents the generated code structures. It handles attribute macros, function-like macros, and custom derive implementations with their helper attributes.



Output formats include structured JSON indexes for agent queries, markdown reference pages with syntax-highlighted code blocks, and compatibility matrices showing minimum supported Rust versions (MSRV) per API item. The skill also generates feature flag documentation showing which APIs are gated behind optional Cargo features.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill rust-crate-docs-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill rust-crate-docs-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill rust-crate-docs-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill rust-crate-docs-scanner -a codex
```

### OpenClaw

```bash
clawhub install rust-crate-docs-scanner
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crate-docs-scanner/)
