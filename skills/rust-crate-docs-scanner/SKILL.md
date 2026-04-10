---
title: "Rust Crate Docs Scanner"
description: "Scans Rust crate documentation using rustdoc JSON output and cargo-doc metadata. Indexes public API surfaces including traits, impls, and derive macros with cross-crate dependency linking via docs.rs integration."
slug: "rust-crate-docs-scanner"
category:
  - "Library &amp; API Reference"
framework:
  - "Custom Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/rust-crate-docs-scanner/"
---

# Rust Crate Docs Scanner

Scans Rust crate documentation using rustdoc JSON output and cargo-doc metadata. Indexes public API surfaces including traits, impls, and derive macros with cross-crate dependency linking via docs.rs integration.

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
clawhub install rust-crate-docs-scanner
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Rust Crate Docs Scanner skill processes Rust crate documentation by leveraging rustdoc JSON output format (unstable) and cargo doc --document-private-items for comprehensive API indexing. It parses the structured JSON to extract all public items, trait implementations, and type relationships.
This skill resolves the complete public API surface of a crate, including re-exports from dependencies, blanket trait implementations, and auto-derived trait impls. It uses cargo metadata to build the dependency graph and links cross-crate references to their docs.rs pages.
For procedural macros and derive macros, the skill analyzes the macro expansion patterns and documents the generated code structures. It handles attribute macros, function-like macros, and custom derive implementations with their helper attributes.
Output formats include structured JSON indexes for agent queries, markdown reference pages with syntax-highlighted code blocks, and compatibility matrices showing minimum supported Rust versions (MSRV) per API item. The skill also generates feature flag documentation showing which APIs are gated behind optional Cargo features.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rust-crate-docs-scanner/)
