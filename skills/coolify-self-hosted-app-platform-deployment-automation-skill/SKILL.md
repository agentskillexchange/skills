---
name: Coolify Self-Hosted App Platform and Deployment Automation Skill
description: Coolify is an open source self-hosted deployment platform for applications,
  databases, and services. This skill covers installing Coolify, connecting infrastructure
  over SSH, and using it as an operational control plane for repeatable app delivery
  workflows.
category: Developer Tools
framework: Multi-Framework
verification: listed
source: "https://github.com/coollabsio/coolify"
---
# Coolify Self-Hosted App Platform and Deployment Automation Skill

Coolify is an open source self-hosted deployment platform for applications, databases, and services. This skill covers installing Coolify, connecting infrastructure over SSH, and using it as an operational control plane for repeatable app delivery workflows.

Coolify is a large, actively maintained open source platform from CoolLabs for self-hosted application deployment. It provides a control plane for deploying apps, databases, static sites, and supporting services onto your own servers through a web interface and automation-friendly operational model. The upstream project has substantial adoption, detailed documentation, and a quick-install path that makes it relevant for real deployment workflows rather than hypothetical experiments.

The practical job to be done is clear: install Coolify on a supported Linux host, connect target infrastructure over SSH, and use it to standardize deployments, environment management, and service lifecycle operations. That makes it useful for teams that want a Heroku-style or PaaS-like experience on their own infrastructure. In an agent context, Coolify can be used as the documented platform behind runbooks for shipping apps, rotating services, or managing supporting databases and containers with less manual shell work.

Technically, the important integration points are SSH-based server access, Docker-backed runtime management, and the installation script published in the official docs. This skill belongs in developer tools because it gives operators a repeatable deployment interface for application delivery, infra hygiene, and service orchestration on self-managed systems.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill coolify-self-hosted-app-platform-deployment-automation-skill
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill coolify-self-hosted-app-platform-deployment-automation-skill -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill coolify-self-hosted-app-platform-deployment-automation-skill -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill coolify-self-hosted-app-platform-deployment-automation-skill -a codex
```

### OpenClaw

```bash
clawhub install coolify-self-hosted-app-platform-deployment-automation-skill
```


## Source

- [GitHub](https://github.com/coollabsio/coolify)
