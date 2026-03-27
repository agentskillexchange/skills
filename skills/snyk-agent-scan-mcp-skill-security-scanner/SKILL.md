---
name: "Snyk Agent Scan MCP and Skill Security Scanner"
description: "Snyk Agent Scan automatically discovers and scans AI agent components including MCP servers, agent skills, and agent harnesses for security vulnerabilities like prompt injections, tool poisoning, t..."
category: "Security & Verification"
framework: "MCP"
verification: "listed"
source: "https://agentskillexchange.com/skills/snyk-agent-scan-mcp-skill-security-scanner/"
---

# Snyk Agent Scan MCP and Skill Security Scanner

Snyk Agent Scan automatically discovers and scans AI agent components including MCP servers, agent skills, and agent harnesses for security vulnerabilities like prompt injections, tool poisoning, tool shadowing, and malware payloads. It supports Claude Code, Cursor, Windsurf, Gemini CLI, VS Code, and more.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill snyk-agent-scan-mcp-skill-security-scanner
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill snyk-agent-scan-mcp-skill-security-scanner -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill snyk-agent-scan-mcp-skill-security-scanner -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill snyk-agent-scan-mcp-skill-security-scanner -a codex
```

### OpenClaw

```bash
clawhub install snyk-agent-scan-mcp-skill-security-scanner
```
