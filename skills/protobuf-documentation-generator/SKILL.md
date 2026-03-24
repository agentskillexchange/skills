---
name: "Protobuf Documentation Generator"
description: "Generates API documentation from Protocol Buffer definitions using protoc-gen-doc and buf build toolchain. Produces Markdown, HTML, and DocJSON output with cross-linked message and service references."
category: "Library & API Reference"
framework: "Gemini"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/protobuf-documentation-generator/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "grpc"  # from ase_tool_match
  github_stars: 4816  # from ase_github_stars (integer, not string)
  npm_weekly_downloads: 30883690  # from ase_npm_downloads
  github_repo: "grpc/grpc-node"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# Protobuf Documentation Generator

Generates API documentation from Protocol Buffer definitions using protoc-gen-doc and buf build toolchain. Produces Markdown, HTML, and DocJSON output with cross-linked message and service references.

## Overview

The Protobuf Documentation Generator creates comprehensive API documentation from Protocol Buffer (.proto) definition files. It leverages protoc-gen-doc as the primary documentation compiler, generating Markdown, HTML, and DocJSON output formats with full cross-referencing between messages, enums, services, and RPC methods. The tool integrates with the buf build toolchain for dependency resolution, ensuring all imported proto files from buf.build BSR (Buf Schema Registry) are available during documentation generation. It extracts documentation from proto comments (both leading and trailing) and maps them to structured documentation pages. For gRPC services, it generates per-method documentation including request/response message schemas, streaming indicators, and example payloads in JSON format using protobuf-json-mapping. The generator supports custom documentation templates using Go text/template syntax for organization-specific formatting requirements. It validates proto files using buf lint before generation, ensuring consistent naming conventions and package structure. The output includes navigable table of contents, deprecation notices, and field-level documentation with type links.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill protobuf-documentation-generator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill protobuf-documentation-generator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill protobuf-documentation-generator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill protobuf-documentation-generator -a codex
```

### OpenClaw

```bash
clawhub install protobuf-documentation-generator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/protobuf-documentation-generator/
