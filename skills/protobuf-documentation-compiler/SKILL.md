---
name: "Protocol Buffers Documentation Compiler"
description: "Compiles Protocol Buffer .proto files using protoc and generates API documentation with protoc-gen-doc. Validates proto style with buf lint and produces gRPC service client stubs for multiple languages."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/protobuf-documentation-compiler/"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
---

# Protocol Buffers Documentation Compiler

The Protocol Buffers Documentation Compiler skill processes .proto file collections to generate comprehensive gRPC service documentation and client libraries. It uses buf for dependency management, compilation, and linting with configurable lint categories including MINIMAL, BASIC, and DEFAULT rule sets enforcing naming conventions, package structure, and field numbering best practices. The skill generates multi-format documentation using protoc-gen-doc with HTML, Markdown, and JSON output templates, including service method descriptions, message field tables, and enum value documentation extracted from proto comments. It compiles gRPC client stubs via protoc with language-specific plugins for Go (protoc-gen-go-grpc), Python (grpcio-tools), and TypeScript (ts-proto) with custom output options. The compiler validates backward compatibility using buf breaking with FILE and PACKAGE level checks against git references, detects wire-incompatible changes, and generates migration guides for breaking changes. It also produces Postman gRPC request collections using grpcurl reflection output.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-documentation-compiler/)
