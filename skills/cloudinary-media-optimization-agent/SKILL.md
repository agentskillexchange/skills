---
name: "Cloudinary Media Optimization Agent"
description: "Automates image and video optimization workflows via the Cloudinary Upload and Admin APIs. Applies responsive breakpoints, format negotiation, and intelligent cropping with gravity detection."
category: "Image &amp; Creative Automation"
framework: "Claude Agents"
verification: security_reviewed
source: "https://agentskillexchange.com/skills/cloudinary-media-optimization-agent/"
---
# Cloudinary Media Optimization Agent

Automates image and video optimization workflows via the Cloudinary Upload and Admin APIs. Applies responsive breakpoints, format negotiation, and intelligent cropping with gravity detection.

The Cloudinary Media Optimization Agent manages automated image and video processing workflows through the Cloudinary Upload API and Admin API. It handles bulk asset optimization with intelligent format selection (AVIF, WebP, JPEG XL) based on browser capability detection.

Responsive image breakpoint generation uses Cloudinary responsive breakpoints API to calculate optimal image widths, generating srcset attributes that minimize bandwidth while maintaining visual quality. The agent configures automatic format (f_auto) and quality (q_auto) transformations for delivery optimization.

Intelligent cropping leverages Cloudinary AI-powered gravity detection modes including g_auto, g_face, and g_custom for content-aware composition. Named transformations are managed programmatically for consistent brand styling across asset libraries.

Video optimization includes adaptive bitrate streaming with HLS and DASH manifest generation, automatic thumbnail extraction, and video-to-GIF conversion for social media assets. The skill supports webhook notifications for asynchronous processing status and integrates with DAM workflows through Cloudinary metadata and structured metadata schemas.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cloudinary-media-optimization-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cloudinary-media-optimization-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cloudinary-media-optimization-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cloudinary-media-optimization-agent -a codex
```

### OpenClaw

```bash
clawhub install cloudinary-media-optimization-agent
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-media-optimization-agent/)
