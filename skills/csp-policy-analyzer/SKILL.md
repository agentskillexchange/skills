---
title: "CSP Policy Analyzer"
description: "Parses and evaluates Content Security Policy headers using csp-parse and csp-evaluator libraries. Identifies overly permissive directives, missing protections, and generates tightened policy recommendations."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/csp-policy-analyzer/"
category:
  - "Security &amp; Verification"
framework:
  - "Claude Agents"
---

# CSP Policy Analyzer

The CSP Policy Analyzer audits Content Security Policy headers for web applications to identify security weaknesses and generate hardened policy recommendations. It uses csp-parse to decompose complex CSP strings into structured directive objects and csp-evaluator (based on Google CSP Evaluator) to score each directive against known bypass techniques. The tool fetches live CSP headers from target URLs using undici HTTP client and also accepts raw policy strings for offline analysis. It detects dangerous patterns including unsafe-inline, unsafe-eval, wildcard sources, data: URI allowlists, and overly broad domain patterns that enable XSS bypasses. For each finding, it provides a severity rating, exploit scenario description, and a recommended fix with the most restrictive policy that maintains functionality. The analyzer supports CSP Level 3 features including strict-dynamic, nonce-based policies, and hash-based script allowlisting. It generates report-only headers for gradual migration from permissive to strict policies and tracks violation reports from the report-uri or report-to endpoints.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/csp-policy-analyzer/)
