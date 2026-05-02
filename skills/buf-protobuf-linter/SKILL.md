---
title: "Buf Protobuf Linter"
description: "Lints Protocol Buffer definitions using the Buf CLI ruleset and validates gRPC service contracts. Detects breaking changes between proto revisions using buf breaking with git integration."
verification: "security_reviewed"
source: "https://github.com/bufbuild/buf"
category:
  - "Library & API Reference"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "bufbuild/buf"
  github_stars: 11049
---

# Buf Protobuf Linter

The Buf Protobuf Linter enforces style and compatibility rules on Protocol Buffer definition files using the Buf CLI toolchain. It applies the buf lint ruleset covering package naming, field numbering conventions, enum value prefixes, service method naming, and import organization. Breaking change detection uses buf breaking to compare proto definitions across git revisions, catching field type changes, removed RPCs, changed field numbers, and narrowed oneof options. The skill supports buf.yaml configuration with custom lint rules and breaking change exception lists for intentional modifications. It validates well-known types usage (google.protobuf.Timestamp, Any, Struct) and checks for proper use of FieldMask in update RPCs. gRPC service contract analysis verifies streaming patterns (unary, server-streaming, client-streaming, bidirectional) match their intended use cases. The skill generates documentation from proto comments using protoc-gen-doc and creates Markdown API references with message field tables.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/buf-protobuf-linter/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/buf-protobuf-linter
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/buf-protobuf-linter`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buf-protobuf-linter/)
