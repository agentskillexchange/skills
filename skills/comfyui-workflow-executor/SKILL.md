---
name: "ComfyUI Workflow Executor"
slug: "comfyui-workflow-executor"
description: "Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint."
github_stars: 109121
verification: "listed"
source: "https://github.com/Comfy-Org/ComfyUI"
author: "Comfy Org"
category: "Image & Creative Automation"
framework: "Codex"
tool_ecosystem:
  github_repo: "Comfy-Org/ComfyUI"
  github_stars: 109121
---

# ComfyUI Workflow Executor

Executes ComfyUI image generation workflows via the /prompt REST API endpoint with WebSocket progress tracking. Manages node graph JSON payloads, KSampler scheduler configurations (euler_ancestral, dpmpp_2m_sde), and output image retrieval from the /view endpoint.

## Installation

Use the upstream install or setup path that matches your environment:
- pip install comfy-cli
- Git clone this repo.
- pip install torch torchvision torchaudio --index-url https://download.pytorch.org/whl/rocm7.2
- pip install --pre torch torchvision torchaudio --index-url https://download.pytorch.org/whl/nightly/rocm7.2

Requirements and caveats from upstream:
- ComfyUI is the AI creation engine for visual professionals who demand control over every model, every parameter, and every output. Its powerful and modular node graph interface empowers creatives to generate images, v...
- | Ctrl + B | Bypass selected nodes (acts like the node was removed from the graph and the wires reconnected through) |
- | Ctrl/Shift + Click | Add clicked node to selection |

Basic usage or getting-started notes:
- See what ComfyUI can do with the [newer template workflows](https://comfy.org/workflows) or old [example workflows](https://comfyanonymous.github.io/ComfyUI_examples/).
- Smart memory management: can automatically run large models on GPUs with as low as 1GB vram with smart offloading.
- [Config file](extra_model_paths.yaml.example) to set the search paths for models.

- Source: https://github.com/Comfy-Org/ComfyUI
- Extracted from upstream docs: https://raw.githubusercontent.com/Comfy-Org/ComfyUI/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/comfyui-workflow-executor/)
