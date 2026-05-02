---
title: "Protobuf Schema Registry Manager"
description: "Manages Protocol Buffer schema evolution using buf CLI with breaking change detection and Confluent Schema Registry integration. Enforces buf lint rules and generates gRPC service stubs via protoc-gen-go and protoc-gen-grpc-web."
verification: "security_reviewed"
source: "https://github.com/bufbuild/buf"
category:
  - "Library & API Reference"
framework:
  - "Codex"
tool_ecosystem:
  github_repo: "bufbuild/buf"
  github_stars: 11051
---

# Protobuf Schema Registry Manager

The Protobuf Schema Registry Manager provides comprehensive Protocol Buffer schema lifecycle management using the buf CLI toolchain. It enforces schema quality through configurable buf lint rules covering naming conventions, field numbering, package organization, and service definition patterns. Breaking change detection via buf breaking compares current schemas against the Git baseline, preventing backwards-incompatible changes from reaching production. Integration with Confluent Schema Registry enables centralized schema storage with compatibility mode enforcement (BACKWARD, FORWARD, FULL). The manager generates gRPC service stubs using protoc-gen-go for Go servers, protoc-gen-grpc-web for browser clients, and protoc-gen-ts for TypeScript definitions. It handles proto file dependency resolution across multiple roots and supports Buf Schema Registry (BSR) for publishing and consuming shared proto packages. Schema evolution workflows include automated migration script generation when breaking changes are intentionally introduced, with field deprecation tracking and removal timelines.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/protobuf-schema-registry-manager/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/protobuf-schema-registry-manager
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/protobuf-schema-registry-manager`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-schema-registry-manager/)
