---
name: "Run authorized security research pipelines in Claude Code with RAPTOR"
slug: "run-authorized-security-research-pipelines-in-claude-code-with-raptor"
description: "RAPTOR turns Claude Code into an evidence-first offensive and defensive security research workflow for mapping attack surfaces, validating scanner findings, analyzing binaries, generating patches, and tracking project findings."
github_stars: 3348
verification: "security_reviewed"
source: "https://github.com/gadievron/raptor"
author: "Gadi Evron, Daniel Cuthbert, Thomas Dullien, Michael Bargury, and John Cartwright"
publisher_type: "individuals"
category: "Security & Verification"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "gadievron/raptor"
  github_stars: 3348
---

# Run authorized security research pipelines in Claude Code with RAPTOR

RAPTOR turns Claude Code into an evidence-first offensive and defensive security research workflow for mapping attack surfaces, validating scanner findings, analyzing binaries, generating patches, and tracking project findings.

## Prerequisites

Claude Code, Python dependencies from the repository, Semgrep, CodeQL for relevant scans, optional Docker devcontainer or privileged container for rr/debugger-backed binary workflows, and authorization to test the target codebase or artifact.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/gadievron/raptor.git
- pip install -r requirements.txt
- npm install @anthropic-ai/claude-code
- npm install -g @anthropic-ai/claude-code

Requirements and caveats from upstream:
- The --privileged flag is required for the rr deterministic debugger. The image is large (around 6 GB). It starts from the Microsoft Python 3.12 devcontainer and adds static analysis, fuzzing, and browser automation to...
- The **Python execution layer** (raptor.py, packages/, core/, engine/) handles the heavy lifting: running Semgrep and CodeQL, managing subprocesses, parsing SARIF, deduplicating findings, dispatching LLM API calls, tra...

Basic usage or getting-started notes:
- cd raptor
- claude
- Everything pre-installed. Open in VS Code with **Dev Containers: Open Folder in Container**, or pull the prebuilt image:

- Source: https://github.com/gadievron/raptor
- Extracted from upstream docs: https://raw.githubusercontent.com/gadievron/raptor/HEAD/README.md

## Documentation

- https://github.com/gadievron/raptor

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/run-authorized-security-research-pipelines-in-claude-code-with-raptor/)
