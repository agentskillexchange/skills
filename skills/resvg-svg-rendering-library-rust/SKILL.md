---
name: "resvg High-Performance SVG Rendering Library in Rust"
description: "resvg is a fast, portable SVG rendering library written in Rust that converts SVG files to PNG images with high correctness. It works as a Rust library, C library, CLI tool, and has Node.js bindings via resvg-js for server-side SVG-to-image conversion."
category: "Image & Creative Automation"
framework: "Multi-Framework"
verification: listed
source: "https://github.com/linebender/resvg"
---
# resvg High-Performance SVG Rendering Library in Rust

resvg is a fast, portable SVG rendering library written in Rust that converts SVG files to PNG images with high correctness. It works as a Rust library, C library, CLI tool, and has Node.js bindings via resvg-js for server-side SVG-to-image conversion.

## Overview

resvg is an SVG rendering library written entirely in Rust that focuses on correctness, safety, and portability. Maintained under the Linebender project, it uses the tiny-skia rendering engine and aims to support the full static SVG 1.1 specification. The library ships as a Rust crate, a C library with a stable ABI, a standalone CLI application, and has community-maintained Node.js bindings through resvg-js powered by napi-rs and WebAssembly.

Rendering Architecture

resvg splits SVG processing into two phases: parsing and rendering. The parsing phase is handled by usvg, which normalizes SVG input by resolving attributes, converting shapes to paths, removing invisible elements, and fixing malformed markup. The result is a simplified render tree that any 2D graphics library can consume. The rendering phase uses tiny-skia, a pure-Rust 2D rendering library, to produce pixel-perfect output. This separation means developers can use usvg alone as a preprocessing step and plug in their own renderer.

Correctness and Testing

The library maintains a test suite of approximately 1,600 SVG-to-PNG regression tests, covering edge cases in gradients, filters, text layout, clipping, masking, and pattern fills. This test suite is publicly available and not tied to resvg, making it useful for anyone building SVG processing tools. resvg produces reproducible output across all platforms — rendering the same SVG on x86 Windows and ARM macOS yields identical pixel values.

Node.js Integration via resvg-js

The resvg-js package on npm provides high-performance SVG rendering for Node.js applications using napi-rs native bindings or a pure WebAssembly backend. Developers use it for server-side SVG-to-PNG conversion in image generation pipelines, OG image generators (commonly paired with Satori for HTML-to-SVG), and PDF rendering workflows. Install with npm install @resvg/resvg-js and call renderAsync() or new Resvg(svgString).render().asPng().

CLI Usage

The resvg CLI converts SVG files to PNG from the command line. It supports custom DPI, background color, width/height constraints, and font directory configuration. The standalone binary is under 3MB with zero external dependencies, making it suitable for CI/CD pipelines, Docker containers, and server environments where installing a full browser for SVG rendering is impractical.

Safety and Performance

Written in safe Rust with minimal unsafe code, resvg provides memory safety guarantees and protection against common vulnerabilities when processing untrusted SVG input. It includes guards against infinite loops and stack overflows from recursive SVG structures. Performance is competitive with native browser SVG rendering for static content, with room for further optimization.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill resvg-svg-rendering-library-rust
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill resvg-svg-rendering-library-rust -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill resvg-svg-rendering-library-rust -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill resvg-svg-rendering-library-rust -a codex
```

### OpenClaw

```bash
clawhub install resvg-svg-rendering-library-rust
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/resvg-svg-rendering-library-rust/)
