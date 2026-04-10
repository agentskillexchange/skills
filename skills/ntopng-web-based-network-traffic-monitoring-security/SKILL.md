---
name: "ntopng Web-Based Network Traffic Monitoring and Security Analysis"
description: "ntopng is a web-based network traffic monitoring application that provides real-time visibility into network flows, bandwidth usage, and security threats. With 7.7k+ GitHub stars and decades of development since the original ntop in 1998, it is a proven enterprise-grade network analysis platform."
verification: security_reviewed
source: "https://github.com/ntop/ntopng"
category:
  - "Monitoring &amp; Alerts"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "ntop/ntopng"
  github_stars: 7702
---

# ntopng Web-Based Network Traffic Monitoring and Security Analysis

Overview
ntopng is a high-performance, web-based network traffic monitoring application released under GPLv3 by ntop. It is the modern incarnation of the original ntop project first written in 1998, completely revamped for contemporary network environments. ntopng provides deep packet inspection, flow analysis, and security monitoring through an intuitive web dashboard, REST API, and alerting system.
Key Features

Real-time traffic analysis: Monitor network flows, protocols, and bandwidth usage with sub-second granularity across all network interfaces
Deep Packet Inspection: Uses the nDPI library (also by ntop) to classify network traffic by application protocol, detecting over 300 protocols including encrypted traffic
Security monitoring: Detect anomalies, suspicious behaviors, lateral movement, DNS tunneling, and other network-based threats in real time
Web dashboard: Rich HTML5 web interface with interactive charts, flow tables, host profiles, and customizable dashboards
REST API: Comprehensive REST API for programmatic access to all monitoring data, enabling integration with external tools and automation workflows
Flow export: Export flow data in NetFlow v5/v9, IPFIX, and sFlow formats for long-term storage and analysis
Alerting system: Configurable alerts for bandwidth thresholds, security events, and anomaly detection with webhook, email, and Slack notification support
Multi-platform: Runs on Debian/Ubuntu, CentOS/RHEL, Windows, Raspberry Pi, FreeBSD, OPNsense, and pfSense

Agent Integration
AI agents can leverage ntopng's REST API to build network intelligence and security monitoring workflows. The API exposes host data, flow information, alert streams, and historical statistics that agents can query to diagnose network issues, detect security incidents, and generate network health reports. Agents can automate responses to ntopng alerts by integrating with firewall APIs, ticketing systems, or incident response platforms. The JSON-based API is straightforward for agents to consume and reason about.
Installation
# Ubuntu/Debian
apt-get install software-properties-common wget
add-apt-repository universe
wget https://packages.ntop.org/apt-stable/bookworm/all/apt-ntop-stable.deb
apt install ./apt-ntop-stable.deb
apt-get update
apt-get install ntopng

# Start service
systemctl start ntopng
Technical Details
ntopng is written in C++ with Lua scripting for extensibility and runs as a daemon that captures packets from network interfaces or receives flows from routers and switches. It uses Redis for caching and InfluxDB or ClickHouse for time-series storage. The web interface is served via an embedded HTTP server on port 3000 by default. ntopng integrates with the ntop ecosystem including nProbe (NetFlow/sFlow collector), PF_RING (high-speed packet capture), and nDPI (deep packet inspection library).

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ntopng-web-based-network-traffic-monitoring-security/)
