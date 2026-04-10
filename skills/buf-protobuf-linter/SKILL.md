---
name: Buf Protobuf Linter
description: Lints Protocol Buffer definitions using the Buf CLI ruleset and validates
  gRPC service contracts. Detects breaking changes between proto revisions using buf
  breaking with git integration.
verification: security_reviewed
source: https://agentskillexchange.com/skills/buf-protobuf-linter/
category:
- Library &amp; API Reference
framework:
- Claude Code
---
# Buf Protobuf Linter

The Buf Protobuf Linter enforces style and compatibility rules on Protocol Buffer definition files using the Buf CLI toolchain. It applies the buf lint ruleset covering package naming, field numbering conventions, enum value prefixes, service method naming, and import organization. Breaking change detection uses buf breaking to compare proto definitions across git revisions, catching field type changes, removed RPCs, changed field numbers, and narrowed oneof options. The skill supports buf.yaml configuration with custom lint rules and breaking change exception lists for intentional modifications. It validates well-known types usage (google.protobuf.Timestamp, Any, Struct) and checks for proper use of FieldMask in update RPCs. gRPC service contract analysis verifies streaming patterns (unary, server-streaming, client-streaming, bidirectional) match their intended use cases. The skill generates documentation from proto comments using protoc-gen-doc and creates Markdown API references with message field tables.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buf-protobuf-linter/)
