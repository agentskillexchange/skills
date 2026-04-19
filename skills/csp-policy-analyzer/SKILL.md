---
title: "CSP Policy Analyzer"
description: "The CSP Policy Analyzer audits Content Security Policy headers for web applications to identify security weaknesses and generate hardened policy recommendations. It uses csp-parse to decompose complex CSP strings into structured directive objects and csp-evaluator (based on Google CSP Evaluator) to score each directive against known bypass techniques. The tool fetches live CSP headers from target URLs using undici HTTP client and also accepts raw policy strings for offline analysis. It detects dangerous patterns including unsafe-inline, unsafe-eval, wildcard sources, data: URI allowlists, and overly broad domain patterns that enable XSS bypasses. For each finding, it provides a severity rating, exploit scenario description, and a recommended fix with the most restrictive policy that maintains functionality. The analyzer supports CSP Level 3 features including strict-dynamic, nonce-based policies, and hash-based script allowlisting. It generates report-only headers for gradual migration from permissive to strict policies and tracks violation reports from the report-uri or report-to endpoints."
source: "https://agentskillexchange.com/skills/csp-policy-analyzer/"
verification: "security_reviewed"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Agents"
---

# CSP Policy Analyzer

The CSP Policy Analyzer audits Content Security Policy headers for web applications to identify security weaknesses and generate hardened policy recommendations. It uses csp-parse to decompose complex CSP strings into structured directive objects and csp-evaluator (based on Google CSP Evaluator) to score each directive against known bypass techniques. The tool fetches live CSP headers from target URLs using undici HTTP client and also accepts raw policy strings for offline analysis. It detects dangerous patterns including unsafe-inline, unsafe-eval, wildcard sources, data: URI allowlists, and overly broad domain patterns that enable XSS bypasses. For each finding, it provides a severity rating, exploit scenario description, and a recommended fix with the most restrictive policy that maintains functionality. The analyzer supports CSP Level 3 features including strict-dynamic, nonce-based policies, and hash-based script allowlisting. It generates report-only headers for gradual migration from permissive to strict policies and tracks violation reports from the report-uri or report-to endpoints.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/csp-policy-analyzer/)
