---
name: "piku Tiny PaaS for Git Push Deployments to Your Own Servers"
description: "piku is a minimal Heroku-like PaaS that enables git push deployments to any server, from Raspberry Pis to cloud VPSes. It supports Python, Node.js, Go, Java, Ruby, and Clojure runtimes with automatic dependency installation, Procfile-based process management via uwsgi, nginx virtual hosts, and Let's Encrypt SSL."
category: "Developer Tools"
framework: "Custom Agents"
verification: listed
source: "https://github.com/piku/piku"
tool_ecosystem:
  tool: piku
  github_repo: piku/piku
  github_stars: 6568
  license: MIT
  maintained: true
---
# piku Tiny PaaS for Git Push Deployments to Your Own Servers

piku is a minimal Heroku-like PaaS that enables git push deployments to any server, from Raspberry Pis to cloud VPSes. It supports Python, Node.js, Go, Java, Ruby, and Clojure runtimes with automatic dependency installation, Procfile-based process management via uwsgi, nginx virtual hosts, and Let's Encrypt SSL.

## Overview

piku is a self-hosted Platform-as-a-Service inspired by Dokku and Heroku that allows developers to deploy applications to their own servers using simple git push commands. Originally built to run on a 256MB Raspberry Pi, it scales from tiny ARM boards to full cloud servers, making it one of the most lightweight deployment platforms available.

How It Works
Set up a git remote pointing to your piku server (git remote add piku piku@yourserver:appname), then push your code (git push piku master). piku automatically detects the runtime, installs dependencies, reads the Procfile, and starts your application using uwsgi as the process manager. nginx handles reverse proxying with automatic virtual host configuration.

Supported Runtimes
piku supports Python (with virtualenv isolation), Node.js (npm/yarn), Go (separate GOPATH per app), Java (Maven or Gradle), Clojure (Leiningen or deps.edn), and Ruby (Bundler). Static sites are supported via a static worker type. Each runtime gets proper dependency isolation and build steps.

Features
Key features include multiple apps per host with independent scaling (ps:scale), environment variable management (config:set), release tasks that run on deploy, full virtual host support for multiple domains on one server, automatic SSL via Let's Encrypt, static asset serving with URL prefix mapping, response caching, and Avahi/mDNS support for LAN discovery.

Installation
Install with one command: curl https://piku.github.io/get | sh. Alternative methods include cloud-init for automated server provisioning and manual installation. piku requires Python 3.8+, nginx, uwsgi, and SSH access on the target server.

Use Cases
piku is ideal for deploying side projects, internal tools, staging environments, and production apps on budget hardware or cloud VPSes. It works on any POSIX system including Linux, FreeBSD, Cygwin, and WSL, supporting both Intel and ARM architectures.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill piku-tiny-paas-git-push-deployments-own-servers
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill piku-tiny-paas-git-push-deployments-own-servers -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill piku-tiny-paas-git-push-deployments-own-servers -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill piku-tiny-paas-git-push-deployments-own-servers -a codex
```

### OpenClaw

```bash
clawhub install piku-tiny-paas-git-push-deployments-own-servers
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/piku-tiny-paas-git-push-deployments-own-servers/)
