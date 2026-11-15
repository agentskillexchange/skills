---
name: "Transfer clothed character poses from mannequin renders with Qwen Pose"
slug: "transfer-clothed-character-poses-from-mannequin-renders-with-qwen-pose"
description: "Apply an existing textureless 3D mannequin pose to a clothed character image through a repeatable local ComfyUI edit, with PNG and JSON artifacts."
github_stars: 3462
verification: "security_reviewed"
source: "https://github.com/Arekejoker/qwen21-nsfw-pose-skill"
author: "Arekejoker"
publisher_type: "individual"
category: "Image & Creative Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "Arekejoker/qwen21-nsfw-pose-skill"
  github_stars: 3462
---

# Transfer clothed character poses from mannequin renders with Qwen Pose

Apply an existing textureless 3D mannequin pose to a clothed character image through a repeatable local ComfyUI edit, with PNG and JSON artifacts.

## Prerequisites

Python 3.10+; approved ComfyUI server; Qwen-Image 2.1 base models; VNCCS PoseStudio LoRA; bundled Route 3 script and workflow; character image; existing textureless 3D mannequin render

## Installation

Install or set up from the source-backed instructions:

Clone https://github.com/Arekejoker/qwen21-nsfw-pose-skill into a working directory. Follow install/setup.md for Python 3.10+, a running ComfyUI server, the three Qwen-Image 2.1 base model files, and the VNCCS PoseStudio LoRA required by Route 3. Configure COMFY and COMFYUI_URL for that installation. Supply an existing textureless 3D mannequin render and an authorized, clothed character image. Run python3 scripts/doctor.py to inspect prerequisites. Route 3 uses Python standard-library scripts and existing renders; its setup does not require browser authentication, the pose-library browser runner, or the separate NSFW model recipes.

- Source: https://github.com/Arekejoker/qwen21-nsfw-pose-skill

## Documentation

- https://github.com/Arekejoker/qwen21-nsfw-pose-skill/blob/main/SKILL.md#6-route--scripted-pose-transfer-3d-mannequin-reference

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/transfer-clothed-character-poses-from-mannequin-renders-with-qwen-pose/)
