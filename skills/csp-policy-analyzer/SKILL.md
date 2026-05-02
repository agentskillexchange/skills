---
title: "CSP Policy Analyzer"
description: "Parses and evaluates Content Security Policy headers using csp-parse and csp-evaluator libraries. Identifies overly permissive directives, missing protections, and generates tightened policy recommendations."
verification: "security_reviewed"
source: "https://github.com/google/csp-evaluator"
category:
  - "Security & Verification"
framework:
  - "Claude Agents"
tool_ecosystem:
  github_repo: "google/csp-evaluator"
  github_stars: 390
---

# CSP Policy Analyzer

The CSP Policy Analyzer audits Content Security Policy headers for web applications to identify security weaknesses and generate hardened policy recommendations. It uses csp-parse to decompose complex CSP strings into structured directive objects and csp-evaluator (based on Google CSP Evaluator) to score each directive against known bypass techniques. The tool fetches live CSP headers from target URLs using undici HTTP client and also accepts raw policy strings for offline analysis. It detects dangerous patterns including unsafe-inline, unsafe-eval, wildcard sources, data: URI allowlists, and overly broad domain patterns that enable XSS bypasses. For each finding, it provides a severity rating, exploit scenario description, and a recommended fix with the most restrictive policy that maintains functionality. The analyzer supports CSP Level 3 features including strict-dynamic, nonce-based policies, and hash-based script allowlisting. It generates report-only headers for gradual migration from permissive to strict policies and tracks violation reports from the report-uri or report-to endpoints.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/csp-policy-analyzer/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/csp-policy-analyzer
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/csp-policy-analyzer`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/csp-policy-analyzer/)
