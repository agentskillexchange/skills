---
name: "Trellis WordPress LEMP Stack Provisioner by Roots"
description: "Trellis is a collection of Ansible playbooks for provisioning and deploying WordPress LEMP stack servers. It automates Nginx, PHP, MariaDB, Let’s Encrypt SSL, fail2ban, and zero-downtime deploys across development, staging, and production environments."
category: "WordPress &amp; CMS"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/roots/trellis"
tool_ecosystem:
  github_repo: "roots/trellis"
  github_stars: 2560
  license: "MIT"
---
# Trellis WordPress LEMP Stack Provisioner by Roots

Trellis is a collection of Ansible playbooks for provisioning and deploying WordPress LEMP stack servers. It automates Nginx, PHP, MariaDB, Let’s Encrypt SSL, fail2ban, and zero-downtime deploys across development, staging, and production environments.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill trellis-wordpress-lemp-ansible-provisioner-roots
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill trellis-wordpress-lemp-ansible-provisioner-roots -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill trellis-wordpress-lemp-ansible-provisioner-roots -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill trellis-wordpress-lemp-ansible-provisioner-roots -a codex
```

### OpenClaw

```bash
clawhub install trellis-wordpress-lemp-ansible-provisioner-roots
```

## Details

Trellis is an open-source server provisioning and deployment tool for WordPress built by the Roots team. It uses Ansible playbooks to automate the complete setup of a LEMP (Linux, Nginx, MariaDB, PHP) stack optimized specifically for WordPress hosting, including automated Let’s Encrypt SSL certificates, fail2ban intrusion prevention, and zero-downtime deployments.

The tool provides two main Ansible playbooks: server.yml for initial server provisioning and deploy.yml for deploying WordPress sites. Server provisioning installs and configures Nginx with optimized WordPress rules, PHP-FPM with appropriate settings, MariaDB for the database layer, and additional components like WP-CLI, Composer, and security hardening. The deploy playbook handles git-based deployments with atomic symlink swaps for zero downtime.

Configuration is managed through YAML files organized by environment. The group_vars directory contains settings for development, staging, and production, each defining WordPress sites with their domains, database credentials, SSL settings, and deployment repositories. Sensitive data like passwords and API keys are encrypted using Ansible Vault, keeping secrets safe in version control.

Trellis supports multiple WordPress sites on a single server, each with its own Nginx configuration, database, and deployment pipeline. It integrates directly with Bedrock-based WordPress projects, automatically handling Composer installs, shared directories for uploads, and environment variable injection during deployment.

Development environments use Vagrant for local VMs that mirror production configuration exactly. The trellis-cli companion tool provides commands for initializing projects, managing vaults, and running deployments. Licensed under MIT with over 2,500 GitHub stars and comprehensive documentation at roots.io/trellis/docs.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/trellis-wordpress-lemp-ansible-provisioner-roots/)
