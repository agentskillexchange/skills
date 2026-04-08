---
title: Protocol Buffer Schema Generator
description: The Protocol Buffer Schema Generator skill automatically infers .proto
  schema definitions from JSON sample data, eliminating the manual work of writing
  Protocol Buffer schemas for existing JSON APIs. It analyzes one or more JSON documents
  to determine field types, detect repeated fields (arrays), identify nested message
  structures, and recognize enum candidates (fields with a small set of string values).
  The inference engine uses statistical analysis across multiple samples to distinguish
  between optional and required fields, detect union types that need oneof declarations,
  and choose optimal numeric types (int32 vs int64, float vs double). Generated schemas
  follow proto3 syntax with proper package namespacing, import statements for well-known
  types (Timestamp, Duration, Any), and comprehensive field comments documenting observed
  value ranges and patterns. When gRPC service generation is enabled, the tool creates
  service definitions with standard CRUD RPCs based on detected resource patterns.
  The generated .proto files are validated using protoc compiler, and optional code
  generation produces Python, Go, or TypeScript stubs via grpcio-tools. Supports JSON
  Schema to Proto conversion as an alternative input format.
verification: security_reviewed
source: https://agentskillexchange.com/skills/protobuf-schema-generator-from-json/
category:
- Data Extraction &amp; Transformation
framework:
- Gemini
---

# Protocol Buffer Schema Generator

The Protocol Buffer Schema Generator skill automatically infers .proto schema definitions from JSON sample data, eliminating the manual work of writing Protocol Buffer schemas for existing JSON APIs. It analyzes one or more JSON documents to determine field types, detect repeated fields (arrays), identify nested message structures, and recognize enum candidates (fields with a small set of string values). The inference engine uses statistical analysis across multiple samples to distinguish between optional and required fields, detect union types that need oneof declarations, and choose optimal numeric types (int32 vs int64, float vs double). Generated schemas follow proto3 syntax with proper package namespacing, import statements for well-known types (Timestamp, Duration, Any), and comprehensive field comments documenting observed value ranges and patterns. When gRPC service generation is enabled, the tool creates service definitions with standard CRUD RPCs based on detected resource patterns. The generated .proto files are validated using protoc compiler, and optional code generation produces Python, Go, or TypeScript stubs via grpcio-tools. Supports JSON Schema to Proto conversion as an alternative input format.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-schema-generator-from-json/)
