---
title: "Review REST API designs before implementation for versioning, security, and contract clarity"
description: "Review an API design, endpoint set, or OpenAPI spec before implementation and return prioritized findings on design quality, security, resilience, and missing contract decisions."
verification: "security_reviewed"
source: "https://github.com/psenger/ai-agent-skills/tree/main/skills/review-api-design"
category:
  - "Code Quality & Review"
framework:
  - "Claude Code"
tool_ecosystem:
  github_repo: "psenger/ai-agent-skills"
---

# Review REST API designs before implementation for versioning, security, and contract clarity

This skill lets an agent review a REST API design before code is written. The agent gathers missing context, loads the relevant reference material, evaluates the design across design principles, payloads and errors, security, resilience, and extensibility, then produces a structured review with severity levels, concrete recommendations, and a readiness assessment.

Use this when the user is still designing an API and wants an expert review of endpoints, contracts, versioning, auth, pagination, error formats, idempotency, or integration boundaries before implementation starts. It is more appropriate than using the product normally because the value is the agent’s staged review workflow and critique, not just reading REST guidance or browsing an OpenAPI file.

The scope boundary is specific: this is not a generic API framework or REST best-practices listing. It is a planning-phase design-review workflow with explicit questions, reference routing, severity scoring, and structured output for operator decision-making.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/review-rest-api-designs-before-implementation-for-versioning-security-and-contract-clarity/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/review-rest-api-designs-before-implementation-for-versioning-security-and-contract-clarity
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/review-rest-api-designs-before-implementation-for-versioning-security-and-contract-clarity`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/review-rest-api-designs-before-implementation-for-versioning-security-and-contract-clarity/)
