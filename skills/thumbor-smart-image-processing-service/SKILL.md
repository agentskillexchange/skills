---
title: "Thumbor Smart Image Processing Service"
description: "Thumbor is an open-source smart imaging service created by Globo.com that provides on-demand crop, resizing, and flipping of images through a URL-based API. This skill integrates Thumbor into agent workflows, enabling automated image transformation pipelines without manual intervention.\nCore Capabilities\nThe skill wraps Thumbor’s HTTP API to handle smart cropping with face and feature detection, dynamic resizing with aspect ratio preservation, image format conversion between JPEG, PNG, WebP and AVIF, and filter chains including blur, watermark, brightness, contrast, and grayscale adjustments. Thumbor’s smart detection algorithms use OpenCV to identify faces and points of interest, ensuring that automated crops preserve the most important visual elements.\nHow It Works\nAgents construct Thumbor-compatible URLs that specify the target dimensions, smart cropping preferences, and any filters to apply. The skill validates URL parameters, manages security hashing with HMAC-SHA1 to prevent URL tampering, and handles error responses from the Thumbor server. It supports both unsafe mode for development and secured URLs for production deployments.\nIntegration Points\nThe skill connects to self-hosted Thumbor instances running via Docker or direct Python installation from PyPI. It integrates with content management systems by transforming uploaded images on the fly, feeds into CDN workflows for responsive image generation, and supports batch processing for bulk image libraries. Thumbor’s loader and storage backends allow pulling source images from S3, HTTP origins, or local filesystems.\nTechnical Details\nThumbor is written in Python, distributed on PyPI as the thumbor package (latest version 7.7.7), and licensed under MIT. The project has over 10,000 GitHub stars and is actively maintained with commits in 2026. It supports custom detectors, filters, and storage backends through a plugin architecture. The skill outputs optimized image URLs, processing metadata, and can return base64-encoded image data for inline embedding."
verification: security_reviewed
source: "https://github.com/thumbor/thumbor"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "thumbor/thumbor"
  github_stars: 10470
---

# Thumbor Smart Image Processing Service

Thumbor is an open-source smart imaging service created by Globo.com that provides on-demand crop, resizing, and flipping of images through a URL-based API. This skill integrates Thumbor into agent workflows, enabling automated image transformation pipelines without manual intervention.
Core Capabilities
The skill wraps Thumbor’s HTTP API to handle smart cropping with face and feature detection, dynamic resizing with aspect ratio preservation, image format conversion between JPEG, PNG, WebP and AVIF, and filter chains including blur, watermark, brightness, contrast, and grayscale adjustments. Thumbor’s smart detection algorithms use OpenCV to identify faces and points of interest, ensuring that automated crops preserve the most important visual elements.
How It Works
Agents construct Thumbor-compatible URLs that specify the target dimensions, smart cropping preferences, and any filters to apply. The skill validates URL parameters, manages security hashing with HMAC-SHA1 to prevent URL tampering, and handles error responses from the Thumbor server. It supports both unsafe mode for development and secured URLs for production deployments.
Integration Points
The skill connects to self-hosted Thumbor instances running via Docker or direct Python installation from PyPI. It integrates with content management systems by transforming uploaded images on the fly, feeds into CDN workflows for responsive image generation, and supports batch processing for bulk image libraries. Thumbor’s loader and storage backends allow pulling source images from S3, HTTP origins, or local filesystems.
Technical Details
Thumbor is written in Python, distributed on PyPI as the thumbor package (latest version 7.7.7), and licensed under MIT. The project has over 10,000 GitHub stars and is actively maintained with commits in 2026. It supports custom detectors, filters, and storage backends through a plugin architecture. The skill outputs optimized image URLs, processing metadata, and can return base64-encoded image data for inline embedding.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/thumbor-smart-image-processing-service
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/thumbor-smart-image-processing-service` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/thumbor-smart-image-processing-service/)
