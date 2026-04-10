---
title: "Protobuf & gRPC Stub Generator"
description: "Compiles Protocol Buffer definitions into language-specific gRPC client and server stubs using buf CLI and protoc plugins. Validates proto files against Buf lint rules and detects breaking changes."
slug: "protobuf-grpc-stub-generator"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/protobuf-grpc-stub-generator/"
listed: true
---

# Protobuf & gRPC Stub Generator

Compiles Protocol Buffer definitions into language-specific gRPC client and server stubs using buf CLI and protoc plugins. Validates proto files against Buf lint rules and detects breaking changes.

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
clawhub install protobuf-grpc-stub-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

This skill manages Protocol Buffer compilation and gRPC code generation using the Buf CLI toolchain. It validates .proto files against configurable Buf lint rules including package naming conventions, field naming standards, and service method patterns. Breaking change detection compares current proto definitions against git-tracked baselines, identifying removed fields, changed types, and incompatible enum modifications. The generator produces gRPC stubs for Go, Python, TypeScript, Java, and Rust using language-specific protoc plugins with optimized serialization options. Client stubs include interceptor chains for authentication metadata injection, distributed tracing context propagation via OpenTelemetry, and deadline management. Server stubs generate interface definitions with health check and reflection service registration. The skill configures Buf Schema Registry publishing for team-wide proto dependency management. Mock server generation creates in-memory gRPC servers for integration testing with configurable response fixtures. Documentation generation produces markdown API references from proto comments with rendered message diagrams.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-grpc-stub-generator/)
