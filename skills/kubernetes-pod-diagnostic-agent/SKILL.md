---
title: Kubernetes Pod Diagnostic Agent
description: Diagnoses Kubernetes pod failures using kubectl and the Kubernetes API
  server endpoints. Analyzes CrashLoopBackOff, OOMKilled, and ImagePullBackOff states
  by querying /api/v1/namespaces/{ns}/pods/{pod}/log and /api/v1/events resources.
verification: security_reviewed
source: https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-agent/
category:
- Runbooks & Diagnostics
framework:
- Codex
---


# Kubernetes Pod Diagnostic Agent

Diagnoses Kubernetes pod failures using kubectl and the Kubernetes API server endpoints. Analyzes CrashLoopBackOff, OOMKilled, and ImagePullBackOff states by querying /api/v1/namespaces/{ns}/pods/{pod}/log and /api/v1/events resources.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/kubernetes-pod-diagnostic-agent/)
