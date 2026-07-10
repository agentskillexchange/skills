---
name: "Datadog Triage Playbook"
slug: "datadog-triage-playbook"
description: "Automates alert triage using the Datadog Monitors API v2 and Notebooks API. Correlates metrics with traces via the Datadog APM Trace Search API and generates RCA timelines from the Events Stream API."
github_stars: 791
verification: "security_reviewed"
source: "https://github.com/DataDog/dd-trace-js"
category: "Runbooks & Diagnostics"
framework: "MCP"
tool_ecosystem:
  github_repo: "datadog/dd-trace-js"
  github_stars: 791
  npm_package: "dd-trace"
  npm_weekly_downloads: 6596660
---

# Datadog Triage Playbook

Automates alert triage using the Datadog Monitors API v2 and Notebooks API. Correlates metrics with traces via the Datadog APM Trace Search API and generates RCA timelines from the Events Stream API.

## Installation

Use the upstream install or setup path that matches your environment:
- $ npm install dd-trace
- $ yarn add dd-trace
- $ npm install dd-trace@4 # or whatever version you need
- $ yarn add dd-trace@4 # or whatever version you need

Requirements and caveats from upstream:
- # dd-trace: Node.js APM Tracer Library
- dd-trace is an npm package that you can install in your Node.js application to capture APM (Application Performance Monitoring) data. In Datadog terminology this library is called a Tracer. This data is then sent off...
- [Tracing Node.js Applications](https://docs.datadoghq.com/tracing/languages/nodejs/) - most project documentation, including setup instructions

Basic usage or getting-started notes:
- [API Documentation](https://datadog.github.io/dd-trace-js) - method signatures, plugin list, and some usage examples

- Source: https://github.com/DataDog/dd-trace-js
- Extracted from upstream docs: https://raw.githubusercontent.com/DataDog/dd-trace-js/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/datadog-triage-playbook/)
