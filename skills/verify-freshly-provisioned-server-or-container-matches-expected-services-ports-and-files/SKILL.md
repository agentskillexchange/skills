---
title: "Verify a freshly provisioned server or container matches expected services, ports, and files"
description: "This skill uses Goss to validate that a newly provisioned server, golden image, or container actually matches the state you intended to ship. Goss works from a YAML test file and can check packages, files, ports, services, processes, users, groups, HTTP endpoints, and more. For an agent, the useful job is very concrete: compare a host or container against an expected operational contract and report drift before that machine goes further down the pipeline. Invoke this after infrastructure automation has already run, not instead of it. It fits the moment right after cloud-init, Ansible, Terraform, Packer, a Docker build, or a Kubernetes image update when you need to answer questions like “is sshd really listening,” “did the right package version land,” “does the config file exist with the expected mode,” or “did the service come up yet.” An agent can generate an initial baseline with autoadd , trim it to the assertions that matter, run goss validate , and use retry mode to wait until a target reaches a healthy state. The scope boundary keeps this skill from collapsing into a generic server tool listing. Goss is not configuration management, not a monitoring platform, and not a full compliance suite. It is a fast validation layer for post-provisioning checks and repeatable health assertions. Integration points include CI jobs, container image tests via dgoss , AMI bake pipelines, infrastructure runbooks, and deployment gates that should fail fast when a machine is not in the state the automation promised."
source: "https://github.com/goss-org/goss"
verification: "security_reviewed"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "goss-org/goss"
  github_stars: 5877
---

# Verify a freshly provisioned server or container matches expected services, ports, and files

This skill uses Goss to validate that a newly provisioned server, golden image, or container actually matches the state you intended to ship. Goss works from a YAML test file and can check packages, files, ports, services, processes, users, groups, HTTP endpoints, and more. For an agent, the useful job is very concrete: compare a host or container against an expected operational contract and report drift before that machine goes further down the pipeline. Invoke this after infrastructure automation has already run, not instead of it. It fits the moment right after cloud-init, Ansible, Terraform, Packer, a Docker build, or a Kubernetes image update when you need to answer questions like “is sshd really listening,” “did the right package version land,” “does the config file exist with the expected mode,” or “did the service come up yet.” An agent can generate an initial baseline with autoadd , trim it to the assertions that matter, run goss validate , and use retry mode to wait until a target reaches a healthy state. The scope boundary keeps this skill from collapsing into a generic server tool listing. Goss is not configuration management, not a monitoring platform, and not a full compliance suite. It is a fast validation layer for post-provisioning checks and repeatable health assertions. Integration points include CI jobs, container image tests via dgoss , AMI bake pipelines, infrastructure runbooks, and deployment gates that should fail fast when a machine is not in the state the automation promised.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-freshly-provisioned-server-or-container-matches-expected-services-ports-and-files/)
