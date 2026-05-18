---
name: "Traefik Cloud-Native Application Proxy and Reverse Proxy"
slug: "traefik-cloud-native-reverse-proxy"
description: "Traefik is a modern cloud-native reverse proxy and load balancer that automatically discovers services and configures routing. It integrates natively with Docker, Kubernetes, and Let's Encrypt for automatic HTTPS."
github_stars: 62473
verification: "security_reviewed"
source: "https://github.com/traefik/traefik"
category: "Developer Tools"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "traefik/traefik"
  github_stars: 62473
---

# Traefik Cloud-Native Application Proxy and Reverse Proxy

Traefik is a modern cloud-native reverse proxy and load balancer that automatically discovers services and configures routing. It integrates natively with Docker, Kubernetes, and Let's Encrypt for automatic HTTPS.

## Installation

Use the upstream install or setup path that matches your environment:
- docker run -d -p 8080:8080 -p 80:80 -v $PWD/traefik.toml:/etc/traefik/traefik.toml traefik
- git clone https://github.com/traefik/traefik

Requirements and caveats from upstream:
- Traefik integrates with your existing infrastructure components ([Docker](https://www.docker.com/), [Swarm mode](https://docs.docker.com/engine/swarm/), [Kubernetes](https://kubernetes.io), [Consul](https://www.consul...
- Traditional reverse-proxies require that you configure _each_ route that will connect paths and subdomains to _each_ microservice.
- Packaged as a single binary file (made with :heart: with go) and available as an [official](https://hub.docker.com/r/_/traefik/) docker image

Basic usage or getting-started notes:
- **Run Traefik and let it do the work for you!**
- ## Web UI
- You can access the simple HTML frontend of Traefik.

- Source: https://github.com/traefik/traefik
- Extracted from upstream docs: https://raw.githubusercontent.com/traefik/traefik/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/traefik-cloud-native-reverse-proxy/)
