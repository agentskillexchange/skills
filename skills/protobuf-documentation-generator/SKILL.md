---
name: Protobuf Documentation Generator
description: Generates API documentation from Protocol Buffer definitions using protoc-gen-doc
  and buf build toolchain. Produces Markdown, HTML, and DocJSON output with cross-linked
  message and service references.
verification: security_reviewed
source: https://agentskillexchange.com/skills/protobuf-documentation-generator/
category:
- Library &amp; API Reference
framework:
- Gemini
---
# Protobuf Documentation Generator

The Protobuf Documentation Generator creates comprehensive API documentation from Protocol Buffer (.proto) definition files. It leverages protoc-gen-doc as the primary documentation compiler, generating Markdown, HTML, and DocJSON output formats with full cross-referencing between messages, enums, services, and RPC methods. The tool integrates with the buf build toolchain for dependency resolution, ensuring all imported proto files from buf.build BSR (Buf Schema Registry) are available during documentation generation. It extracts documentation from proto comments (both leading and trailing) and maps them to structured documentation pages. For gRPC services, it generates per-method documentation including request/response message schemas, streaming indicators, and example payloads in JSON format using protobuf-json-mapping. The generator supports custom documentation templates using Go text/template syntax for organization-specific formatting requirements. It validates proto files using buf lint before generation, ensuring consistent naming conventions and package structure. The output includes navigable table of contents, deprecation notices, and field-level documentation with type links.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/protobuf-documentation-generator/)
