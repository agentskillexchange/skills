---
title: "SWC Speedy Web Compiler for JavaScript and TypeScript"
description: "SWC (Speedy Web Compiler) is a Rust-based JavaScript and TypeScript compiler that is 20x faster than Babel on a single thread and 70x faster on four cores. It handles transpilation, minification, and bundling, and powers major tools including Next.js, Parcel, and Rspack."
verification: security_reviewed
source: "https://github.com/swc-project/swc"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "swc-project/swc"
  github_stars: 33347
---

# SWC Speedy Web Compiler for JavaScript and TypeScript

Overview
SWC is a super-fast TypeScript and JavaScript compiler written in Rust. It serves as both a Rust library and a JavaScript/Node.js package, providing compilation, minification, and bundling capabilities. SWC is used as the default compiler in Next.js, Parcel v2, and Rspack, and is the foundation for Deno’s TypeScript compilation. It achieves 20x the speed of Babel on a single thread and 70x on four cores.

Key Features

Compilation: Transpiles modern JavaScript and TypeScript (including JSX/TSX) to browser-compatible output, supporting ES2015 through the latest ECMAScript proposals
Minification: Replaces Terser for JavaScript minification with significantly faster execution while producing comparable output sizes
Bundling: Experimental bundler (spack) for producing optimized bundles with tree shaking and code splitting
Plugin System: WebAssembly-based plugin system allows custom transforms written in Rust, compiled to WASM, and loaded at runtime
Babel Compatibility: Direct migration path from Babel with support for common Babel plugins and presets via the @swc/core npm package
Source Maps: Full source map support for debugging transpiled code

Integration for AI Agents
Agents working on JavaScript/TypeScript codebases can use SWC for fast compilation during development workflows. The @swc/cli package provides command-line access for transpiling files and directories. The @swc/core package offers a programmatic API for Node.js. SWC’s speed makes it ideal for agents that need to repeatedly compile and test code changes, reducing wait times from seconds to milliseconds on large codebases.

Installation
npm install --save-dev @swc/core @swc/cli
npx swc src -d dist
Documentation: https://swc.rs/docs/installation

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swc-speedy-web-compiler-javascript-typescript/)
