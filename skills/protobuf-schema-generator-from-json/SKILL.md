---
title: "Protocol Buffer Schema Generator"
description: "Infers Protocol Buffer (.proto) definitions from JSON samples using protobuf-compiler and grpcio-tools. Generates proto3 schemas with nested message types, enums, and gRPC service stubs."
verification: "security_reviewed"
source: "https://github.com/protocolbuffers/protobuf"
category:
  - "Data Extraction & Transformation"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "protocolbuffers/protobuf"
  github_stars: 71179
---

# Protocol Buffer Schema Generator

The Protocol Buffer Schema Generator skill automatically infers .proto schema definitions from JSON sample data, eliminating the manual work of writing Protocol Buffer schemas for existing JSON APIs. It analyzes one or more JSON documents to determine field types, detect repeated fields (arrays), identify nested message structures, and recognize enum candidates (fields with a small set of string values). The inference engine uses statistical analysis across multiple samples to distinguish between optional and required fields, detect union types that need oneof declarations, and choose optimal numeric types (int32 vs int64, float vs double). Generated schemas follow proto3 syntax with proper package namespacing, import statements for well-known types (Timestamp, Duration, Any), and comprehensive field comments documenting observed value ranges and patterns. When gRPC service generation is enabled, the tool creates service definitions with standard CRUD RPCs based on detected resource patterns. The generated .proto files are validated using protoc compiler, and optional code generation produces Python, Go, or TypeScript stubs via grpcio-tools. Supports JSON Schema to Proto conversion as an alternative input format.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/protobuf-schema-generator-from-json/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/protobuf-schema-generator-from-json
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/protobuf-schema-generator-from-json`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-schema-generator-from-json/)
