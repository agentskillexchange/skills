---
title: "Ansible Playbook Diagnostics Runner"
description: "Runs Ansible diagnostic playbooks using ansible-runner and the Ansible Collections ecosystem (ansible.builtin, community.general). Captures system health, service status, and log analysis across inventory hosts."
verification: security_reviewed
source: "https://github.com/ansible/ansible"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Gemini"
tool_ecosystem:
  github_repo: "ansible/ansible"
  github_stars: 68364
---

# Ansible Playbook Diagnostics Runner

The Ansible Playbook Diagnostics Runner skill executes diagnostic playbooks using ansible-runner (ansible_runner.run()) and the Ansible automation framework. It leverages modules from ansible.builtin (command, shell, copy, template, service, systemd) and community.general (ufw, nmcli, sysctl, modprobe) collections to perform comprehensive system diagnostics.

The skill manages inventory through dynamic inventory plugins (aws_ec2, azure_rm, gcp_compute) and static YAML/INI inventory files. It executes health check playbooks that gather facts using ansible.builtin.setup, check service status with ansible.builtin.systemd, analyze disk usage via ansible.builtin.command (df, du), and collect log entries using ansible.builtin.shell with journalctl queries.

Advanced capabilities include role-based diagnostic suites organized as Ansible roles with tasks/handlers/defaults/vars, callback plugin integration for custom output formatting (json, yaml, timer), vault-encrypted variable management for sensitive credentials, and async task execution for long-running diagnostics with poll intervals. The runner also supports check mode (–check) for dry-run validation, diff mode (–diff) for configuration drift detection, and custom filter plugins for log parsing and metric extraction.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-diagnostics-runner/)
