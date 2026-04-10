---
title: "Cerbos Open Source Authorization Policy Decision Point"
description: "Cerbos is an open-core, language-agnostic, scalable authorization solution that makes implementing and managing user permissions simple. It uses context-aware YAML access control policies managed through Git-ops, providing high-availability APIs for dynamic access decisions across applications."
slug: "cerbos-authorization-pdp"
category:
  - "Security &amp; Verification"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/cerbos/cerbos"
listed: true
---

# Cerbos Open Source Authorization Policy Decision Point

Cerbos is an open-core, language-agnostic, scalable authorization solution that makes implementing and managing user permissions simple. It uses context-aware YAML access control policies managed through Git-ops, providing high-availability APIs for dynamic access decisions across applications.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install cerbos-authorization-pdp
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Cerbos is a self-hosted Policy Decision Point (PDP) that provides fine-grained authorization for applications of any scale. Rather than embedding complex permission logic directly in application code, developers define access control rules in declarative YAML policies that are stored alongside application code in Git repositories.
The Cerbos PDP is a stateless service that evaluates authorization requests against defined policies. It exposes two primary APIs: CheckResources (determining whether a principal can access a specific resource) and PlanResources (identifying which resources of a given kind a principal can access). These APIs can be called via HTTP/gRPC or through official client SDKs available for Go, Java, JavaScript/TypeScript, Python, Ruby, Rust, PHP, .NET, and more.
Cerbos supports progressive authorization complexity. Teams can start with straightforward Role-Based Access Control (RBAC), then layer on Attribute-Based Access Control (ABAC) by adding conditions to resource policies that are evaluated dynamically at runtime using contextual data. Derived roles allow extending RBAC roles dynamically based on runtime attributes, while principal policies enable user-specific overrides.
Policies are organized into three types: resource policies define access rules per resource kind, derived roles compute dynamic roles from existing ones using conditions, and principal policies create exceptions for specific users. All policies are versioned and can be hot-reloaded without service restarts.
Deployment is flexible: Cerbos runs as a Kubernetes service or sidecar, a systemd service, an AWS Lambda function, or a Docker container. Policy storage supports local disk, cloud object stores (S3, GCS, Azure Blob), Git repositories, and databases (PostgreSQL, MySQL, SQLite). The PDP includes a built-in Admin API for runtime management and audit logging for compliance.
For AI agents and automated systems, Cerbos provides a clean API boundary for authorization decisions. Agents can query the PDP to determine permitted actions before executing operations, ensuring consistent policy enforcement across human and automated workflows. The PlanResources API is particularly useful for agents that need to discover what resources they can operate on without trial-and-error.
Installation is straightforward: download the binary, run it with a configuration file pointing to your policy directory, and start making API calls. Docker images are available for all platforms, and Helm charts support Kubernetes deployments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cerbos-authorization-pdp/)
