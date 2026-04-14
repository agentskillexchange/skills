---
title: "Audit and normalize SPDX license headers before releasing or open-sourcing a repository"
description: "Use REUSE when an agent needs file-level licensing clarity instead of guessing from a single top-level LICENSE file. The agent checks compliance, adds or verifies SPDX headers, pulls missing license texts into LICENSES/, and produces a concrete remediation list or SPDX export."
verification: security_reviewed
source: "https://codeberg.org/fsfe/reuse-tool"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
---

# Audit and normalize SPDX license headers before releasing or open-sourcing a repository

This skill uses the REUSE tool from the Free Software Foundation Europe project to make repository licensing explicit, machine-readable, and auditable at the file level. It is built for a very specific job: checking whether a repository follows the REUSE recommendations, then helping the agent close the gaps by adding SPDX headers, confirming copyright lines, downloading missing license texts, and generating SPDX output for downstream review.

A user should invoke this skill when a repository is about to be released, open-sourced, handed to another team, or put through compliance review. In those moments, using the project “normally” as just another CLI is not enough. The agent needs a repeatable workflow: run reuse lint, identify which files are missing licensing metadata, use commands such as reuse annotate or reuse download, and rerun the check until the repository is in a predictable state. That is the job-to-be-done. It is much narrower than a generic legal-tech product card.

The boundary is also clear. This skill does not replace legal advice, does not scan for software vulnerabilities, and does not attempt broad package policy enforcement. It focuses on REUSE compliance and SPDX-oriented remediation. Official upstream docs describe package-manager installs such as apt install reuse, dnf install reuse, and pipx install reuse, plus Docker-based CI usage for automated checks. Integration points include GitHub, GitLab, and other CI systems, along with the companion docs at reuse.software and reuse.readthedocs.io.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/audit-and-normalize-spdx-license-headers-before-releasing-or-open-sourcing-a-repository/)
