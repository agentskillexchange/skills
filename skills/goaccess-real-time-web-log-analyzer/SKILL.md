---
name: "GoAccess Real-Time Web Log Analyzer and Terminal Dashboard"
description: "GoAccess is an open-source real-time web log analyzer that runs in a terminal or generates live HTML dashboards. It parses Apache, Nginx, CloudFront, S3, and other log formats with minimal configuration, providing instant traffic insights for system administrators and DevOps engineers."
category: "Monitoring & Alerts"
framework: "Custom Agents"
verification: security_reviewed
source: "https://github.com/allinurl/goaccess"
tool_ecosystem:
  tool: docker
  github_repo: allinurl/goaccess
  github_stars: 20377
---
# GoAccess Real-Time Web Log Analyzer and Terminal Dashboard

GoAccess is an open-source real-time web log analyzer that runs in a terminal or generates live HTML dashboards. It parses Apache, Nginx, CloudFront, S3, and other log formats with minimal configuration, providing instant traffic insights for system administrators and DevOps engineers.

## Overview

What is GoAccess?

GoAccess is an open-source, real-time web log analyzer and interactive viewer that runs in a terminal on Unix systems or directly in your browser via live HTML reports. With over 20,000 stars on GitHub, it is designed for system administrators, DevOps engineers, and security professionals who need fast, actionable HTTP statistics without complex setup. Written in C with only ncurses as a dependency, it delivers exceptional performance even on large datasets.

Real-Time Analysis

All panels and metrics update every 200 milliseconds in the terminal and every second on HTML output. GoAccess can monitor live access logs by piping them directly, showing visitor counts, bandwidth usage, status codes, referring sites, requested files, geographic data, and more in real time. This makes it ideal for monitoring production servers during deployments or investigating traffic spikes as they happen.

Log Format Support

GoAccess supports nearly every web log format out of the box. Predefined configurations include Apache Combined/Common, Nginx, Amazon CloudFront, Amazon S3, AWS Elastic Load Balancing, Google Cloud Storage, Squid, W3C (IIS), Caddy JSON, and Traefik. Custom log format strings are also supported for non-standard configurations.

Security Monitoring

Beyond traffic analysis, GoAccess serves as a practical security monitoring tool. It can detect suspicious activity, unusual traffic patterns, brute-force attempts, scanners, bots, and anomalous requests directly from logs. The ASN (Autonomous System Number) mapping feature helps identify and block malicious traffic patterns by their originating networks.

Output Formats and Integration

GoAccess produces three output formats: an interactive terminal TUI, a self-contained real-time HTML dashboard with WebSocket updates, JSON reports, and CSV exports. The HTML dashboard includes WebSocket authentication supporting JWT verification for secure remote access. Incremental log processing with on-disk persistence enables data continuity across restarts.

Deployment Options

GoAccess can be installed from source, via package managers (apt, brew, pacman), or run as a Docker container. The Docker setup supports volume mapping for configuration and integrates with docker-compose for orchestrated deployments. It pairs well with existing monitoring stacks and can complement tools like Prometheus and Grafana for web-specific log analysis.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill goaccess-real-time-web-log-analyzer
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill goaccess-real-time-web-log-analyzer -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill goaccess-real-time-web-log-analyzer -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill goaccess-real-time-web-log-analyzer -a codex
```

### OpenClaw

```bash
clawhub install goaccess-real-time-web-log-analyzer
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/goaccess-real-time-web-log-analyzer/)
