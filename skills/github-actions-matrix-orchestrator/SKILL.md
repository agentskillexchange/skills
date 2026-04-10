---
name: GitHub Actions Matrix Orchestrator
description: Dynamically generates GitHub Actions matrix strategies using the GitHub
  REST API and workflow dispatch events. Supports conditional job inclusion via the
  actions/github-script action and OIDC token federation for cross-account AWS deployments.
verification: security_reviewed
source: https://agentskillexchange.com/skills/github-actions-matrix-orchestrator/
category:
- CI/CD Integrations
framework:
- Claude Code
---
# GitHub Actions Matrix Orchestrator

Overview
The GitHub Actions Matrix Orchestrator dynamically generates CI/CD matrix strategies for complex multi-platform builds. By leveraging the GitHub REST API's workflow dispatch endpoint and the actions/github-script action, it creates conditional job matrices that adapt based on changed files, branch names, or PR labels.
Key Capabilities
This skill handles OIDC token federation for cross-account AWS deployments, enabling secure assume-role operations without storing long-lived credentials. It analyzes dorny/paths-filter outputs to determine which matrix combinations are necessary, reducing unnecessary CI minutes. The orchestrator supports reusable workflow composition with workflow_call triggers and dynamic job generation through JSON matrix output steps.
Technical Integration
Integrates with GitHub's check runs API for granular status reporting, supports concurrency groups for deployment serialization, and manages artifact retention policies through the actions/upload-artifact v4 API. Compatible with self-hosted runners using custom labels and runner groups.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/github-actions-matrix-orchestrator/)
