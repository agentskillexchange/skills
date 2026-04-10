---
title: "Protocol Buffer Schema Generator"
description: "Infers Protocol Buffer (.proto) definitions from JSON samples using protobuf-compiler and grpcio-tools. Generates proto3 schemas with nested message types, enums, and gRPC service stubs."
slug: "protobuf-schema-generator-from-json"
category:
  - "Data Extraction &amp; Transformation"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/protobuf-schema-generator-from-json/"
listed: true
---

# Protocol Buffer Schema Generator

Infers Protocol Buffer (.proto) definitions from JSON samples using protobuf-compiler and grpcio-tools. Generates proto3 schemas with nested message types, enums, and gRPC service stubs.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install protobuf-schema-generator-from-json
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Protocol Buffer Schema Generator skill automatically infers .proto schema definitions from JSON sample data, eliminating the manual work of writing Protocol Buffer schemas for existing JSON APIs. It analyzes one or more JSON documents to determine field types, detect repeated fields (arrays), identify nested message structures, and recognize enum candidates (fields with a small set of string values). The inference engine uses statistical analysis across multiple samples to distinguish between optional and required fields, detect union types that need oneof declarations, and choose optimal numeric types (int32 vs int64, float vs double). Generated schemas follow proto3 syntax with proper package namespacing, import statements for well-known types (Timestamp, Duration, Any), and comprehensive field comments documenting observed value ranges and patterns. When gRPC service generation is enabled, the tool creates service definitions with standard CRUD RPCs based on detected resource patterns. The generated .proto files are validated using protoc compiler, and optional code generation produces Python, Go, or TypeScript stubs via grpcio-tools. Supports JSON Schema to Proto conversion as an alternative input format.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-schema-generator-from-json/)
