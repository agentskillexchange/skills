---
title: "Oxipng Multithreaded Lossless PNG Compression Optimizer"
description: "Oxipng is a multithreaded lossless PNG and APNG compression optimizer written in Rust. It reduces PNG file sizes without any quality loss using advanced compression techniques including Zopfli support, metadata stripping, and alpha channel optimization."
slug: "oxipng-png-compression-optimizer"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/oxipng/oxipng"
tool_ecosystem:
  github_repo: "oxipng/oxipng"
  github_stars: 3870
listed: true
---

# Oxipng Multithreaded Lossless PNG Compression Optimizer

Oxipng is a multithreaded lossless PNG and APNG compression optimizer written in Rust. It reduces PNG file sizes without any quality loss using advanced compression techniques including Zopfli support, metadata stripping, and alpha channel optimization.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install oxipng-png-compression-optimizer
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Oxipng is a high-performance, multithreaded lossless PNG and APNG compression optimizer written in Rust. It serves as a modern replacement for OptiPNG, delivering significantly faster optimization through parallel processing while maintaining or exceeding compression ratios.
How It Works
Oxipng analyzes PNG files and applies a series of lossless compression strategies to reduce file size without altering image quality. It tries multiple filter and compression combinations, selecting the smallest output. The tool supports optimization levels from 0 (fastest) through 6 and max (best compression), allowing users to balance speed versus compression ratio.
Key Capabilities
The CLI provides several powerful features for image optimization workflows:
- Multithreaded processing: Takes full advantage of modern multi-core CPUs for faster optimization of large batches of PNG files.
- Lossless compression: Reduces file size without any quality degradation, making it safe for production assets.
- Metadata stripping: The --strip safe option removes non-essential metadata (EXIF, text chunks) while preserving rendering-critical data. Use --strip all for maximum savings.
- Alpha optimization: The --alpha flag optimizes fully transparent pixels for better compression.
- Zopfli compression: Optional Zopfli backend (-Z) for maximum compression at the cost of speed.
- APNG support: Handles animated PNG files in addition to static PNGs.
- Batch processing: Supports glob patterns like oxipng *.png for processing entire directories.
Integration Points
Oxipng integrates into CI/CD pipelines, static site generators, and build systems. Install via cargo install oxipng, system package managers (Homebrew, apt, pacman), or download prebuilt binaries from GitHub Releases. It can also be used as a Rust library crate for embedding in other applications. Common integration patterns include pre-commit hooks for image assets, build step optimization in web projects, and automated asset pipelines.
Example Usage
oxipng -o 4 --strip safe --alpha *.png
This command optimizes all PNG files in the current directory at level 4, strips safe metadata, and optimizes alpha channels.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/oxipng-png-compression-optimizer/)
