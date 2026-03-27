---
name: "RunPod Serverless GPU Inference"
description: "Deploy and manage GPU inference endpoints on RunPod Serverless using their REST API. Handles endpoint creation, cold start optimization, request queuing, and auto-scaling configuration for image generation models."
category: "Image & Creative Automation"
framework: "Claude Agents"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/runpod-serverless-gpu-inference/"
tool_ecosystem:
  tool: docker
  github_stars: 71560
  github_repo: moby/moby
  license: Apache-2.0
  maintained: true
---

# RunPod Serverless GPU Inference

Deploy and manage GPU inference endpoints on RunPod Serverless using their REST API. Handles endpoint creation, cold start optimization, request queuing, and auto-scaling configuration for image generation models.

## Overview

Run GPU-accelerated inference workloads on RunPod’s serverless platform via their management and inference APIs. This skill automates endpoint deployment and request orchestration for ML model serving.

Endpoint creation uses the RunPod GraphQL API to configure worker templates with Docker image references, GPU type selection (A100, A40, RTX 4090), and scaling parameters including min/max workers, idle timeout, and request queue depth.

Inference requests are submitted via POST /v2/{endpoint_id}/run for async execution or /v2/{endpoint_id}/runsync for synchronous responses. The skill manages request lifecycle by polling /v2/{endpoint_id}/status/{job_id} for async jobs and implements client-side timeout handling.

Cold start optimization strategies include maintaining minimum active workers during peak hours, pre-warming endpoints with lightweight health check requests, and configuring execution timeout buffers. The skill tracks per-endpoint metrics including queue depth, average execution time, and GPU utilization via the RunPod status API.

Cost management features monitor GPU-seconds consumed per endpoint and alert when spend approaches configured budget thresholds.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill runpod-serverless-gpu-inference
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill runpod-serverless-gpu-inference -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill runpod-serverless-gpu-inference -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill runpod-serverless-gpu-inference -a codex
```

### OpenClaw

```bash
clawhub install runpod-serverless-gpu-inference
```

## Source

- Marketplace: https://agentskillexchange.com/skills/runpod-serverless-gpu-inference/
