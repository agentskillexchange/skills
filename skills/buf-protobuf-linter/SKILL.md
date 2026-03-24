---
name: "Buf Protobuf Linter"
description: "Lints Protocol Buffer definitions using the Buf CLI ruleset and validates gRPC service contracts. Detects breaking changes between proto revisions using buf breaking with git integration."
category: "Library & API Reference"
framework: "Claude Code"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/buf-protobuf-linter/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "grpc"  # from ase_tool_match
  github_stars: 4816  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 30883690  # from ase_npm_downloads
  github_repo: "grpc/grpc-node"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
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

- Marketplace: https://agentskillexchange.com/skills/buf-protobuf-linter/
