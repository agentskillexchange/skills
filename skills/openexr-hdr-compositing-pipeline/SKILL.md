---
name: "OpenEXR HDR Compositing Pipeline"
slug: "openexr-hdr-compositing-pipeline"
description: "Processes OpenEXR high dynamic range images using the OpenImageIO (oiiotool) CLI and Imath library for multi-layer compositing, tone mapping with ACES color transforms, and cryptomatte-based object isolation."
github_stars: 1795
verification: "security_reviewed"
source: "https://github.com/AcademySoftwareFoundation/openexr"
category: "Image & Creative Automation"
framework: "OpenClaw"
tool_ecosystem:
  github_repo: "academysoftwarefoundation/openexr"
  github_stars: 1795
---

# OpenEXR HDR Compositing Pipeline

Processes OpenEXR high dynamic range images using the OpenImageIO (oiiotool) CLI and Imath library for multi-layer compositing, tone mapping with ACES color transforms, and cryptomatte-based object isolation.

## Installation

Use the upstream install or setup path that matches your environment:
- $ cmake -S . -B _build -DCMAKE_PREFIX_PATH=<path to OpenEXR libraries/includes>
- $ cmake --build _build

Requirements and caveats from upstream:
- OpenEXR and its required prerequisites.

Basic usage or getting-started notes:
- See the [technical documentation](https://openexr.readthedocs.io) for
- complete details, but to get started, the "Hello, world" [exrwriter.cpp](https://raw.githubusercontent.com/AcademySoftwareFoundation/openexr/main/website/src/exrwriter/exrwriter.cpp) writer program is:
- #include <ImfRgbaFile.h>

- Source: https://github.com/AcademySoftwareFoundation/openexr
- Extracted from upstream docs: https://raw.githubusercontent.com/AcademySoftwareFoundation/openexr/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/openexr-hdr-compositing-pipeline/)
