---
title: "imgproxy High-Performance Image Processing Proxy"
description: "imgproxy is a standalone, high-performance image processing server written in Go that uses libvips under the hood for fast, memory-efficient image operations. This skill enables agents to generate optimized image variants through URL-based processing directives without touching the original source files.\nCore Capabilities\nThe skill constructs imgproxy-compatible processing URLs that specify resize dimensions, crop gravity, output format, quality level, and advanced operations like watermarking, blurring, sharpening, and rotation. imgproxy handles automatic format negotiation, serving WebP or AVIF to browsers that support them while falling back to JPEG or PNG for older clients. It supports processing pipelines that chain multiple operations in a single request.\nHow It Works\nAgents provide a source image URL and the desired transformations. The skill builds a signed processing URL using HMAC-based signature verification to prevent unauthorized usage. imgproxy fetches the source image, applies the transformation pipeline, and returns the processed result. The server supports streaming responses and concurrent processing, handling thousands of image operations per second on modest hardware.\nSecurity and Performance\nAll processing URLs are cryptographically signed to prevent abuse. imgproxy runs in a Docker container with minimal attack surface and supports allowlisting source domains. The libvips engine processes images in constant memory regardless of image size, avoiding the memory spikes common with ImageMagick-based solutions. It supports reading from local storage, S3, Google Cloud Storage, and Azure Blob Storage.\nIntegration Points\nThe skill integrates with CDN edge workers for dynamic image optimization, content management systems for responsive image generation, and e-commerce platforms for product image processing. imgproxy supports JPEG, PNG, WebP, AVIF, GIF, ICO, SVG, HEIC, BMP, and TIFF formats for both input and output.\nTechnical Details\nimgproxy is written in Go, distributed as Docker images and pre-built binaries, and licensed under MIT. The project has over 10,500 GitHub stars and receives regular updates with the latest commit activity in March 2026. Configuration is handled through environment variables, making it straightforward to deploy in containerized environments."
verification: security_reviewed
source: "https://github.com/imgproxy/imgproxy"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "imgproxy/imgproxy"
  github_stars: 10554
---

# imgproxy High-Performance Image Processing Proxy

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

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/imgproxy-high-performance-image-processing-proxy
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/imgproxy-high-performance-image-processing-proxy` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/imgproxy-high-performance-image-processing-proxy/)
