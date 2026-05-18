---
name: "Stable Diffusion ControlNet Pose Pipeline"
slug: "stable-diffusion-controlnet-pose-pipeline"
description: "Orchestrates Stable Diffusion image generation with ControlNet pose conditioning via the Automatic1111 API. Chains OpenPose detection, depth estimation, and img2img endpoints."
github_stars: 33793
verification: "security_reviewed"
source: "https://github.com/lllyasviel/ControlNet"
category: "Image & Creative Automation"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "lllyasviel/ControlNet"
  github_stars: 33793
---

# Stable Diffusion ControlNet Pose Pipeline

Orchestrates Stable Diffusion image generation with ControlNet pose conditioning via the Automatic1111 API. Chains OpenPose detection, depth estimation, and img2img endpoints.

## Installation

Use the upstream install or setup path that matches your environment:
- conda env create -f environment.yaml
- conda activate control

Requirements and caveats from upstream:
- python gradio_canny2image.py
- python gradio_hough2image.py
- python gradio_hed2image.py

Basic usage or getting-started notes:
- Note that the UI is based on Gradio, and Gradio is somewhat difficult to customize. Right now you need to draw scribbles outside the UI (using your favorite drawing software, for example, MS Paint) and then import the...
- Note that the below example is 768×768. No prompts. No "positive" prompts. No "negative" prompts.
- Below is another challenging example:

- Source: https://github.com/lllyasviel/ControlNet
- Extracted from upstream docs: https://raw.githubusercontent.com/lllyasviel/ControlNet/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-pose-pipeline/)
