---
name: "Protocol Buffer Schema Generator"
description: "Infers Protocol Buffer (.proto) definitions from JSON samples using protobuf-compiler and grpcio-tools. Generates proto3 schemas with nested message types, enums, and gRPC service stubs."
category: "Data Extraction & Transformation"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/protobuf-schema-generator-from-json/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "grpc"  # from ase_tool_match
  github_stars: 4816  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 30883690  # from ase_npm_downloads
  github_repo: "grpc/grpc-node"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Protocol Buffer Schema Generator

Infers Protocol Buffer (.proto) definitions from JSON samples using protobuf-compiler and grpcio-tools. Generates proto3 schemas with nested message types, enums, and gRPC service stubs.

## Overview

The Protocol Buffer Schema Generator skill automatically infers .proto schema definitions from JSON sample data, eliminating the manual work of writing Protocol Buffer schemas for existing JSON APIs. It analyzes one or more JSON documents to determine field types, detect repeated fields (arrays), identify nested message structures, and recognize enum candidates (fields with a small set of string values). The inference engine uses statistical analysis across multiple samples to distinguish between optional and required fields, detect union types that need oneof declarations, and choose optimal numeric types (int32 vs int64, float vs double). Generated schemas follow proto3 syntax with proper package namespacing, import statements for well-known types (Timestamp, Duration, Any), and comprehensive field comments documenting observed value ranges and patterns. When gRPC service generation is enabled, the tool creates service definitions with standard CRUD RPCs based on detected resource patterns. The generated .proto files are validated using protoc compiler, and optional code generation produces Python, Go, or TypeScript stubs via grpcio-tools. Supports JSON Schema to Proto conversion as an alternative input format.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill protobuf-schema-generator-from-json
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill protobuf-schema-generator-from-json -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill protobuf-schema-generator-from-json -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill protobuf-schema-generator-from-json -a codex
```

### OpenClaw

```bash
clawhub install protobuf-schema-generator-from-json
```

## Source

- Marketplace: https://agentskillexchange.com/skills/protobuf-schema-generator-from-json/
