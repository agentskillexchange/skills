---
title: Ansible Playbook Diagnostics Runner
description: The Ansible Playbook Diagnostics Runner skill executes diagnostic playbooks
  using ansible-runner (ansible_runner.run()) and the Ansible automation framework.
  It leverages modules from ansible.builtin (command, shell, copy, template, service,
  systemd) and community.general (ufw, nmcli, sysctl, modprobe) collections to perform
  comprehensive system diagnostics. The skill manages inventory through dynamic inventory
  plugins (aws_ec2, azure_rm, gcp_compute) and static YAML/INI inventory files. It
  executes health check playbooks that gather facts using ansible.builtin.setup, check
  service status with ansible.builtin.systemd, analyze disk usage via ansible.builtin.command
  (df, du), and collect log entries using ansible.builtin.shell with journalctl queries.
  Advanced capabilities include role-based diagnostic suites organized as Ansible
  roles with tasks/handlers/defaults/vars, callback plugin integration for custom
  output formatting (json, yaml, timer), vault-encrypted variable management for sensitive
  credentials, and async task execution for long-running diagnostics with poll intervals.
  The runner also supports check mode (–check) for dry-run validation, diff mode (–diff)
  for configuration drift detection, and custom filter plugins for log parsing and
  metric extraction.
verification: security_reviewed
source: https://agentskillexchange.com/skills/ansible-playbook-diagnostics-runner/
category:
- Runbooks &amp; Diagnostics
framework:
- Gemini
---

# Ansible Playbook Diagnostics Runner

The Ansible Playbook Diagnostics Runner skill executes diagnostic playbooks using ansible-runner (ansible_runner.run()) and the Ansible automation framework. It leverages modules from ansible.builtin (command, shell, copy, template, service, systemd) and community.general (ufw, nmcli, sysctl, modprobe) collections to perform comprehensive system diagnostics. The skill manages inventory through dynamic inventory plugins (aws_ec2, azure_rm, gcp_compute) and static YAML/INI inventory files. It executes health check playbooks that gather facts using ansible.builtin.setup, check service status with ansible.builtin.systemd, analyze disk usage via ansible.builtin.command (df, du), and collect log entries using ansible.builtin.shell with journalctl queries. Advanced capabilities include role-based diagnostic suites organized as Ansible roles with tasks/handlers/defaults/vars, callback plugin integration for custom output formatting (json, yaml, timer), vault-encrypted variable management for sensitive credentials, and async task execution for long-running diagnostics with poll intervals. The runner also supports check mode (–check) for dry-run validation, diff mode (–diff) for configuration drift detection, and custom filter plugins for log parsing and metric extraction.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ansible-playbook-diagnostics-runner/)
