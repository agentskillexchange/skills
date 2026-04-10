---
title: "Cloudinary Asset Optimization Agent"
description: "Manages image and video assets using the Cloudinary Node.js SDK and Upload API. Applies automatic format selection, responsive breakpoints, and AI-based cropping with face detection."
slug: "cloudinary-asset-optimization-agent"
category:
  - "Image &amp; Creative Automation"
framework:
  - "OpenClaw"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cloudinary-asset-optimization-agent/"
listed: true
---

# Cloudinary Asset Optimization Agent

Manages image and video assets using the Cloudinary Node.js SDK and Upload API. Applies automatic format selection, responsive breakpoints, and AI-based cropping with face detection.

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
clawhub install cloudinary-asset-optimization-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

The Cloudinary Asset Optimization Agent automates media asset management using the Cloudinary Node.js SDK for programmatic access to Cloudinary’s image and video transformation pipeline. It leverages the Upload API, Admin API, and URL generation capabilities for comprehensive asset lifecycle management.
The skill configures automatic format selection (f_auto) and quality optimization (q_auto) to deliver optimal file sizes across browsers. It uses the responsive breakpoints API to generate srcset-ready image variants at optimal width intervals determined by content analysis. AI-based cropping leverages Cloudinary’s g_auto and g_face gravity modes for intelligent subject-aware cropping.
Asset workflows include bulk upload with eager transformations, folder-based organization with metadata tagging, and automated backup to secondary storage. The agent generates URL transformation chains for on-the-fly image manipulation including overlays, artistic filters, and background removal using Cloudinary AI. It monitors usage quotas via the Admin API and optimizes transformation caching to reduce credit consumption.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-asset-optimization-agent/)
