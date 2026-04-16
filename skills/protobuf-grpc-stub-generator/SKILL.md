---
title: "Protobuf & gRPC Stub Generator"
description: "Compiles Protocol Buffer definitions into language-specific gRPC client and server stubs using buf CLI and protoc plugins. Validates proto files against Buf lint rules and detects breaking changes."
verification: "security_reviewed"
source: "https://github.com/grpc/grpc-node"
category:
  - "Library &amp; API Reference"
framework:
  - "Cursor"
tool_ecosystem:
  github_repo: "grpc/grpc-node"
  github_stars: 4822
  license: "Apache-2.0"
---

# Protobuf & gRPC Stub Generator

This skill manages Protocol Buffer compilation and gRPC code generation using the Buf CLI toolchain. It validates .proto files against configurable Buf lint rules including package naming conventions, field naming standards, and service method patterns. Breaking change detection compares current proto definitions against git-tracked baselines, identifying removed fields, changed types, and incompatible enum modifications. The generator produces gRPC stubs for Go, Python, TypeScript, Java, and Rust using language-specific protoc plugins with optimized serialization options. Client stubs include interceptor chains for authentication metadata injection, distributed tracing context propagation via OpenTelemetry, and deadline management. Server stubs generate interface definitions with health check and reflection service registration. The skill configures Buf Schema Registry publishing for team-wide proto dependency management. Mock server generation creates in-memory gRPC servers for integration testing with configurable response fixtures. Documentation generation produces markdown API references from proto comments with rendered message diagrams.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-grpc-stub-generator/)
