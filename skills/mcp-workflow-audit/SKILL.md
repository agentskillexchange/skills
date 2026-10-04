---
name: "MCP Workflow Audit"
slug: "mcp-workflow-audit"
description: "Audit Claude Code, MCP, and AI-agent workflows for permissions, consequential actions, idempotency, failure recovery, verification, and operator handoff."
category: "Developer Tools"
framework: "Claude Code"
verification: listed
source: "https://github.com/OssaBellator/claude-mcp-workflow-audit"
---

# MCP Workflow Audit

MCP Workflow Audit is a read-first operational audit workflow for Claude Code, Model Context Protocol integrations, and AI-agent automations. Use it when an agent workspace works inconsistently, has accumulated MCP configuration, performs consequential external writes, or needs a maintainable handoff before further automation is added. The workflow inventories instructions, MCP configuration, Skills, hooks, scheduled automation, package metadata, and credential boundaries; maps external writes and approval points; and reviews least privilege, bounded retries, idempotency, missing or conflicting data, partial-failure recovery, and post-action verification. It explicitly treats scanner findings as heuristics rather than proof, avoids destructive testing, and does not broaden permissions merely to make a workflow pass. The upstream MIT-licensed repository also provides a dependency-free static scanner, regression tests, workflow contracts, and synthetic appointment, trades-operations, and retail-pricing references.

## Installation

### Skills CLI

```bash
npm exec --package=skills@1.5.7 -- skills add OssaBellator/claude-mcp-workflow-audit --skill auditing-mcp-workflows
```

### Claude Code plugin

```text
/plugin marketplace add OssaBellator/claude-mcp-workflow-audit
/plugin install mcp-workflow-audit@ossabellator-claude-tools
```

### Direct repository

```bash
git clone https://github.com/OssaBellator/claude-mcp-workflow-audit.git
```

Review the Skill and scripts before installation. The audit methodology is read-first, and the public business examples are synthetic/open-source methodology rather than claims of customer deployments.
