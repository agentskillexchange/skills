---
name: "WASM Component Model Linker"
description: "Compiles and links WebAssembly components using the WASI Preview 2 Component Model, wasm-tools CLI for component composition, and wit-bindgen for generating host/guest bindings from WIT interface definitions."
category: "Developer Tools"
framework: "Gemini"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/wasm-component-model-linker/"
---

# WASM Component Model Linker

Compiles and links WebAssembly components using the WASI Preview 2 Component Model, wasm-tools CLI for component composition, and wit-bindgen for generating host/guest bindings from WIT interface definitions.

## Overview

The WASM Component Model Linker automates the WebAssembly Component Model workflow from WIT (WebAssembly Interface Type) definitions through compilation and linking. It uses wit-bindgen to generate language-specific bindings for Rust (wit-bindgen-rust), JavaScript (jco), and Go (wit-bindgen-go) from .wit files. The agent orchestrates wasm-tools component new for creating components from core modules, wasm-tools compose for linking multiple components together, and wasm-tools validate for checking component conformance. It supports WASI Preview 2 interfaces including wasi:io, wasi:filesystem, wasi:http, and wasi:cli. For JavaScript hosts, it generates bindings using jco transpile and jco componentize. The pipeline integrates with Wasmtime for local testing and Fermyon Spin or Fastly Compute for edge deployment. Handles the full lifecycle from WIT authoring through component registry publishing using warg CLI for the WebAssembly component registry.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill wasm-component-model-linker
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill wasm-component-model-linker -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill wasm-component-model-linker -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill wasm-component-model-linker -a codex
```

### OpenClaw

```bash
clawhub install wasm-component-model-linker
```

## Source

- Marketplace: https://agentskillexchange.com/skills/wasm-component-model-linker/
