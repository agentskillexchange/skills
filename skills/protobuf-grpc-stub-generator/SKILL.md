---
name: "Protobuf & gRPC Stub Generator"
description: "Compiles Protocol Buffer definitions into language-specific gRPC client and server stubs using buf CLI and protoc plugins. Validates proto files against Buf lint rules and detects breaking changes."
category: "Library & API Reference"
framework: "Cursor"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/protobuf-grpc-stub-generator/"
---
# Protobuf & gRPC Stub Generator

Compiles Protocol Buffer definitions into language-specific gRPC client and server stubs using buf CLI and protoc plugins. Validates proto files against Buf lint rules and detects breaking changes.

This skill manages Protocol Buffer compilation and gRPC code generation using the Buf CLI toolchain. It validates .proto files against configurable Buf lint rules including package naming conventions, field naming standards, and service method patterns. Breaking change detection compares current proto definitions against git-tracked baselines, identifying removed fields, changed types, and incompatible enum modifications. The generator produces gRPC stubs for Go, Python, TypeScript, Java, and Rust using language-specific protoc plugins with optimized serialization options. Client stubs include interceptor chains for authentication metadata injection, distributed tracing context propagation via OpenTelemetry, and deadline management. Server stubs generate interface definitions with health check and reflection service registration. The skill configures Buf Schema Registry publishing for team-wide proto dependency management. Mock server generation creates in-memory gRPC servers for integration testing with configurable response fixtures. Documentation generation produces markdown API references from proto comments with rendered message diagrams.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill protobuf-grpc-stub-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill protobuf-grpc-stub-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill protobuf-grpc-stub-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill protobuf-grpc-stub-generator -a codex
```

### OpenClaw

```bash
clawhub install protobuf-grpc-stub-generator
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-grpc-stub-generator/)
