---
title: "RunPod Serverless GPU Inference"
description: "Deploy and manage GPU inference endpoints on RunPod Serverless using their REST API. Handles endpoint creation, cold start optimization, request queuing, and auto-scaling configuration for image generation models."
verification: "security_reviewed"
source: "https://docs.runpod.io/serverless/overview"
category:
  - "Image &amp; Creative Automation"
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

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/runpod-serverless-gpu-inference/)
