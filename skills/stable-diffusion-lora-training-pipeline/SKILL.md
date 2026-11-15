---
name: "Stable Diffusion LoRA Training Pipeline"
slug: "stable-diffusion-lora-training-pipeline"
description: "Orchestrates LoRA fine-tuning for Stable Diffusion XL using the diffusers library and Kohya ss-scripts. Manages dataset preparation with BLIP-2 auto-captioning, configures AdaFactor optimizer parameters, and exports safetensors checkpoints with A1111 metadata embedding."
github_stars: 7023
verification: "security_reviewed"
source: "https://github.com/kohya-ss/sd-scripts"
category: "Image & Creative Automation"
framework: "Custom Agents"
tool_ecosystem:
  github_repo: "kohya-ss/sd-scripts"
  github_stars: 7023
---

# Stable Diffusion LoRA Training Pipeline

Orchestrates LoRA fine-tuning for Stable Diffusion XL using the diffusers library and Kohya ss-scripts. Manages dataset preparation with BLIP-2 auto-captioning, configures AdaFactor optimizer parameters, and exports safetensors checkpoints with A1111 metadata embedding.

## Installation

Use the upstream install or setup path that matches your environment:
- git clone https://github.com/kohya-ss/sd-scripts.git
- pip install torch==2.6.0 torchvision==0.21.0 --index-url https://download.pytorch.org/whl/cu124
- pip install --upgrade -r requirements.txt
- This installation is for CUDA 12.4. If you use a different version of CUDA, please install the appropriate version of PyTorch. For example, if you use CUDA 12.1, please install pip install torch==2.6.0 torchvision==0....

Requirements and caveats from upstream:
- Python 3.10.x and Git:
- Python 3.10.x: Download Windows installer (64-bit) from https://www.python.org/downloads/windows/
- Python 3.11.x, and 3.12.x will work but not tested.

Basic usage or getting-started notes:
- Open a regular Powershell terminal and type the following inside:
- powershell
- cd sd-scripts

- Source: https://github.com/kohya-ss/sd-scripts
- Extracted from upstream docs: https://raw.githubusercontent.com/kohya-ss/sd-scripts/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/stable-diffusion-lora-training-pipeline/)
