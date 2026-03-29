---
name: "VS Code Extension Debugger"
description: "Debugs VS Code extensions using the Debug Adapter Protocol (DAP) with breakpoint management and variable inspection. Integrates with VS Code Extension API for webview debugging and uses Chrome DevTools Protocol for renderer process analysis."
category: "Developer Tools"
framework: "Claude Code"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/vscode-extension-debugger-dap-protocol/"
---
# VS Code Extension Debugger

Debugs VS Code extensions using the Debug Adapter Protocol (DAP) with breakpoint management and variable inspection. Integrates with VS Code Extension API for webview debugging and uses Chrome DevTools Protocol for renderer process analysis.

## Overview

Debugs VS Code extensions using the Debug Adapter Protocol (DAP) with breakpoint management and variable inspection. Integrates with VS Code Extension API for webview debugging and uses Chrome DevTools Protocol for renderer process analysis.

This skill provides a comprehensive automation layer for developers and teams who need reliable, repeatable workflows. It handles authentication, rate limiting, and error recovery automatically, so you can focus on the logic that matters. The agent monitors for changes in real time and applies incremental updates to minimize API calls and reduce latency. Configuration is handled through a simple YAML manifest that defines inputs, outputs, and trigger conditions. Built-in logging captures every action for audit trails and debugging. Supports both interactive and headless modes, making it suitable for CI/CD pipelines as well as local development. The skill includes pre-built templates for common use cases and can be extended with custom plugins. Error handling follows exponential backoff with jitter for transient failures and provides clear diagnostic messages for permanent errors. Compatible with major operating systems and containerized environments. Tested against production workloads with comprehensive integration test suites.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill vscode-extension-debugger-dap-protocol
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill vscode-extension-debugger-dap-protocol -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill vscode-extension-debugger-dap-protocol -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill vscode-extension-debugger-dap-protocol -a codex
```

### OpenClaw

```bash
clawhub install vscode-extension-debugger-dap-protocol
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/vscode-extension-debugger-dap-protocol/)
