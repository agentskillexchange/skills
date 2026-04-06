---
name: "Dasel Multi-Format Data Selector and Modifier"
description: "Dasel (Data-Select) is a command-line tool and Go library for querying, modifying, and transforming structured data across JSON, YAML, TOML, XML, CSV, HCL, and INI formats using a unified selector syntax. It supports format conversion between all supported types."
category: "Data Extraction &amp; Transformation"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/TomWright/dasel"
tool_ecosystem:
  github_repo: "https://github.com/tomwright/dasel"
  github_stars: 7892
---
# Dasel Multi-Format Data Selector and Modifier

Dasel (Data-Select) is a command-line tool and Go library for querying, modifying, and transforming structured data across JSON, YAML, TOML, XML, CSV, HCL, and INI formats using a unified selector syntax. It supports format conversion between all supported types.

Dasel (short for Data-Select) is a command-line tool created by Tom Wright that provides a single, consistent syntax for querying and modifying data across multiple structured formats: JSON, YAML, TOML, XML, CSV, HCL, and INI. Unlike using separate tools for each format (jq for JSON, yq for YAML, xmlstarlet for XML), Dasel uses one unified selector syntax that works identically regardless of the input format.

The tool supports three core operations: select (extract values from data), put (insert or update values), and delete (remove values). Its selector syntax supports array indexing, key access, dynamic filtering, searching, and type coercion. For example, the same selector expression works whether your data is in a YAML config file, a JSON API response, or an XML document.

One of Dasel is most powerful features is format conversion. You can read data from one format and output it in another with zero configuration. For instance, reading a TOML configuration file and outputting it as JSON, or converting an XML document to YAML. This makes it invaluable for DevOps tasks where configuration files exist in different formats across different tools.

Dasel is written in Go with zero runtime dependencies, making it easy to install and deploy. It ships as a single static binary for Linux, macOS, and Windows, and is available via Homebrew (brew install dasel), Go install, and prebuilt binaries on GitHub Releases. Version 3 was released in December 2025 with significant performance improvements and an enhanced query language.

The tool integrates naturally into shell pipelines, reading from stdin and writing to stdout. It can also modify files in-place, making it useful for scripted configuration management. Dasel is also available as a Go library for use in Go projects. Licensed under MIT, it has strong community adoption with thousands of GitHub stars and active maintenance.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill dasel-multi-format-data-selector-modifier
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill dasel-multi-format-data-selector-modifier -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill dasel-multi-format-data-selector-modifier -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill dasel-multi-format-data-selector-modifier -a codex
```

### OpenClaw

```bash
clawhub install dasel-multi-format-data-selector-modifier
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/dasel-multi-format-data-selector-modifier/)
