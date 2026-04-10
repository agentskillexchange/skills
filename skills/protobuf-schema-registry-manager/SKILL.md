---
title: "Protobuf Schema Registry Manager"
description: "Manages Protocol Buffer schema evolution using buf CLI with breaking change detection and Confluent Schema Registry integration. Enforces buf lint rules and generates gRPC service stubs via protoc-gen-go and protoc-gen-grpc-web."
slug: "protobuf-schema-registry-manager"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/protobuf-schema-registry-manager/"
---

# Protobuf Schema Registry Manager

Manages Protocol Buffer schema evolution using buf CLI with breaking change detection and Confluent Schema Registry integration. Enforces buf lint rules and generates gRPC service stubs via protoc-gen-go and protoc-gen-grpc-web.

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
clawhub install protobuf-schema-registry-manager
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Protobuf Schema Registry Manager provides comprehensive Protocol Buffer schema lifecycle management using the buf CLI toolchain. It enforces schema quality through configurable buf lint rules covering naming conventions, field numbering, package organization, and service definition patterns. Breaking change detection via buf breaking compares current schemas against the Git baseline, preventing backwards-incompatible changes from reaching production. Integration with Confluent Schema Registry enables centralized schema storage with compatibility mode enforcement (BACKWARD, FORWARD, FULL). The manager generates gRPC service stubs using protoc-gen-go for Go servers, protoc-gen-grpc-web for browser clients, and protoc-gen-ts for TypeScript definitions. It handles proto file dependency resolution across multiple roots and supports Buf Schema Registry (BSR) for publishing and consuming shared proto packages. Schema evolution workflows include automated migration script generation when breaking changes are intentionally introduced, with field deprecation tracking and removal timelines.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-schema-registry-manager/)
