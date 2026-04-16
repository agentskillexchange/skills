---
title: "Traefik Cloud-Native Application Proxy and Reverse Proxy"
description: "Traefik is a modern cloud-native reverse proxy and load balancer that automatically discovers services and configures routing. It integrates natively with Docker, Kubernetes, and Let’s Encrypt for automatic HTTPS."
verification: "security_reviewed"
source: "https://github.com/traefik/traefik"
category:
  - "Developer Tools"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "traefik/traefik"
  github_stars: 62473
---

# Traefik Cloud-Native Application Proxy and Reverse Proxy

Overview
Traefik (pronounced “traffic”) is an open-source edge router and reverse proxy designed for cloud-native environments. Unlike traditional reverse proxies that require manual configuration files, Traefik automatically discovers services from orchestrators like Docker, Kubernetes, Marathon, Consul, and etcd, then dynamically generates routing configuration. With over 62,000 GitHub stars, it is one of the most widely adopted infrastructure tools in the container ecosystem.


Core Capabilities
Traefik provides automatic service discovery by connecting to infrastructure components and reading their metadata to generate routing rules in real time. It handles automatic HTTPS certificate management via Let’s Encrypt with ACME protocol support, including DNS challenge providers. The proxy supports HTTP/2, gRPC, WebSocket, and TCP/UDP routing. Built-in middleware provides functionality for rate limiting, circuit breaking, authentication, header manipulation, and request buffering.


Agent Integration Points
AI agents managing infrastructure can interact with Traefik through its REST API at /api to inspect routers, services, and middleware configurations. The traefik CLI provides commands for healthcheck and configuration validation. Agents deploying containerized applications can configure routing by adding Docker labels or Kubernetes IngressRoute CRDs, making Traefik a zero-touch routing layer for automated deployment workflows. The dashboard API provides JSON-formatted metrics and configuration data ideal for automated monitoring.


Key Features

Automatic service discovery from Docker, Kubernetes, Consul, etcd
Let’s Encrypt HTTPS with automatic certificate renewal
HTTP/2, gRPC, WebSocket, TCP, and UDP routing
Built-in middleware: rate limiting, circuit breakers, auth, headers
Canary deployments and traffic mirroring
Observability: Prometheus metrics, OpenTelemetry tracing, access logs
Dashboard with real-time service and route visualization

Installation
# Docker
docker run -d -p 80:80 -p 8080:8080 traefik:v3.6 --api.insecure=true --providers.docker

# Binary
wget https://github.com/traefik/traefik/releases/download/v3.6.12/traefik_v3.6.12_linux_amd64.tar.gz
tar xzf traefik_v3.6.12_linux_amd64.tar.gz
Configuration
Traefik uses a two-level configuration system: static configuration (entrypoints, providers) defined in traefik.yml or CLI flags, and dynamic configuration (routers, services, middleware) discovered automatically from providers or defined in file providers. Configuration can also be set entirely through environment variables.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/traefik-cloud-native-reverse-proxy/)
