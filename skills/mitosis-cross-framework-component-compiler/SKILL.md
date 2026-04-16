---
title: "Mitosis Cross-Framework Component Compiler by Builder.io"
description: "Mitosis lets you write UI components once and compile them to React, Vue, Angular, Svelte, Solid, Qwik, and more. Built by Builder.io, it enables maintaining a single component codebase across all major frontend frameworks."
verification: "security_reviewed"
source: "https://github.com/BuilderIO/mitosis"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "BuilderIO/mitosis"
  github_stars: 13808
---

# Mitosis Cross-Framework Component Compiler by Builder.io

Mitosis is a cross-framework component compiler developed by Builder.io that solves one of the most persistent problems in frontend development: writing and maintaining components across multiple JavaScript frameworks. With Mitosis, developers write components once using a JSX-based syntax and compile the output to native framework code for React, Vue, Angular, Svelte, Solid, Qwik, Alpine.js, Liquid (Shopify), and more.


How It Works
Mitosis uses its own component format (a subset of JSX) as a universal intermediate representation. The compiler parses this format and generates idiomatic code for each target framework. Unlike web components, the output is native framework code — no runtime wrapper, no shadow DOM overhead, no interoperability issues.


Key Features

Write once, compile everywhere: A single component definition compiles to React, Vue 2/3, Angular, Svelte, Solid, Qwik, Alpine.js, Lit, Stencil, React Native, and Swift.
Figma integration: Import designs from Figma and generate framework-specific components directly.
Design system consistency: Maintain a unified design system that compiles to every framework your organization uses.
CLI and API: Use npm create @builder.io/mitosis@latest to scaffold a new project, or use the compiler API programmatically.
Interactive playground: Test component compilation in real-time at mitosis.builder.io/playground.

Agent Integration
AI agents can use Mitosis to generate cross-framework component libraries from a single specification. An agent can write the Mitosis JSX format and produce output for any target framework, making it valuable for design system automation, multi-framework codebases, and Figma-to-code pipelines. The npm package @builder.io/mitosis provides the CLI and compiler API.


Installation
npm create @builder.io/mitosis@latest
Or add the compiler to an existing project:


npm install @builder.io/mitosis

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mitosis-cross-framework-component-compiler/)
