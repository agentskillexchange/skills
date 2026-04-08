---
title: CSP Policy Analyzer
description: 'The CSP Policy Analyzer audits Content Security Policy headers for web
  applications to identify security weaknesses and generate hardened policy recommendations.
  It uses csp-parse to decompose complex CSP strings into structured directive objects
  and csp-evaluator (based on Google CSP Evaluator) to score each directive against
  known bypass techniques. The tool fetches live CSP headers from target URLs using
  undici HTTP client and also accepts raw policy strings for offline analysis. It
  detects dangerous patterns including unsafe-inline, unsafe-eval, wildcard sources,
  data: URI allowlists, and overly broad domain patterns that enable XSS bypasses.
  For each finding, it provides a severity rating, exploit scenario description, and
  a recommended fix with the most restrictive policy that maintains functionality.
  The analyzer supports CSP Level 3 features including strict-dynamic, nonce-based
  policies, and hash-based script allowlisting. It generates report-only headers for
  gradual migration from permissive to strict policies and tracks violation reports
  from the report-uri or report-to endpoints.'
verification: security_reviewed
source: https://agentskillexchange.com/skills/csp-policy-analyzer/
category:
- Security &amp; Verification
framework:
- Claude Agents
---

# CSP Policy Analyzer

The CSP Policy Analyzer audits Content Security Policy headers for web applications to identify security weaknesses and generate hardened policy recommendations. It uses csp-parse to decompose complex CSP strings into structured directive objects and csp-evaluator (based on Google CSP Evaluator) to score each directive against known bypass techniques. The tool fetches live CSP headers from target URLs using undici HTTP client and also accepts raw policy strings for offline analysis. It detects dangerous patterns including unsafe-inline, unsafe-eval, wildcard sources, data: URI allowlists, and overly broad domain patterns that enable XSS bypasses. For each finding, it provides a severity rating, exploit scenario description, and a recommended fix with the most restrictive policy that maintains functionality. The analyzer supports CSP Level 3 features including strict-dynamic, nonce-based policies, and hash-based script allowlisting. It generates report-only headers for gradual migration from permissive to strict policies and tracks violation reports from the report-uri or report-to endpoints.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/csp-policy-analyzer/)
