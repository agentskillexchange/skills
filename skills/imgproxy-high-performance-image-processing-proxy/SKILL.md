---
title: "imgproxy High-Performance Image Processing Proxy"
description: "An agent skill built on imgproxy, the high-performance Go-based image processing server, enabling on-the-fly image resizing, cropping, format conversion, and optimization through URL-based transformations. Designed for production CDN pipelines and automated media workflows."
slug: "imgproxy-high-performance-image-processing-proxy"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/imgproxy/imgproxy"
tool_ecosystem:
  github_repo: "imgproxy/imgproxy"
  github_stars: 10554
---

# imgproxy High-Performance Image Processing Proxy

An agent skill built on imgproxy, the high-performance Go-based image processing server, enabling on-the-fly image resizing, cropping, format conversion, and optimization through URL-based transformations. Designed for production CDN pipelines and automated media workflows.

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
clawhub install imgproxy-high-performance-image-processing-proxy
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

imgproxy is a standalone, high-performance image processing server written in Go that uses libvips under the hood for fast, memory-efficient image operations. This skill enables agents to generate optimized image variants through URL-based processing directives without touching the original source files.
Core Capabilities
The skill constructs imgproxy-compatible processing URLs that specify resize dimensions, crop gravity, output format, quality level, and advanced operations like watermarking, blurring, sharpening, and rotation. imgproxy handles automatic format negotiation, serving WebP or AVIF to browsers that support them while falling back to JPEG or PNG for older clients. It supports processing pipelines that chain multiple operations in a single request.
How It Works
Agents provide a source image URL and the desired transformations. The skill builds a signed processing URL using HMAC-based signature verification to prevent unauthorized usage. imgproxy fetches the source image, applies the transformation pipeline, and returns the processed result. The server supports streaming responses and concurrent processing, handling thousands of image operations per second on modest hardware.
Security and Performance
All processing URLs are cryptographically signed to prevent abuse. imgproxy runs in a Docker container with minimal attack surface and supports allowlisting source domains. The libvips engine processes images in constant memory regardless of image size, avoiding the memory spikes common with ImageMagick-based solutions. It supports reading from local storage, S3, Google Cloud Storage, and Azure Blob Storage.
Integration Points
The skill integrates with CDN edge workers for dynamic image optimization, content management systems for responsive image generation, and e-commerce platforms for product image processing. imgproxy supports JPEG, PNG, WebP, AVIF, GIF, ICO, SVG, HEIC, BMP, and TIFF formats for both input and output.
Technical Details
imgproxy is written in Go, distributed as Docker images and pre-built binaries, and licensed under MIT. The project has over 10,500 GitHub stars and receives regular updates with the latest commit activity in March 2026. Configuration is handled through environment variables, making it straightforward to deploy in containerized environments.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imgproxy-high-performance-image-processing-proxy/)
