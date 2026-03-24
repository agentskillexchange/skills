---
name: "CSP Policy Analyzer"
description: "Parses and evaluates Content Security Policy headers using csp-parse and csp-evaluator libraries. Identifies overly permissive directives, missing protections, and generates tightened policy recommendations."
category: "Security & Verification"
framework: "Claude Agents"
verification: security_reviewed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/csp-policy-analyzer/"
---

# CSP Policy Analyzer

Parses and evaluates Content Security Policy headers using csp-parse and csp-evaluator libraries. Identifies overly permissive directives, missing protections, and generates tightened policy recommendations.

## Overview

The CSP Policy Analyzer audits Content Security Policy headers for web applications to identify security weaknesses and generate hardened policy recommendations. It uses csp-parse to decompose complex CSP strings into structured directive objects and csp-evaluator (based on Google CSP Evaluator) to score each directive against known bypass techniques. The tool fetches live CSP headers from target URLs using undici HTTP client and also accepts raw policy strings for offline analysis. It detects dangerous patterns including unsafe-inline, unsafe-eval, wildcard sources, data: URI allowlists, and overly broad domain patterns that enable XSS bypasses. For each finding, it provides a severity rating, exploit scenario description, and a recommended fix with the most restrictive policy that maintains functionality. The analyzer supports CSP Level 3 features including strict-dynamic, nonce-based policies, and hash-based script allowlisting. It generates report-only headers for gradual migration from permissive to strict policies and tracks violation reports from the report-uri or report-to endpoints.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill csp-policy-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill csp-policy-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill csp-policy-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill csp-policy-analyzer -a codex
```

### OpenClaw

```bash
clawhub install csp-policy-analyzer
```

## Source

- Marketplace: https://agentskillexchange.com/skills/csp-policy-analyzer/
