---
name: "Sigstore Cosign Container Signature Checker"
description: "Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline."
category: "Security &amp; Verification"
framework: ""
verification: listed
rating: 0
reviews: 0
creator: ""
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/sigstore-cosign-container-signature-checker/"
---

# Sigstore Cosign Container Signature Checker

Checks container trust with `cosign verify`, Rekor transparency log lookups, and OCI image reference inspection. Useful for agents that need to confirm whether an image was actually signed and recorded before it reaches a deployment pipeline.

## Installation

### Any Agent (npx)
```bash
npx @anthropic/agent-skills add sigstore-cosign-container-signature-checker
```

### Claude Code
```bash
npx @anthropic/agent-skills add sigstore-cosign-container-signature-checker --target claude-code
```

### Cursor
```bash
npx @anthropic/agent-skills add sigstore-cosign-container-signature-checker --target cursor
```

### Codex
```bash
npx @anthropic/agent-skills add sigstore-cosign-container-signature-checker --target codex
```

### OpenClaw
```bash
clawhub install sigstore-cosign-container-signature-checker
```
