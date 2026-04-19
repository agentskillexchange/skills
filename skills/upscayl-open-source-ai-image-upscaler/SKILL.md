---
title: "Upscayl Open Source AI Image Upscaler"
description: "Upscayl is a cross-platform desktop application that upscales images using AI-powered super-resolution models. Built with Electron and backed by a Real-ESRGAN engine using Vulkan GPU acceleration, Upscayl enhances low-resolution images by intelligently predicting and reconstructing fine details that were not present in the original. How It Works Upscayl wraps the upscayl-ncnn binary (an open-source NCNN-based Real-ESRGAN implementation) in a user-friendly GUI. Users drag and drop images into the interface, select an upscaling model and scale factor (2x or 4x), and the tool processes them through the neural network on the GPU via the Vulkan API. The result is a higher-resolution image with AI-generated detail enhancement. Models and Customization Upscayl ships with several built-in models optimized for different use cases: general photo upscaling, digital art enhancement, and ultrasharp detail recovery. Users can also import custom NCNN models converted from ESRGAN-compatible architectures. The community maintains an additional model repository at github.com/upscayl/custom-models with specialized models for anime, faces, and other domains. Batch Processing Beyond single-image upscaling, Upscayl supports batch mode for processing entire folders of images at once. Users can set output format (PNG, JPG, WebP), quality level, and target scale. This makes it practical for bulk asset preparation, game texture upscaling, and archival photo restoration workflows. Platform Support Upscayl runs on Linux (AppImage, Flatpak, Snap, DEB, RPM), macOS (DMG, Homebrew via brew install --cask upscayl ), and Windows (EXE installer). It requires a Vulkan-compatible GPU for operation. The project has over 44,000 GitHub stars and is licensed under AGPL-3.0. Integration for Agents While Upscayl is primarily a GUI application, its underlying upscayl-ncnn binary can be invoked directly from the command line for automated pipelines. Agents can use it to upscale screenshots, enhance scraped images, improve thumbnail quality, or prepare high-resolution assets as part of content generation workflows."
source: "https://github.com/upscayl/upscayl"
verification: "security_reviewed"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "upscayl/upscayl"
  github_stars: 44297
---

# Upscayl Open Source AI Image Upscaler

Upscayl is a cross-platform desktop application that upscales images using AI-powered super-resolution models. Built with Electron and backed by a Real-ESRGAN engine using Vulkan GPU acceleration, Upscayl enhances low-resolution images by intelligently predicting and reconstructing fine details that were not present in the original. How It Works Upscayl wraps the upscayl-ncnn binary (an open-source NCNN-based Real-ESRGAN implementation) in a user-friendly GUI. Users drag and drop images into the interface, select an upscaling model and scale factor (2x or 4x), and the tool processes them through the neural network on the GPU via the Vulkan API. The result is a higher-resolution image with AI-generated detail enhancement. Models and Customization Upscayl ships with several built-in models optimized for different use cases: general photo upscaling, digital art enhancement, and ultrasharp detail recovery. Users can also import custom NCNN models converted from ESRGAN-compatible architectures. The community maintains an additional model repository at github.com/upscayl/custom-models with specialized models for anime, faces, and other domains. Batch Processing Beyond single-image upscaling, Upscayl supports batch mode for processing entire folders of images at once. Users can set output format (PNG, JPG, WebP), quality level, and target scale. This makes it practical for bulk asset preparation, game texture upscaling, and archival photo restoration workflows. Platform Support Upscayl runs on Linux (AppImage, Flatpak, Snap, DEB, RPM), macOS (DMG, Homebrew via brew install --cask upscayl ), and Windows (EXE installer). It requires a Vulkan-compatible GPU for operation. The project has over 44,000 GitHub stars and is licensed under AGPL-3.0. Integration for Agents While Upscayl is primarily a GUI application, its underlying upscayl-ncnn binary can be invoked directly from the command line for automated pipelines. Agents can use it to upscale screenshots, enhance scraped images, improve thumbnail quality, or prepare high-resolution assets as part of content generation workflows.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/upscayl-open-source-ai-image-upscaler/)
