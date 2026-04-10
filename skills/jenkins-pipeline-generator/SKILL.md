---
name: Jenkins Pipeline Generator
description: Generates declarative Jenkins pipeline scripts using the Jenkins Pipeline
  Syntax reference and shared library patterns. Integrates with the Jenkins REST API
  (/api/json) for job configuration and the Blue Ocean API for pipeline visualization.
verification: security_reviewed
source: https://agentskillexchange.com/skills/jenkins-pipeline-generator/
category:
- CI/CD Integrations
framework:
- Custom Agents
---
# Jenkins Pipeline Generator

The Jenkins Pipeline Generator skill automates the creation of declarative and scripted Jenkins pipeline definitions following the official Pipeline Syntax reference. It generates Jenkinsfile content with proper stage definitions, parallel execution blocks, post-condition handlers, and agent specifications for both traditional and Kubernetes-based executors.
This skill integrates with the Jenkins REST API (/api/json) to discover existing job configurations, installed plugins, and available build agents. It queries the Blue Ocean API endpoints for pipeline run visualization data and uses the Pipeline Model Definition API to validate generated pipeline syntax before deployment.
Shared library integration is a core capability, generating vars/ scripts and src/ classes that follow Jenkins shared library conventions. The skill creates library configurations with proper @Library annotations and manages version pinning for reproducible builds across teams.
Advanced features include generating multibranch pipeline configurations with custom branch discovery strategies, creating pipeline templates for common patterns like build-test-deploy with approval gates, and configuring credential bindings using the Jenkins Credentials API. The skill also generates proper Groovy sandbox-compatible code to avoid script approval requirements.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/jenkins-pipeline-generator/)
