---
name: Stable Diffusion ControlNet Pipeline
description: Automates image generation workflows using Stability AI ControlNet API
  with depth maps, edge detection, and pose estimation. Integrates with Hugging Face
  diffusers library for model management and CLIP interrogator for prompt refinement.
category: "Image &amp; Creative Automation"
framework: Cursor
verification: security_reviewed
source: "https://agentskillexchange.com/skills/stable-diffusion-controlnet-pipeline/"
---
# Stable Diffusion ControlNet Pipeline

Automates image generation workflows using Stability AI ControlNet API with depth maps, edge detection, and pose estimation. Integrates with Hugging Face diffusers library for model management and CLIP interrogator for prompt refinement.

The Stable Diffusion ControlNet Pipeline skill provides a comprehensive image generation framework that leverages ControlNet conditioning models through the Stability AI API. It supports multiple control modes including depth mapping via MiDaS, edge detection through Canny filters, and OpenPose skeleton estimation for precise human figure guidance.

The skill integrates directly with the Hugging Face diffusers library to manage model downloads, LoRA weight loading, and scheduler configuration. It includes CLIP interrogator functionality to reverse-engineer prompts from reference images, enabling style transfer workflows.

Key capabilities include batch processing with configurable seed management, automatic EXIF metadata embedding, and resolution upscaling via Real-ESRGAN. The pipeline supports both local ComfyUI backends and cloud Stability AI endpoints, with automatic fallback between providers. Output images are validated against NSFW classifiers and can be automatically uploaded to S3-compatible storage with CDN invalidation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-controlnet-pipeline
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-controlnet-pipeline -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-controlnet-pipeline -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill stable-diffusion-controlnet-pipeline -a codex
```

### OpenClaw

```bash
clawhub install stable-diffusion-controlnet-pipeline
```


## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-pipeline/)
