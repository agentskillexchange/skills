---
title: "Detect repository licenses before dependency approval or open-source due diligence"
description: "Tool: Licensee. This skill gives an agent a narrow job: inspect a repository, read the license file the way Licensee does, and return a concrete answer about which known license the project most closely matches before anyone treats the code as safe to use, ship, or redistribute. That is useful in dependency intake, vendor reviews, open-source due diligence, and internal audits where the failure mode is not malicious code, but bad assumptions about licensing. When to use it: invoke this skill when an agent is triaging a new repository, reviewing transitive dependencies, checking whether an archived project is still usable, or preparing a release package that pulls in third-party code. In those situations, using the product normally would mean manually opening LICENSE files, guessing whether edited text still maps to MIT, Apache-2.0, GPL, or something custom, and repeating that work for every repository. The agent can use Licensee to turn that into a repeatable check and hand back a specific result plus the confidence context needed for human review. Scope boundary: this is not a full legal-compliance platform, policy engine, or software bill of materials workflow. It does not decide whether a license is acceptable for your organization, generate counsel-ready guidance, or track obligations across deployments. Its boundary is much tighter: identify the project license from repository contents and surface that result early enough for a human or another system to act on it. Integration points: GitHub and Git clones, dependency-vetting pipelines, procurement checklists, CI guardrails, and internal repository scanners. Upstream sources are the Licensee GitHub repository and official documentation site, with active maintenance and current repository activity."
source: "https://github.com/licensee/licensee"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "licensee/licensee"
  github_stars: 876
---

# Detect repository licenses before dependency approval or open-source due diligence

Tool: Licensee. This skill gives an agent a narrow job: inspect a repository, read the license file the way Licensee does, and return a concrete answer about which known license the project most closely matches before anyone treats the code as safe to use, ship, or redistribute. That is useful in dependency intake, vendor reviews, open-source due diligence, and internal audits where the failure mode is not malicious code, but bad assumptions about licensing. When to use it: invoke this skill when an agent is triaging a new repository, reviewing transitive dependencies, checking whether an archived project is still usable, or preparing a release package that pulls in third-party code. In those situations, using the product normally would mean manually opening LICENSE files, guessing whether edited text still maps to MIT, Apache-2.0, GPL, or something custom, and repeating that work for every repository. The agent can use Licensee to turn that into a repeatable check and hand back a specific result plus the confidence context needed for human review. Scope boundary: this is not a full legal-compliance platform, policy engine, or software bill of materials workflow. It does not decide whether a license is acceptable for your organization, generate counsel-ready guidance, or track obligations across deployments. Its boundary is much tighter: identify the project license from repository contents and surface that result early enough for a human or another system to act on it. Integration points: GitHub and Git clones, dependency-vetting pipelines, procurement checklists, CI guardrails, and internal repository scanners. Upstream sources are the Licensee GitHub repository and official documentation site, with active maintenance and current repository activity.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/detect-repository-licenses-before-dependency-approval-or-open-source-due-diligence/)
