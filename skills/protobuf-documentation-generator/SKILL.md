---
title: "Protobuf Documentation Generator"
description: "Generates API documentation from Protocol Buffer definitions using protoc-gen-doc and buf build toolchain. Produces Markdown, HTML, and DocJSON output with cross-linked message and service references."
slug: "protobuf-documentation-generator"
category:
  - "Library &amp; API Reference"
framework:
  - "Gemini"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/protobuf-documentation-generator/"
---

# Protobuf Documentation Generator

Generates API documentation from Protocol Buffer definitions using protoc-gen-doc and buf build toolchain. Produces Markdown, HTML, and DocJSON output with cross-linked message and service references.

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
clawhub install protobuf-documentation-generator
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Protobuf Documentation Generator creates comprehensive API documentation from Protocol Buffer (.proto) definition files. It leverages protoc-gen-doc as the primary documentation compiler, generating Markdown, HTML, and DocJSON output formats with full cross-referencing between messages, enums, services, and RPC methods. The tool integrates with the buf build toolchain for dependency resolution, ensuring all imported proto files from buf.build BSR (Buf Schema Registry) are available during documentation generation. It extracts documentation from proto comments (both leading and trailing) and maps them to structured documentation pages. For gRPC services, it generates per-method documentation including request/response message schemas, streaming indicators, and example payloads in JSON format using protobuf-json-mapping. The generator supports custom documentation templates using Go text/template syntax for organization-specific formatting requirements. It validates proto files using buf lint before generation, ensuring consistent naming conventions and package structure. The output includes navigable table of contents, deprecation notices, and field-level documentation with type links.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-documentation-generator/)
