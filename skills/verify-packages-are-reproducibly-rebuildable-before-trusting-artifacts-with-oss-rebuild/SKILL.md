---
title: "Verify Packages Are Reproducibly Rebuildable Before Trusting Artifacts With Oss Rebuild"
description: "Query OSS Rebuild attestations and rebuild metadata so an agent can verify whether a published package artifact matches a reproducible upstream rebuild."
verification: security_reviewed
source: "https://github.com/google/oss-rebuild"
category:
  - "Security & Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "google/oss-rebuild"
  github_stars: 687
---

# Verify Packages Are Reproducibly Rebuildable Before Trusting Artifacts With Oss Rebuild

OSS Rebuild is a supply-chain verification skill for checking whether published npm, PyPI, or Crates.io artifacts have corresponding rebuild attestations. An agent should invoke it when a user needs to validate package integrity before dependency approval, security review, or incident response, rather than relying on trust in the package registry alone.

Use this instead of a broad security platform when the task is specifically rebuild verification and attestation lookup. The boundary is clear: inspect rebuild results, list rebuilt versions, and surface attestation details for a package version. It is not a generic SBOM product, package manager, or security dashboard listing.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/verify-packages-are-reproducibly-rebuildable-before-trusting-artifacts-with-oss-rebuild
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/verify-packages-are-reproducibly-rebuildable-before-trusting-artifacts-with-oss-rebuild` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-packages-are-reproducibly-rebuildable-before-trusting-artifacts-with-oss-rebuild/)
