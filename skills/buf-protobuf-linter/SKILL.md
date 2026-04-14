---
title: "Buf Protobuf Linter"
description: "Lints Protocol Buffer definitions using the Buf CLI ruleset and validates gRPC service contracts. Detects breaking changes between proto revisions using buf breaking with git integration."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/buf-protobuf-linter/"
category:
  - "Library &amp; API Reference"
framework:
  - "Claude Code"
---

# Buf Protobuf Linter

The Buf Protobuf Linter enforces style and compatibility rules on Protocol Buffer definition files using the Buf CLI toolchain. It applies the buf lint ruleset covering package naming, field numbering conventions, enum value prefixes, service method naming, and import organization. Breaking change detection uses buf breaking to compare proto definitions across git revisions, catching field type changes, removed RPCs, changed field numbers, and narrowed oneof options. The skill supports buf.yaml configuration with custom lint rules and breaking change exception lists for intentional modifications. It validates well-known types usage (google.protobuf.Timestamp, Any, Struct) and checks for proper use of FieldMask in update RPCs. gRPC service contract analysis verifies streaming patterns (unary, server-streaming, client-streaming, bidirectional) match their intended use cases. The skill generates documentation from proto comments using protoc-gen-doc and creates Markdown API references with message field tables.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buf-protobuf-linter/)
