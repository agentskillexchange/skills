---
name: "PM2 Node.js Production Process Manager with Load Balancing"
description: "PM2 is a production-grade process manager for Node.js and Bun applications with a built-in load balancer. With over 42,000 GitHub stars and millions of weekly npm downloads, it keeps applications alive forever, enables zero-downtime reloads, and provides comprehensive process monitoring with cluster mode support."
category: "Monitoring &amp; Alerts"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/Unitech/pm2"
tool_ecosystem:
  github_repo: "Unitech/pm2"
  github_stars: 43031
---
# PM2 Node.js Production Process Manager with Load Balancing

PM2 is a production-grade process manager for Node.js and Bun applications with a built-in load balancer. With over 42,000 GitHub stars and millions of weekly npm downloads, it keeps applications alive forever, enables zero-downtime reloads, and provides comprehensive process monitoring with cluster mode support.

PM2 is the industry-standard process manager for Node.js applications in production environments. It daemonizes applications, monitors their health, automatically restarts crashed processes, and provides a built-in load balancer through its cluster mode. PM2 works on Linux, macOS, and Windows, supporting all Node.js versions from 12.x onward and Bun since v1.

Cluster mode is PM2’s standout feature for production Node.js deployments. Running pm2 start app.js -i max launches one process per CPU core and automatically distributes incoming HTTP, TCP, and UDP connections across them. This can improve throughput by up to 10x on multi-core machines. Zero-downtime reloads (pm2 reload all) restart processes one at a time, ensuring the application never goes offline during deployments.

The process management CLI provides commands for starting, stopping, restarting, and deleting processes by name, ID, or namespace. pm2 monit opens a real-time terminal dashboard showing CPU usage, memory consumption, loop latency, and custom metrics for each process. pm2 logs streams application output with support for JSON and formatted output modes, and the pm2-logrotate module handles automatic log rotation.

PM2 integrates with system init systems (systemd, upstart, launchd) via pm2 startup to ensure processes survive server reboots. The pm2 save command persists the current process list for automatic restoration. For containerized deployments, the pm2-runtime drop-in replacement for node works seamlessly in Docker containers.

AI coding agents benefit from PM2 when deploying or managing Node.js services. Agents can use it to start background API servers, manage multiple microservices, monitor process health, and implement zero-downtime deployment strategies. The ecosystem configuration file (ecosystem.config.js) defines multi-app deployments declaratively.

Install globally via npm install pm2 -g. Documentation at pm2.keymetrics.io.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill pm2-nodejs-production-process-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill pm2-nodejs-production-process-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill pm2-nodejs-production-process-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill pm2-nodejs-production-process-manager -a codex
```

### OpenClaw

```bash
clawhub install pm2-nodejs-production-process-manager
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pm2-nodejs-production-process-manager/)
