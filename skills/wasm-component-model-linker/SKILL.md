---
name: "WASM Component Model Linker"
description: "Compiles and links WebAssembly components using the WASI Preview 2 Component Model, wasm-tools CLI for component composition, and wit-bindgen for generating host/guest bindings from WIT interface definitions."
verification: security_reviewed
source: "https://github.com/WebAssembly/component-model"
category:
  - "Developer Tools"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "WebAssembly/component-model"
  github_stars: 1294
---

# WASM Component Model Linker

The WASM Component Model Linker automates the WebAssembly Component Model workflow from WIT (WebAssembly Interface Type) definitions through compilation and linking. It uses wit-bindgen to generate language-specific bindings for Rust (wit-bindgen-rust), JavaScript (jco), and Go (wit-bindgen-go) from .wit files. The agent orchestrates wasm-tools component new for creating components from core modules, wasm-tools compose for linking multiple components together, and wasm-tools validate for checking component conformance. It supports WASI Preview 2 interfaces including wasi:io, wasi:filesystem, wasi:http, and wasi:cli. For JavaScript hosts, it generates bindings using jco transpile and jco componentize. The pipeline integrates with Wasmtime for local testing and Fermyon Spin or Fastly Compute for edge deployment. Handles the full lifecycle from WIT authoring through component registry publishing using warg CLI for the WebAssembly component registry.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wasm-component-model-linker/)
