---
name: "Stable Diffusion Prompt Optimizer"
slug: "stable-diffusion-prompt-optimizer"
description: "Analyzes and enhances Stable Diffusion prompts using the Automatic1111 WebUI API /sdapi/v1/txt2img endpoint. Applies prompt weighting, negative prompt generation, and A1111-specific syntax like (keyword:weight)."
github_stars: 72984
verification: "listed"
source: "https://github.com/CompVis/stable-diffusion"
category: "Image & Creative Automation"
framework: "Gemini"
tool_ecosystem:
  github_repo: "CompVis/stable-diffusion"
  github_stars: 72984
---

# Stable Diffusion Prompt Optimizer

Analyzes and enhances Stable Diffusion prompts using the Automatic1111 WebUI API /sdapi/v1/txt2img endpoint. Applies prompt weighting, negative prompt generation, and A1111-specific syntax like (keyword:weight).

## Installation

Use the upstream install or setup path that matches your environment:
- conda env create -f environment.yaml
- conda activate ldm
- conda install pytorch torchvision -c pytorch
- pip install transformers==4.19.2 diffusers invisible-watermark

Requirements and caveats from upstream:
- python scripts/txt2img.py --prompt "a photograph of an astronaut riding a horse" --plms
- and renders images of size 512x512 (which it was trained on) in 50 steps. All supported arguments are listed below (type python scripts/txt2img.py --help).

Basic usage or getting-started notes:
- A suitable [conda](https://conda.io/) environment named ldm can be created
- and activated with:
- You can also update an existing [latent diffusion](https://github.com/CompVis/latent-diffusion) environment by running

- Source: https://github.com/CompVis/stable-diffusion
- Extracted from upstream docs: https://raw.githubusercontent.com/CompVis/stable-diffusion/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-prompt-optimizer/)
