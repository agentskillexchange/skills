---
title: "Kestra Event-Driven Orchestration and Scheduling Platform"
description: "Kestra is an open-source, event-driven orchestration platform that makes both scheduled and event-driven workflows easy. Define workflows declaratively in YAML with a rich plugin ecosystem covering databases, cloud storage, APIs, and scripting in any language."
verification: "security_reviewed"
source: "https://github.com/kestra-io/kestra"
category:
  - "Templates &amp; Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "kestra-io/kestra"
  github_stars: 26683
---

# Kestra Event-Driven Orchestration and Scheduling Platform

Kestra is an open-source orchestration and scheduling platform built for mission-critical applications. It provides a declarative YAML-based workflow definition system with a built-in code editor, enabling teams to create, manage, and monitor complex data pipelines and process automation workflows.

Core Capabilities

Kestra supports both scheduled and real-time event-driven workflows through a simple trigger definition system. Workflows are defined using YAML configuration files that can be version-controlled with Git. The platform includes an intuitive web UI with syntax highlighting, auto-completion, and real-time validation for building and visualizing workflows.

Plugin Ecosystem

The platform ships with hundreds of built-in plugins for extracting data from databases (PostgreSQL, MySQL, BigQuery), cloud storage services (S3, GCS, Azure Blob), REST APIs, and running scripts in Python, Node.js, R, Julia, and shell. Custom plugins can be developed using the Kestra Plugin SDK.

Workflow Features

Kestra provides enterprise-grade workflow capabilities including namespaces for organization, labels for categorization, subflows for modular composition, automatic retries with configurable backoff, timeout handling, comprehensive error management, conditional branching, dynamic task generation, and both sequential and parallel task execution. Workflows support inputs, outputs, and variables for parameterization.

Deployment and Scaling

The platform can be deployed via Docker with a single command, on AWS using CloudFormation templates, or on Google Cloud via Terraform modules. Kestra is designed to handle millions of workflows with high availability and fault tolerance. It supports Infrastructure as Code practices through its Git integration, CI/CD pipeline compatibility, and Terraform provider for managing workflows programmatically.

Agent Integration

AI agents can use Kestra to orchestrate multi-step data pipelines, automate ETL processes, schedule recurring jobs, react to webhook events, and coordinate complex workflows across multiple services. The REST API enables programmatic workflow management, execution triggering, and status monitoring.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kestra-event-driven-orchestration-scheduling-platform/)
