---
title: "Nginx Error Log Pattern Analyzer"
description: "Parses Nginx error logs using configurable regex patterns and the GoAccess real-time log analyzer API. Clusters recurring 502/504 errors and correlates with upstream health check failures."
verification: security_reviewed
source: "https://github.com/nginx/nginx"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "nginx/nginx"
  github_stars: 29930
---

# Nginx Error Log Pattern Analyzer

The Nginx Error Log Pattern Analyzer processes Nginx error log files using configurable regex patterns to extract structured data from error entries. It integrates with the GoAccess real-time web log analyzer API for live dashboard generation and historical trend analysis. The skill clusters recurring error patterns, with special focus on 502 Bad Gateway and 504 Gateway Timeout errors, correlating them with upstream server health check failures and connection timeouts. It parses upstream response times from access logs to identify degrading backend services before they trigger errors. The analyzer supports log rotation detection, compressed log file reading (.gz), and multi-server log aggregation via rsyslog or Filebeat inputs. Output includes frequency heatmaps by hour, top offending upstreams, client IP analysis for potential abuse patterns, and recommended Nginx configuration tuning parameters for proxy_read_timeout, proxy_connect_timeout, and keepalive settings.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/nginx-error-log-pattern-analyzer/)
