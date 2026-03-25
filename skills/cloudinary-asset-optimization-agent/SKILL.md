---
name: "Cloudinary Asset Optimization Agent"
description: "Manages image and video assets using the Cloudinary Node.js SDK and Upload API. Applies automatic format selection, responsive breakpoints, and AI-based cropping with face detection."
category: "Image & Creative Automation"
framework: "OpenClaw"
verification: security_reviewed  # security_reviewed or listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/cloudinary-asset-optimization-agent/"
---

# Cloudinary Asset Optimization Agent

Manages image and video assets using the Cloudinary Node.js SDK and Upload API. Applies automatic format selection, responsive breakpoints, and AI-based cropping with face detection.

## Overview

The Cloudinary Asset Optimization Agent automates media asset management using the Cloudinary Node.js SDK for programmatic access to Cloudinary’s image and video transformation pipeline. It leverages the Upload API, Admin API, and URL generation capabilities for comprehensive asset lifecycle management.

The skill configures automatic format selection (f_auto) and quality optimization (q_auto) to deliver optimal file sizes across browsers. It uses the responsive breakpoints API to generate srcset-ready image variants at optimal width intervals determined by content analysis. AI-based cropping leverages Cloudinary’s g_auto and g_face gravity modes for intelligent subject-aware cropping.

Asset workflows include bulk upload with eager transformations, folder-based organization with metadata tagging, and automated backup to secondary storage. The agent generates URL transformation chains for on-the-fly image manipulation including overlays, artistic filters, and background removal using Cloudinary AI. It monitors usage quotas via the Admin API and optimizes transformation caching to reduce credit consumption.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill cloudinary-asset-optimization-agent
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill cloudinary-asset-optimization-agent -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill cloudinary-asset-optimization-agent -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill cloudinary-asset-optimization-agent -a codex
```

### OpenClaw

```bash
clawhub install cloudinary-asset-optimization-agent
```

## Source

- Marketplace: https://agentskillexchange.com/skills/cloudinary-asset-optimization-agent/
