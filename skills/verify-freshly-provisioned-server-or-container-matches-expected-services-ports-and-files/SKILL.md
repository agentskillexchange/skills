---
title: "Verify a freshly provisioned server or container matches expected services, ports, and files"
description: "Uses Goss to express the expected state of a machine or container, then validates that reality still matches the contract. Reach for it after provisioning, image builds, or config changes when an agent needs a fast pass or fail answer about service health and system drift."
verification: security_reviewed
source: "https://github.com/goss-org/goss"
category:
  - "Runbooks &amp; Diagnostics"
framework:
  - "Multi-Framework"
---

# Verify a freshly provisioned server or container matches expected services, ports, and files

This skill uses Goss to validate that a newly provisioned server, golden image, or container actually matches the state you intended to ship. Goss works from a YAML test file and can check packages, files, ports, services, processes, users, groups, HTTP endpoints, and more. For an agent, the useful job is very concrete: compare a host or container against an expected operational contract and report drift before that machine goes further down the pipeline.

Invoke this after infrastructure automation has already run, not instead of it. It fits the moment right after cloud-init, Ansible, Terraform, Packer, a Docker build, or a Kubernetes image update when you need to answer questions like “is sshd really listening,” “did the right package version land,” “does the config file exist with the expected mode,” or “did the service come up yet.” An agent can generate an initial baseline with autoadd, trim it to the assertions that matter, run goss validate, and use retry mode to wait until a target reaches a healthy state.

The scope boundary keeps this skill from collapsing into a generic server tool listing. Goss is not configuration management, not a monitoring platform, and not a full compliance suite. It is a fast validation layer for post-provisioning checks and repeatable health assertions. Integration points include CI jobs, container image tests via dgoss, AMI bake pipelines, infrastructure runbooks, and deployment gates that should fail fast when a machine is not in the state the automation promised.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/verify-freshly-provisioned-server-or-container-matches-expected-services-ports-and-files/)
