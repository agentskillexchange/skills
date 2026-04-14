---
title: "Detect repository licenses before dependency approval or open-source due diligence"
description: "Use Licensee when an agent needs to inspect a repository and determine what license text it actually matches before a dependency is approved or a codebase is redistributed. The skill is about evidence-backed license detection, not legal advice or broader compliance automation."
verification: security_reviewed
source: "https://github.com/licensee/licensee"
category:
  - "Security &amp; Verification"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/detect-repository-licenses-before-dependency-approval-or-open-source-due-diligence/)
