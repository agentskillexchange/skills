---
title: "Protobuf & gRPC Stub Generator"
description: "Compiles Protocol Buffer definitions into language-specific gRPC client and server stubs using buf CLI and protoc plugins. Validates proto files against Buf lint rules and detects breaking changes."
verification: "security_reviewed"
source: "https://github.com/grpc/grpc-node"
category:
  - "Library & API Reference"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grpc/grpc-node"
  github_stars: 4822
---

# Protobuf & gRPC Stub Generator

This skill manages Protocol Buffer compilation and gRPC code generation using the Buf CLI toolchain. It validates .proto files against configurable Buf lint rules including package naming conventions, field naming standards, and service method patterns. Breaking change detection compares current proto definitions against git-tracked baselines, identifying removed fields, changed types, and incompatible enum modifications. The generator produces gRPC stubs for Go, Python, TypeScript, Java, and Rust using language-specific protoc plugins with optimized serialization options. Client stubs include interceptor chains for authentication metadata injection, distributed tracing context propagation via OpenTelemetry, and deadline management. Server stubs generate interface definitions with health check and reflection service registration. The skill configures Buf Schema Registry publishing for team-wide proto dependency management. Mock server generation creates in-memory gRPC servers for integration testing with configurable response fixtures. Documentation generation produces markdown API references from proto comments with rendered message diagrams.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/protobuf-grpc-stub-generator/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/protobuf-grpc-stub-generator
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/protobuf-grpc-stub-generator`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-grpc-stub-generator/)
