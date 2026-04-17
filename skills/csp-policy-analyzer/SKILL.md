---
title: "CSP Policy Analyzer"
description: "The CSP Policy Analyzer audits Content Security Policy headers for web applications to identify security weaknesses and generate hardened policy recommendations. It uses csp-parse to decompose complex CSP strings into structured directive objects and csp-evaluator (based on Google CSP Evaluator) to score each directive against known bypass techniques. The tool fetches live CSP headers from target URLs using undici HTTP client and also accepts raw policy strings for offline analysis. It detects dangerous patterns including unsafe-inline, unsafe-eval, wildcard sources, data: URI allowlists, and overly broad domain patterns that enable XSS bypasses. For each finding, it provides a severity rating, exploit scenario description, and a recommended fix with the most restrictive policy that maintains functionality. The analyzer supports CSP Level 3 features including strict-dynamic, nonce-based policies, and hash-based script allowlisting. It generates report-only headers for gradual migration from permissive to strict policies and tracks violation reports from the report-uri or report-to endpoints."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/csp-policy-analyzer/"
framework:
  - "Claude Agents"
---

# CSP Policy Analyzer

The CSP Policy Analyzer audits Content Security Policy headers for web applications to identify security weaknesses and generate hardened policy recommendations. It uses csp-parse to decompose complex CSP strings into structured directive objects and csp-evaluator (based on Google CSP Evaluator) to score each directive against known bypass techniques. The tool fetches live CSP headers from target URLs using undici HTTP client and also accepts raw policy strings for offline analysis. It detects dangerous patterns including unsafe-inline, unsafe-eval, wildcard sources, data: URI allowlists, and overly broad domain patterns that enable XSS bypasses. For each finding, it provides a severity rating, exploit scenario description, and a recommended fix with the most restrictive policy that maintains functionality. The analyzer supports CSP Level 3 features including strict-dynamic, nonce-based policies, and hash-based script allowlisting. It generates report-only headers for gradual migration from permissive to strict policies and tracks violation reports from the report-uri or report-to endpoints.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/csp-policy-analyzer
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/csp-policy-analyzer` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/csp-policy-analyzer/)
