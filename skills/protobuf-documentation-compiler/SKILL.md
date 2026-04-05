---
name: "Protocol Buffers Documentation Compiler"
description: "Compiles Protocol Buffer .proto files using protoc and generates API documentation with protoc-gen-doc. Validates proto style with buf lint and produces gRPC service client stubs for multiple languages."
category: "Library &amp; API Reference"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/protobuf-documentation-compiler/"
---
# Protocol Buffers Documentation Compiler

Compiles Protocol Buffer .proto files using protoc and generates API documentation with protoc-gen-doc. Validates proto style with buf lint and produces gRPC service client stubs for multiple languages.

The Protocol Buffers Documentation Compiler skill processes .proto file collections to generate comprehensive gRPC service documentation and client libraries. It uses buf for dependency management, compilation, and linting with configurable lint categories including MINIMAL, BASIC, and DEFAULT rule sets enforcing naming conventions, package structure, and field numbering best practices. The skill generates multi-format documentation using protoc-gen-doc with HTML, Markdown, and JSON output templates, including service method descriptions, message field tables, and enum value documentation extracted from proto comments. It compiles gRPC client stubs via protoc with language-specific plugins for Go (protoc-gen-go-grpc), Python (grpcio-tools), and TypeScript (ts-proto) with custom output options. The compiler validates backward compatibility using buf breaking with FILE and PACKAGE level checks against git references, detects wire-incompatible changes, and generates migration guides for breaking changes. It also produces Postman gRPC request collections using grpcurl reflection output.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill protobuf-documentation-compiler
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill protobuf-documentation-compiler -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill protobuf-documentation-compiler -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill protobuf-documentation-compiler -a codex
```

### OpenClaw

```bash
clawhub install protobuf-documentation-compiler
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-documentation-compiler/)
