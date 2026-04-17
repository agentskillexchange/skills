---
title: "Rust Crate Docs Scanner"
description: "The Rust Crate Docs Scanner skill processes Rust crate documentation by leveraging rustdoc JSON output format (unstable) and cargo doc --document-private-items for comprehensive API indexing. It parses the structured JSON to extract all public items, trait implementations, and type relationships.\nThis skill resolves the complete public API surface of a crate, including re-exports from dependencies, blanket trait implementations, and auto-derived trait impls. It uses cargo metadata to build the dependency graph and links cross-crate references to their docs.rs pages.\nFor procedural macros and derive macros, the skill analyzes the macro expansion patterns and documents the generated code structures. It handles attribute macros, function-like macros, and custom derive implementations with their helper attributes.\nOutput formats include structured JSON indexes for agent queries, markdown reference pages with syntax-highlighted code blocks, and compatibility matrices showing minimum supported Rust versions (MSRV) per API item. The skill also generates feature flag documentation showing which APIs are gated behind optional Cargo features."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/rust-crate-docs-scanner/"
framework:
  - "Custom Agents"
---

# Rust Crate Docs Scanner

The Rust Crate Docs Scanner skill processes Rust crate documentation by leveraging rustdoc JSON output format (unstable) and cargo doc --document-private-items for comprehensive API indexing. It parses the structured JSON to extract all public items, trait implementations, and type relationships.
This skill resolves the complete public API surface of a crate, including re-exports from dependencies, blanket trait implementations, and auto-derived trait impls. It uses cargo metadata to build the dependency graph and links cross-crate references to their docs.rs pages.
For procedural macros and derive macros, the skill analyzes the macro expansion patterns and documents the generated code structures. It handles attribute macros, function-like macros, and custom derive implementations with their helper attributes.
Output formats include structured JSON indexes for agent queries, markdown reference pages with syntax-highlighted code blocks, and compatibility matrices showing minimum supported Rust versions (MSRV) per API item. The skill also generates feature flag documentation showing which APIs are gated behind optional Cargo features.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/rust-crate-docs-scanner
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/rust-crate-docs-scanner` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crate-docs-scanner/)
