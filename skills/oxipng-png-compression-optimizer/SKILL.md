---
title: "Oxipng Multithreaded Lossless PNG Compression Optimizer"
description: "Oxipng is a multithreaded lossless PNG and APNG compression optimizer written in Rust. It reduces PNG file sizes without any quality loss using advanced compression techniques including Zopfli support, metadata stripping, and alpha channel optimization."
verification: security_reviewed
source: "https://github.com/oxipng/oxipng"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "oxipng/oxipng"
  github_stars: 3870
---

# Oxipng Multithreaded Lossless PNG Compression Optimizer

Oxipng is a high-performance, multithreaded lossless PNG and APNG compression optimizer written in Rust. It serves as a modern replacement for OptiPNG, delivering significantly faster optimization through parallel processing while maintaining or exceeding compression ratios.

How It Works
Oxipng analyzes PNG files and applies a series of lossless compression strategies to reduce file size without altering image quality. It tries multiple filter and compression combinations, selecting the smallest output. The tool supports optimization levels from 0 (fastest) through 6 and max (best compression), allowing users to balance speed versus compression ratio.

Key Capabilities
The CLI provides several powerful features for image optimization workflows:

Multithreaded processing: Takes full advantage of modern multi-core CPUs for faster optimization of large batches of PNG files.
Lossless compression: Reduces file size without any quality degradation, making it safe for production assets.
Metadata stripping: The --strip safe option removes non-essential metadata (EXIF, text chunks) while preserving rendering-critical data. Use --strip all for maximum savings.
Alpha optimization: The --alpha flag optimizes fully transparent pixels for better compression.
Zopfli compression: Optional Zopfli backend (-Z) for maximum compression at the cost of speed.
APNG support: Handles animated PNG files in addition to static PNGs.
Batch processing: Supports glob patterns like oxipng *.png for processing entire directories.

Integration Points
Oxipng integrates into CI/CD pipelines, static site generators, and build systems. Install via cargo install oxipng, system package managers (Homebrew, apt, pacman), or download prebuilt binaries from GitHub Releases. It can also be used as a Rust library crate for embedding in other applications. Common integration patterns include pre-commit hooks for image assets, build step optimization in web projects, and automated asset pipelines.

Example Usage
oxipng -o 4 --strip safe --alpha *.png
This command optimizes all PNG files in the current directory at level 4, strips safe metadata, and optimizes alpha channels.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/oxipng-png-compression-optimizer/)
