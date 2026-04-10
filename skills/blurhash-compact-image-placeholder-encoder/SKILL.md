---
title: "BlurHash Compact Image Placeholder Encoder"
description: "An agent skill that uses BlurHash, the compact image placeholder representation algorithm by Wolt, to generate and decode tiny hash strings that represent blurred previews of images. Enables instant placeholder rendering in web and mobile applications while full images load."
slug: "blurhash-compact-image-placeholder-encoder"
category:
  - "Image &amp; Creative Automation"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/woltapp/blurhash"
tool_ecosystem:
  github_repo: "woltapp/blurhash"
  github_stars: 16958
  npm_package: "blurhash"
  npm_weekly_downloads: 800290
---

# BlurHash Compact Image Placeholder Encoder

An agent skill that uses BlurHash, the compact image placeholder representation algorithm by Wolt, to generate and decode tiny hash strings that represent blurred previews of images. Enables instant placeholder rendering in web and mobile applications while full images load.

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
clawhub install blurhash-compact-image-placeholder-encoder
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

BlurHash is an algorithm and multi-language library created by Wolt that encodes an image into a short string (typically 20-30 characters) representing a blurred, low-resolution version of that image. This skill integrates BlurHash encoding and decoding into agent workflows for automated placeholder image generation across web and mobile platforms.
Core Capabilities
The skill accepts source images and produces BlurHash strings that can be stored alongside image metadata in databases, APIs, or content management systems. These compact strings decode into smooth gradient approximations of the original image, providing a visually pleasant loading experience instead of blank spaces or spinner icons. The algorithm uses discrete cosine transform (DCT) components to represent color patterns, with configurable X and Y component counts that control the level of detail in the placeholder.
How It Works
When encoding, the skill reads the source image, downsamples it, and computes DCT coefficients across a configurable grid (typically 4×3 components). These coefficients are packed into a base83-encoded string. When decoding, the skill reconstructs pixel data from the hash string at any target resolution, producing smooth gradient images suitable for CSS backgrounds or canvas rendering. The entire encode-decode cycle is deterministic and produces identical results across all platform implementations.
Integration Points
BlurHash integrates into content pipelines as a pre-processing step during image upload. The skill can batch-process image libraries to generate hashes for existing assets, embed hashes in API responses alongside image URLs, and generate inline CSS or SVG representations for server-side rendering. It works with React, React Native, iOS (Swift), Android (Kotlin), and pure JavaScript implementations for client-side decoding.
Technical Details
The reference implementation spans TypeScript, Swift, Kotlin, and Python, with the JavaScript package available on npm as blurhash (version 2.0.5). The project has over 16,900 GitHub stars and is licensed under MIT. The algorithm is designed to produce hashes under 30 bytes, making them efficient to store in database columns alongside other image metadata without significant storage overhead.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/blurhash-compact-image-placeholder-encoder/)
