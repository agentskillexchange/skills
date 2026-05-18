---
name: "Oxipng Multithreaded Lossless PNG Compression Optimizer"
slug: "oxipng-png-compression-optimizer"
description: "Oxipng is a multithreaded lossless PNG and APNG compression optimizer written in Rust. It reduces PNG file sizes without any quality loss using advanced compression techniques including Zopfli support, metadata stripping, and alpha channel optimization."
github_stars: 3870
verification: "security_reviewed"
source: "https://github.com/oxipng/oxipng"
category: "Image & Creative Automation"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "oxipng/oxipng"
  github_stars: 3870
---

# Oxipng Multithreaded Lossless PNG Compression Optimizer

Oxipng is a multithreaded lossless PNG and APNG compression optimizer written in Rust. It reduces PNG file sizes without any quality loss using advanced compression techniques including Zopfli support, metadata stripping, and alpha channel optimization.

## Installation

Use the upstream install or setup path that matches your environment:
- cargo install oxipng
- git clone https://github.com/oxipng/oxipng.git
- cargo build --release
- docker run --rm -v $(pwd):/work ghcr.io/oxipng/oxipng -o 4 /work/file.png

Requirements and caveats from upstream:
- ## Docker
- A Docker image is availlable at [ghcr.io/oxipng/oxipng](https://github.com/oxipng/oxipng/pkgs/container/oxipng) for linux/amd64 and linux/arm64.
- [pyoxipng](https://pypi.org/project/pyoxipng/): Python wrapper for Oxipng

Basic usage or getting-started notes:
- Oxipng is a command-line utility. An example usage, suitable for web, may be the following:
- oxipng -o 4 --strip safe --alpha *.png
- The most commonly used options are as follows:

- Source: https://github.com/oxipng/oxipng
- Extracted from upstream docs: https://raw.githubusercontent.com/oxipng/oxipng/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/oxipng-png-compression-optimizer/)
