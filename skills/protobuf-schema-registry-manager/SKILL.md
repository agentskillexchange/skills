---
name: "Protobuf Schema Registry Manager"
description: "Manages Protocol Buffer schema evolution using buf CLI with breaking change detection and Confluent Schema Registry integration. Enforces buf lint rules and generates gRPC service stubs via protoc-gen-go and protoc-gen-grpc-web."
category: "Library &amp; API Reference"
framework: "Codex"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/protobuf-schema-registry-manager/"
---
# Protobuf Schema Registry Manager

Manages Protocol Buffer schema evolution using buf CLI with breaking change detection and Confluent Schema Registry integration. Enforces buf lint rules and generates gRPC service stubs via protoc-gen-go and protoc-gen-grpc-web.

## Overview

The Protobuf Schema Registry Manager provides comprehensive Protocol Buffer schema lifecycle management using the buf CLI toolchain. It enforces schema quality through configurable buf lint rules covering naming conventions, field numbering, package organization, and service definition patterns. Breaking change detection via buf breaking compares current schemas against the Git baseline, preventing backwards-incompatible changes from reaching production. Integration with Confluent Schema Registry enables centralized schema storage with compatibility mode enforcement (BACKWARD, FORWARD, FULL). The manager generates gRPC service stubs using protoc-gen-go for Go servers, protoc-gen-grpc-web for browser clients, and protoc-gen-ts for TypeScript definitions. It handles proto file dependency resolution across multiple roots and supports Buf Schema Registry (BSR) for publishing and consuming shared proto packages. Schema evolution workflows include automated migration script generation when breaking changes are intentionally introduced, with field deprecation tracking and removal timelines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill protobuf-schema-registry-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill protobuf-schema-registry-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill protobuf-schema-registry-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill protobuf-schema-registry-manager -a codex
```

### OpenClaw

```bash
clawhub install protobuf-schema-registry-manager
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-schema-registry-manager/)
