---
name: "SHAR Production Metadata Validation"
slug: "shar-production-metadata-validation"
description: "Uses the SHAR Production Metadata MCP local stdio server to validate rights-aware production metadata manifests before an AI-hybrid video-production asset is treated as releasable."
category: "Security & Verification"
framework: "MCP"
verification: listed
source: "https://github.com/SHARProduction/production-metadata-mcp"
tool_ecosystem:
  tool: "SHAR Production Metadata MCP"
  github_repo: "SHARProduction/production-metadata-mcp"
  license: "MIT"
  maintained: true
---

# SHAR Production Metadata Validation

Use this skill when an agent needs to check whether a production metadata manifest has enough rights-aware information to be considered releasable. It is designed for AI-hybrid video-production workflows where an agent must not infer usage rights, availability windows, or release clearance from incomplete data. The skill invokes the local SHAR Production Metadata MCP server over stdio and reads its deterministic validation result before recommending release, handoff, or publication.

The server is read-only. It does not call network services, modify files, publish content, or accept credentials. Provide only the manifest that the user has authorized the agent to inspect. Treat a failed validation or a non-releasable result as a reason to ask for corrected metadata; do not silently fill missing rights data.

## Setup

Clone the upstream repository and install its locked dependencies:

```bash
git clone https://github.com/SHARProduction/production-metadata-mcp.git
cd production-metadata-mcp
npm ci
```

Configure an MCP-compatible client to launch the server with:

```text
node /absolute/path/to/production-metadata-mcp/server.js
```

## Workflow

1. Send the candidate production metadata manifest to `validate_production_manifest`.
2. Read the returned validation result and the reported field-level reasons.
3. Recommend release only when the result is releasable.
4. Preserve the original manifest and report missing or contradictory metadata to the user.

## Verification boundary

This skill validates metadata structure and declared rights-aware constraints. It does not independently establish legal ownership, obtain licences, contact rightsholders, or publish a production asset.