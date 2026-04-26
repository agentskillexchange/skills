---
title: "Cloudinary Asset Optimization Agent"
description: "Manages image and video assets using the Cloudinary Node.js SDK and Upload API. Applies automatic format selection, responsive breakpoints, and AI-based cropping with face detection."
verification: "security_reviewed"
source: "https://cloudinary.com/documentation"
category:
  - "Image & Creative Automation"
framework:
  - "OpenClaw"
---

# Cloudinary Asset Optimization Agent

The Cloudinary Asset Optimization Agent automates media asset management using the Cloudinary Node.js SDK for programmatic access to Cloudinary’s image and video transformation pipeline. It leverages the Upload API, Admin API, and URL generation capabilities for comprehensive asset lifecycle management.

The skill configures automatic format selection (f_auto) and quality optimization (q_auto) to deliver optimal file sizes across browsers. It uses the responsive breakpoints API to generate srcset-ready image variants at optimal width intervals determined by content analysis. AI-based cropping leverages Cloudinary’s g_auto and g_face gravity modes for intelligent subject-aware cropping.

Asset workflows include bulk upload with eager transformations, folder-based organization with metadata tagging, and automated backup to secondary storage. The agent generates URL transformation chains for on-the-fly image manipulation including overlays, artistic filters, and background removal using Cloudinary AI. It monitors usage quotas via the Admin API and optimizes transformation caching to reduce credit consumption.

## Installation

### Method 1, Agent Skill Exchange

- Install from the marketplace listing: https://agentskillexchange.com/skills/cloudinary-asset-optimization-agent/

### Method 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/cloudinary-asset-optimization-agent
```

### Method 3, Download ZIP

- Download the repository ZIP and extract `skills/cloudinary-asset-optimization-agent`.

### Method 4, Manual copy

- Copy this skill folder into your local skills directory, then reload your agent tooling.

### Method 5, Fork and sync

- Fork the repository if you want to maintain local edits while syncing upstream changes.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-asset-optimization-agent/)
