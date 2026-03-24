---
name: "DigitalOcean Droplet Manager"
description: "Create, configure, and manage DigitalOcean Droplets, Kubernetes clusters, and managed databases through the doctl CLI and DigitalOcean API. Supports automated Droplet provisioning with cloud-init scripts and firewall rule management."
category: "Templates & Workflows"
framework: "Custom Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/digitalocean-droplet-manager/"
tool_ecosystem:  # ONLY if real signals exist in meta
  tool: "kubernetes"  # from ase_tool_match
  github_stars: 121313  # from ase_github_stars (integer, not string)
  github_repo: "kubernetes/kubernetes"  # from ase_github_repo
  license: "Apache-2.0"  # from ase_tool_license
  maintained: true  # from ase_tool_maintained
---

# DigitalOcean Droplet Manager

Create, configure, and manage DigitalOcean Droplets, Kubernetes clusters, and managed databases through the doctl CLI and DigitalOcean API. Supports automated Droplet provisioning with cloud-init scripts and firewall rule management.

## Overview

Create, configure, and manage DigitalOcean Droplets, Kubernetes clusters, and managed databases through the doctl CLI and DigitalOcean API. Supports automated Droplet provisioning with cloud-init scripts and firewall rule management.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill digitalocean-droplet-manager
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill digitalocean-droplet-manager -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill digitalocean-droplet-manager -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill digitalocean-droplet-manager -a codex
```

### OpenClaw

```bash
clawhub install digitalocean-droplet-manager
```

## Source

- Marketplace: https://agentskillexchange.com/skills/digitalocean-droplet-manager/
