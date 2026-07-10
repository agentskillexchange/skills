---
name: "Stable Diffusion ControlNet Pipeline"
slug: "stable-diffusion-controlnet-pipeline"
description: "Automates image generation workflows using Stability AI ControlNet API with depth maps, edge detection, and pose estimation. Integrates with Hugging Face diffusers library for model management and CLIP interrogator for prompt refinement."
github_stars: 33867
verification: "security_reviewed"
source: "https://github.com/lllyasviel/ControlNet"
category: "Image & Creative Automation"
framework: "Cursor"
tool_ecosystem:
  github_repo: "lllyasviel/ControlNet"
  github_stars: 33867
---

# Stable Diffusion ControlNet Pipeline

Automates image generation workflows using Stability AI ControlNet API with depth maps, edge detection, and pose estimation. Integrates with Hugging Face diffusers library for model management and CLIP interrogator for prompt refinement.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-controlnet-pipeline/)
