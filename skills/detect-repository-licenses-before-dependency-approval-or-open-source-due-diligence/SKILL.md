---
title: "Detect repository licenses before dependency approval or open-source due diligence"
description: "Tool: Licensee. This skill gives an agent a narrow job: inspect a repository, read the license file the way Licensee does, and return a concrete answer about which known license the project most closely matches before anyone treats the code as safe to use, ship, or redistribute. That is useful in dependency intake, vendor reviews, open-source due diligence, and internal audits where the failure mode is not malicious code, but bad assumptions about licensing.\nWhen to use it: invoke this skill when an agent is triaging a new repository, reviewing transitive dependencies, checking whether an archived project is still usable, or preparing a release package that pulls in third-party code. In those situations, using the product normally would mean manually opening LICENSE files, guessing whether edited text still maps to MIT, Apache-2.0, GPL, or something custom, and repeating that work for every repository. The agent can use Licensee to turn that into a repeatable check and hand back a specific result plus the confidence context needed for human review.\nScope boundary: this is not a full legal-compliance platform, policy engine, or software bill of materials workflow. It does not decide whether a license is acceptable for your organization, generate counsel-ready guidance, or track obligations across deployments. Its boundary is much tighter: identify the project license from repository contents and surface that result early enough for a human or another system to act on it.\nIntegration points: GitHub and Git clones, dependency-vetting pipelines, procurement checklists, CI guardrails, and internal repository scanners. Upstream sources are the Licensee GitHub repository and official documentation site, with active maintenance and current repository activity."
verification: security_reviewed
source: "https://github.com/licensee/licensee"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "licensee/licensee"
  github_stars: 876
---

# Detect repository licenses before dependency approval or open-source due diligence

Tool: Licensee. This skill gives an agent a narrow job: inspect a repository, read the license file the way Licensee does, and return a concrete answer about which known license the project most closely matches before anyone treats the code as safe to use, ship, or redistribute. That is useful in dependency intake, vendor reviews, open-source due diligence, and internal audits where the failure mode is not malicious code, but bad assumptions about licensing.
When to use it: invoke this skill when an agent is triaging a new repository, reviewing transitive dependencies, checking whether an archived project is still usable, or preparing a release package that pulls in third-party code. In those situations, using the product normally would mean manually opening LICENSE files, guessing whether edited text still maps to MIT, Apache-2.0, GPL, or something custom, and repeating that work for every repository. The agent can use Licensee to turn that into a repeatable check and hand back a specific result plus the confidence context needed for human review.
Scope boundary: this is not a full legal-compliance platform, policy engine, or software bill of materials workflow. It does not decide whether a license is acceptable for your organization, generate counsel-ready guidance, or track obligations across deployments. Its boundary is much tighter: identify the project license from repository contents and surface that result early enough for a human or another system to act on it.
Integration points: GitHub and Git clones, dependency-vetting pipelines, procurement checklists, CI guardrails, and internal repository scanners. Upstream sources are the Licensee GitHub repository and official documentation site, with active maintenance and current repository activity.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/detect-repository-licenses-before-dependency-approval-or-open-source-due-diligence
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/detect-repository-licenses-before-dependency-approval-or-open-source-due-diligence` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/detect-repository-licenses-before-dependency-approval-or-open-source-due-diligence/)
