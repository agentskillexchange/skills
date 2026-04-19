---
title: "RunPod Serverless GPU Inference"
description: "Run GPU-accelerated inference workloads on RunPod&#8217;s serverless platform via their management and inference APIs. This skill automates endpoint deployment and request orchestration for ML model serving. Endpoint creation uses the RunPod GraphQL API to configure worker templates with Docker image references, GPU type selection (A100, A40, RTX 4090), and scaling parameters including min/max workers, idle timeout, and request queue depth. Inference requests are submitted via POST /v2/{endpoint_id}/run for async execution or /v2/{endpoint_id}/runsync for synchronous responses. The skill manages request lifecycle by polling /v2/{endpoint_id}/status/{job_id} for async jobs and implements client-side timeout handling. Cold start optimization strategies include maintaining minimum active workers during peak hours, pre-warming endpoints with lightweight health check requests, and configuring execution timeout buffers. The skill tracks per-endpoint metrics including queue depth, average execution time, and GPU utilization via the RunPod status API. Cost management features monitor GPU-seconds consumed per endpoint and alert when spend approaches configured budget thresholds."
source: "https://docs.runpod.io/serverless/overview"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Claude Agents"
---

# RunPod Serverless GPU Inference

Run GPU-accelerated inference workloads on RunPod&#8217;s serverless platform via their management and inference APIs. This skill automates endpoint deployment and request orchestration for ML model serving. Endpoint creation uses the RunPod GraphQL API to configure worker templates with Docker image references, GPU type selection (A100, A40, RTX 4090), and scaling parameters including min/max workers, idle timeout, and request queue depth. Inference requests are submitted via POST /v2/{endpoint_id}/run for async execution or /v2/{endpoint_id}/runsync for synchronous responses. The skill manages request lifecycle by polling /v2/{endpoint_id}/status/{job_id} for async jobs and implements client-side timeout handling. Cold start optimization strategies include maintaining minimum active workers during peak hours, pre-warming endpoints with lightweight health check requests, and configuring execution timeout buffers. The skill tracks per-endpoint metrics including queue depth, average execution time, and GPU utilization via the RunPod status API. Cost management features monitor GPU-seconds consumed per endpoint and alert when spend approaches configured budget thresholds.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/runpod-serverless-gpu-inference/)
