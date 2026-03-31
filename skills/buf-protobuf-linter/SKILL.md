---
name: "Buf Protobuf Linter"
description: "Lints Protocol Buffer definitions using the Buf CLI ruleset and validates gRPC service contracts. Detects breaking changes between proto revisions using buf breaking with git integration."
category: "Library & API Reference"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/buf-protobuf-linter/"
---
# Buf Protobuf Linter

Lints Protocol Buffer definitions using the Buf CLI ruleset and validates gRPC service contracts. Detects breaking changes between proto revisions using buf breaking with git integration.

## Overview

The Buf Protobuf Linter enforces style and compatibility rules on Protocol Buffer definition files using the Buf CLI toolchain. It applies the buf lint ruleset covering package naming, field numbering conventions, enum value prefixes, service method naming, and import organization. Breaking change detection uses buf breaking to compare proto definitions across git revisions, catching field type changes, removed RPCs, changed field numbers, and narrowed oneof options. The skill supports buf.yaml configuration with custom lint rules and breaking change exception lists for intentional modifications. It validates well-known types usage (google.protobuf.Timestamp, Any, Struct) and checks for proper use of FieldMask in update RPCs. gRPC service contract analysis verifies streaming patterns (unary, server-streaming, client-streaming, bidirectional) match their intended use cases. The skill generates documentation from proto comments using protoc-gen-doc and creates Markdown API references with message field tables.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill buf-protobuf-linter
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill buf-protobuf-linter -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill buf-protobuf-linter -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill buf-protobuf-linter -a codex
```

### OpenClaw

```bash
clawhub install buf-protobuf-linter
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/buf-protobuf-linter/)
