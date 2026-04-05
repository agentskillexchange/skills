---
name: "Tera Jinja2-Inspired Template Engine for Rust"
description: "Tera is a powerful template engine for Rust inspired by Jinja2 and Django templates. It provides template inheritance, macros, filters, and auto-escaping, making it the go-to choice for HTML generation, static site builders, and code generation in Rust projects."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/Keats/tera"
---
# Tera Jinja2-Inspired Template Engine for Rust

Tera is a powerful template engine for Rust inspired by Jinja2 and Django templates. It provides template inheritance, macros, filters, and auto-escaping, making it the go-to choice for HTML generation, static site builders, and code generation in Rust projects.

Tera is an open-source template engine for Rust that brings the familiar syntax of Jinja2 and Django templates to the Rust ecosystem. With over 4,100 GitHub stars and active development, it is the most widely used template engine in Rust web frameworks and static site generators including Zola (by the same author).

How It Works Tera compiles templates at startup into an internal representation, then renders them with context data provided as key-value pairs. Templates use double-curly-brace syntax for expressions ({{ variable }}), curly-percent for control flow ({% if condition %}), and support template inheritance through extends/block patterns. The engine handles auto-escaping for HTML output by default.

Key Features

Jinja2-compatible syntax: Uses familiar {{ }}, {% %}, and {# #} delimiters that developers already know from Python templating. Template inheritance: Full support for extends, block, and include patterns for composable template hierarchies. Macros: Define reusable template components with parameters, similar to function calls in templates. Rich filter library: Built-in filters for string manipulation, number formatting, date handling, JSON serialization, and more. Custom filters and functions: Register your own Rust functions as template filters or global functions. Auto-escaping: Automatic HTML escaping prevents XSS vulnerabilities by default, with safe marking for trusted content. Error reporting: Clear error messages with template name and line numbers for debugging. Testers: Boolean test functions (is defined, is odd, etc.) for conditional logic.

Installation # Add to Cargo.toml [dependencies] tera = "2" Usage Example use tera::{Tera, Context}; let tera = Tera::new("templates/**/*").unwrap(); let mut context = Context::new(); context.insert("title", "My Page"); let rendered = tera.render("index.html", &context).unwrap(); Integration with AI Agents Tera is valuable in agent workflows that need to generate structured output — HTML reports, configuration files, email templates, or code scaffolding. Agents building Rust-based tools or working with static site generators like Zola interact with Tera templates directly. The Jinja2-compatible syntax means agents trained on Python templating patterns can work with Tera templates with minimal adaptation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill tera-rust-template-engine
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill tera-rust-template-engine -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill tera-rust-template-engine -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill tera-rust-template-engine -a codex
```

### OpenClaw

```bash
clawhub install tera-rust-template-engine
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/tera-rust-template-engine/)
