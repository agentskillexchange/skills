---
title: "Protobuf Schema Registry Manager"
description: "Manages Protocol Buffer schema evolution using buf CLI with breaking change detection and Confluent Schema Registry integration. Enforces buf lint rules and generates gRPC service stubs via protoc-gen-go and protoc-gen-grpc-web."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/protobuf-schema-registry-manager/"
category:
  - "Library & API Reference"
framework:
  - "Codex"
---

# Protobuf Schema Registry Manager

The Protobuf Schema Registry Manager provides comprehensive Protocol Buffer schema lifecycle management using the buf CLI toolchain. It enforces schema quality through configurable buf lint rules covering naming conventions, field numbering, package organization, and service definition patterns. Breaking change detection via buf breaking compares current schemas against the Git baseline, preventing backwards-incompatible changes from reaching production. Integration with Confluent Schema Registry enables centralized schema storage with compatibility mode enforcement (BACKWARD, FORWARD, FULL). The manager generates gRPC service stubs using protoc-gen-go for Go servers, protoc-gen-grpc-web for browser clients, and protoc-gen-ts for TypeScript definitions. It handles proto file dependency resolution across multiple roots and supports Buf Schema Registry (BSR) for publishing and consuming shared proto packages. Schema evolution workflows include automated migration script generation when breaking changes are intentionally introduced, with field deprecation tracking and removal timelines.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/protobuf-schema-registry-manager
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/protobuf-schema-registry-manager` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-schema-registry-manager/)
