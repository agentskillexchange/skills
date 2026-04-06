---
name: Logdy Real-Time Log Viewer with Web UI and CLI
description: Logdy is a zero-dependency single-binary log viewer that pipes any command
  output into an interactive browser-based UI. It supports custom TypeScript parsers,
  column definitions, filtering, and works with stdin, files, sockets, and REST API
  inputs.
category: "Monitoring &amp; Alerts"
framework: Multi-Framework
verification: security_reviewed
source: "https://github.com/logdyhq/logdy-core"
---
# Logdy Real-Time Log Viewer with Web UI and CLI

Logdy is a zero-dependency single-binary log viewer that pipes any command output into an interactive browser-based UI. It supports custom TypeScript parsers, column definitions, filtering, and works with stdin, files, sockets, and REST API inputs.

Logdy is a lightweight, single-binary log viewer written in Go that transforms any terminal log output into a structured, filterable web interface. It works like a visual layer on top of grep, awk, or tail, providing real-time log parsing and exploration through an embedded browser UI without requiring any external dependencies or deployment infrastructure.

How It Works

Logdy sits between your log source and the browser. Pipe any command output into Logdy (tail -f app.log | logdy) and it starts a local web server at port 8080. The embedded UI renders incoming log lines in real time with syntax highlighting, filtering, and search capabilities. It also supports reading files directly with logdy follow app.log --full-read, accepting data over sockets, and receiving logs via its REST API.

Custom Parsers and Columns

Logdy includes a built-in TypeScript editor where you can define custom parsers to extract structured fields from unstructured log lines. Parsed fields become sortable, filterable table columns in the UI. This makes it possible to turn JSON logs, Apache access logs, or any structured text into a queryable table without any configuration files or schema definitions.

Go Library Integration

Beyond the CLI, Logdy can be embedded directly into Go applications as a library. Import github.com/logdyhq/logdy-core/logdy, initialize with a config, and call logdyLogger.Log() to send structured log entries to the web UI from within your application code. This provides a zero-setup debugging dashboard for Go services during development.

Agent Integration Points

Agents can use Logdy to monitor application logs during deployment verification, debug failing services by piping their output through Logdy for structured analysis, or embed it into diagnostic runbooks that need interactive log exploration. The single-binary distribution (available via curl installer, Homebrew, or direct download) makes it easy to provision on any target machine. The CLI flags support headless operation with JSON output for programmatic log processing pipelines.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill logdy-realtime-log-viewer-web-ui-cli
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill logdy-realtime-log-viewer-web-ui-cli -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill logdy-realtime-log-viewer-web-ui-cli -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill logdy-realtime-log-viewer-web-ui-cli -a codex
```

### OpenClaw

```bash
clawhub install logdy-realtime-log-viewer-web-ui-cli
```


## Source

- [GitHub](https://github.com/logdyhq/logdy-core)
