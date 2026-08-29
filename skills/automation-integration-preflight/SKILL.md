---
name: "Automation Integration Preflight"
slug: "automation-integration-preflight"
description: "Assess a public HTTP(S) page before building browser automation, extraction, or an integration. Use this skill to collect bounded structural evidence, readiness signals, risk flags, acceptance tests, and remediation priorities without sending credentials or accessing private targets."
category: "Integrations & Connectors"
framework: "Codex"
verification: listed
source: "https://preflight.tinyopsstudio.com/openapi.json"
---

# Automation Integration Preflight

Automation Integration Preflight helps an agent decide whether one public web page is structurally ready for browser automation, data extraction, or an integration before implementation begins. It calls the documented TinyOps preflight API and returns bounded evidence about reachability, redirects, response type, latency, robots policy, forms, headings, structured data, integration links, security headers, and automation-readiness risks. Use the acceptance-pack route when the user needs a go or no-go recommendation, concrete acceptance tests, a contract inventory, or a prioritized remediation backlog. The service reads public server-rendered HTML only. It does not execute JavaScript, inspect authenticated sessions, submit forms, solve challenges, test vulnerabilities, or access private, loopback, link-local, credential-bearing, or reserved-network destinations.

## Installation

### OpenClaw

```bash
clawhub install tinyopsstudio/tinyops-automation-preflight
```

### Direct repo install for Codex, Claude Code, Cursor, or another Agent Skills runtime

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/automation-integration-preflight ~/.agent-skills/automation-integration-preflight
```

### Optional third-party installer

The `skills` npm package is maintained by Vercel Labs and other third parties. Pin the version if you choose to use it:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill automation-integration-preflight
```

## Choose the result

- Use `analyze` for a quick structural preflight and readiness score.
- Use `acceptance-pack` when the user needs an implementation decision, acceptance tests, contract inventory, or prioritized remediation plan.

## Request the evidence

Reject URLs containing embedded credentials. Never send secrets, cookies, authorization headers, form values, or personal data.

For a quick preflight:

```bash
curl -sS https://preflight.tinyopsstudio.com/analyze \
  -A 'TinyOps-Preflight-Skill/1.0' \
  -H 'Content-Type: application/json' \
  --data '{"url":"https://example.com"}'
```

For an implementation acceptance pack:

```bash
curl -sS https://preflight.tinyopsstudio.com/acceptance-pack \
  -A 'TinyOps-Preflight-Skill/1.0' \
  -H 'Content-Type: application/json' \
  --data '{"url":"https://example.com","objective":"Describe the intended automation"}'
```

Use an equivalent HTTP client when shell access is unavailable. Send a truthful, non-empty user agent. If the service rejects a destination or cannot fetch it safely, report that result and do not route around the restriction.

## Interpret the response

Lead with the implementation decision, then summarize only evidence that materially affects it:

- final public URL, HTTP status, content type, latency, and redirects;
- robots policy and automation restrictions;
- detected forms, structured data, integration links, and security headers;
- readiness score, grade, components, and risk flags;
- acceptance tests and remediation items when using the acceptance pack.

Distinguish observations from recommendations. Structural evidence does not prove that a third-party integration works.

## Boundaries

If server-rendered public evidence is insufficient, state what is missing and recommend the smallest lawful manual or authenticated test the user can perform in their own environment. See the [OpenAPI contract](https://preflight.tinyopsstudio.com/openapi.json) and [live proof page](https://tinyopsstudio.com/automation-preflight-api) for the current interface, limits, and production access options.
