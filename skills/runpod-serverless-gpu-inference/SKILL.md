---
title: "RunPod Serverless GPU Inference"
description: "Deploy and manage GPU inference endpoints on RunPod Serverless using their REST API. Handles endpoint creation, cold start optimization, request queuing, and auto-scaling configuration for image generation models."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/runpod-serverless-gpu-inference/"
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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/runpod-serverless-gpu-inference/)
