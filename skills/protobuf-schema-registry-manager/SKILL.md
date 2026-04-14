---
title: "Protobuf Schema Registry Manager"
description: "Manages Protocol Buffer schema evolution using buf CLI with breaking change detection and Confluent Schema Registry integration. Enforces buf lint rules and generates gRPC service stubs via protoc-gen-go and protoc-gen-grpc-web."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/protobuf-schema-registry-manager/"
category:
  - "Library &amp; API Reference"
framework:
  - "Codex"
---

# Protobuf Schema Registry Manager

The Protobuf Schema Registry Manager provides comprehensive Protocol Buffer schema lifecycle management using the buf CLI toolchain. It enforces schema quality through configurable buf lint rules covering naming conventions, field numbering, package organization, and service definition patterns. Breaking change detection via buf breaking compares current schemas against the Git baseline, preventing backwards-incompatible changes from reaching production. Integration with Confluent Schema Registry enables centralized schema storage with compatibility mode enforcement (BACKWARD, FORWARD, FULL). The manager generates gRPC service stubs using protoc-gen-go for Go servers, protoc-gen-grpc-web for browser clients, and protoc-gen-ts for TypeScript definitions. It handles proto file dependency resolution across multiple roots and supports Buf Schema Registry (BSR) for publishing and consuming shared proto packages. Schema evolution workflows include automated migration script generation when breaking changes are intentionally introduced, with field deprecation tracking and removal timelines.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-schema-registry-manager/)
