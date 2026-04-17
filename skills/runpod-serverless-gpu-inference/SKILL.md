---
title: "RunPod Serverless GPU Inference"
description: "Run GPU-accelerated inference workloads on RunPod’s serverless platform via their management and inference APIs. This skill automates endpoint deployment and request orchestration for ML model serving.\nEndpoint creation uses the RunPod GraphQL API to configure worker templates with Docker image references, GPU type selection (A100, A40, RTX 4090), and scaling parameters including min/max workers, idle timeout, and request queue depth.\nInference requests are submitted via POST /v2/{endpoint_id}/run for async execution or /v2/{endpoint_id}/runsync for synchronous responses. The skill manages request lifecycle by polling /v2/{endpoint_id}/status/{job_id} for async jobs and implements client-side timeout handling.\nCold start optimization strategies include maintaining minimum active workers during peak hours, pre-warming endpoints with lightweight health check requests, and configuring execution timeout buffers. The skill tracks per-endpoint metrics including queue depth, average execution time, and GPU utilization via the RunPod status API.\nCost management features monitor GPU-seconds consumed per endpoint and alert when spend approaches configured budget thresholds."
verification: security_reviewed
source: "https://docs.runpod.io/serverless/overview"
framework:
  - "Claude Agents"
---

# RunPod Serverless GPU Inference

Run GPU-accelerated inference workloads on RunPod’s serverless platform via their management and inference APIs. This skill automates endpoint deployment and request orchestration for ML model serving.
Endpoint creation uses the RunPod GraphQL API to configure worker templates with Docker image references, GPU type selection (A100, A40, RTX 4090), and scaling parameters including min/max workers, idle timeout, and request queue depth.
Inference requests are submitted via POST /v2/{endpoint_id}/run for async execution or /v2/{endpoint_id}/runsync for synchronous responses. The skill manages request lifecycle by polling /v2/{endpoint_id}/status/{job_id} for async jobs and implements client-side timeout handling.
Cold start optimization strategies include maintaining minimum active workers during peak hours, pre-warming endpoints with lightweight health check requests, and configuring execution timeout buffers. The skill tracks per-endpoint metrics including queue depth, average execution time, and GPU utilization via the RunPod status API.
Cost management features monitor GPU-seconds consumed per endpoint and alert when spend approaches configured budget thresholds.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/runpod-serverless-gpu-inference
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/runpod-serverless-gpu-inference` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/runpod-serverless-gpu-inference/)
