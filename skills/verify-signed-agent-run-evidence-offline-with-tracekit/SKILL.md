---
name: "Verify signed agent-run evidence offline with Tracekit"
slug: "verify-signed-agent-run-evidence-offline-with-tracekit"
description: "Check an authorized Tracekit bundle against pinned signer keys and report integrity verdicts separately from execution and completeness claims."
github_stars: 726
verification: "security_reviewed"
source: "https://github.com/Cygnux-Labs/Tracekit"
author: "Cygnux-Labs"
publisher_type: "Community"
category: "Security & Verification"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Cygnux-Labs/Tracekit"
  github_stars: 726
---

# Verify signed agent-run evidence offline with Tracekit

Check an authorized Tracekit bundle against pinned signer keys and report integrity verdicts separately from execution and completeness claims.

## Prerequisites

Python, tracekit-ai verifier, authorized .tkb evidence bundle and independently trusted signer public key

## Installation

Install or set up from the source-backed instructions:

Install the upstream verifier with pip install --no-deps tracekit-ai for the documented v1 sample bundles; install appropriate dependencies for other supported formats and integrations. Obtain fixture bundles and signer.pub from a trusted upstream checkout. No agent hooks or signer service are required for this offline verification workflow.

- Source: https://github.com/Cygnux-Labs/Tracekit

## Documentation

- https://github.com/Cygnux-Labs/Tracekit#readme

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-signed-agent-run-evidence-offline-with-tracekit/)
