---
title: "Protocol Buffers Documentation Compiler"
description: "Compiles Protocol Buffer .proto files using protoc and generates API documentation with protoc-gen-doc. Validates proto style with buf lint and produces gRPC service client stubs for multiple languages."
slug: "protobuf-documentation-compiler"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/protobuf-documentation-compiler/"
listed: true
---

# Protocol Buffers Documentation Compiler

Compiles Protocol Buffer .proto files using protoc and generates API documentation with protoc-gen-doc. Validates proto style with buf lint and produces gRPC service client stubs for multiple languages.

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
clawhub install protobuf-documentation-compiler
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Protocol Buffers Documentation Compiler skill processes .proto file collections to generate comprehensive gRPC service documentation and client libraries. It uses buf for dependency management, compilation, and linting with configurable lint categories including MINIMAL, BASIC, and DEFAULT rule sets enforcing naming conventions, package structure, and field numbering best practices. The skill generates multi-format documentation using protoc-gen-doc with HTML, Markdown, and JSON output templates, including service method descriptions, message field tables, and enum value documentation extracted from proto comments. It compiles gRPC client stubs via protoc with language-specific plugins for Go (protoc-gen-go-grpc), Python (grpcio-tools), and TypeScript (ts-proto) with custom output options. The compiler validates backward compatibility using buf breaking with FILE and PACKAGE level checks against git references, detects wire-incompatible changes, and generates migration guides for breaking changes. It also produces Postman gRPC request collections using grpcurl reflection output.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-documentation-compiler/)
