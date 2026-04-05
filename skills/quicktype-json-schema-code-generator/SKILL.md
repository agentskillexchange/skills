---
name: "quicktype JSON Schema to Typed Code Generator"
description: "Generate strongly-typed models and serializers from JSON, JSON Schema, TypeScript, and GraphQL queries in 20+ programming languages. quicktype turns sample data into production-ready type definitions for Swift, C#, Go, Python, Rust, Java, Kotlin, and more."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://github.com/glideapps/quicktype"
tool_ecosystem:
  github_repo: "glideapps/quicktype"
  github_stars: 13690
---
# quicktype JSON Schema to Typed Code Generator

Generate strongly-typed models and serializers from JSON, JSON Schema, TypeScript, and GraphQL queries in 20+ programming languages. quicktype turns sample data into production-ready type definitions for Swift, C#, Go, Python, Rust, Java, Kotlin, and more.

quicktype is an open-source tool by Glide that generates strongly-typed data models and serialization code from JSON samples, JSON Schema definitions, TypeScript interfaces, and GraphQL queries. It supports over 20 target languages including Swift, C#, Go, Python, Rust, Java, Kotlin, Dart, TypeScript, C++, Ruby, Scala, Haskell, PHP, Elm, and Objective-C.



The tool works by inferring a JSON Schema from input data and then generating language-specific type definitions with proper serialization and deserialization logic. This means different parts of a stack can share the same data contract: a Swift iOS client, a Java Android app, and a Node.js backend can all generate models from the same schema, ensuring they serialize to and deserialize from identical JSON structures.



The recommended workflow starts by inferring a schema from sample JSON, reviewing and editing the schema to add constraints or clarify types, committing the schema to the project repository, and then generating code from it as part of the build process. This schema-first approach prevents drift between implementations and catches type mismatches at build time rather than runtime.



quicktype accepts input from multiple sources including local JSON files, URLs pointing to live APIs, JSON Schema files, TypeScript source files, and GraphQL query documents. The CLI is installed globally via npm and supports options for controlling the output language, top-level type name, source language, and output file path. A web application at app.quicktype.io provides the same functionality with a visual interface and works offline without sending data over the network.



For teams working with microservices, mobile clients, or polyglot codebases, quicktype eliminates the manual effort of writing and maintaining type definitions across languages. It handles edge cases like optional fields, nullable types, union types, and nested objects, generating idiomatic code that follows each language’s conventions for data modeling.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill quicktype-json-schema-code-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill quicktype-json-schema-code-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill quicktype-json-schema-code-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill quicktype-json-schema-code-generator -a codex
```

### OpenClaw

```bash
clawhub install quicktype-json-schema-code-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/quicktype-json-schema-code-generator/)
