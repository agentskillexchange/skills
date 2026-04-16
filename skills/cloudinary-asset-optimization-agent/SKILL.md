---
title: "Cloudinary Asset Optimization Agent"
description: "Manages image and video assets using the Cloudinary Node.js SDK and Upload API. Applies automatic format selection, responsive breakpoints, and AI-based cropping with face detection."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/cloudinary-asset-optimization-agent/"
category:
  - "Image &amp; Creative Automation"
framework:
  - "OpenClaw"
---

# Cloudinary Asset Optimization Agent

The Cloudinary Asset Optimization Agent automates media asset management using the Cloudinary Node.js SDK for programmatic access to Cloudinary’s image and video transformation pipeline. It leverages the Upload API, Admin API, and URL generation capabilities for comprehensive asset lifecycle management.

The skill configures automatic format selection (f_auto) and quality optimization (q_auto) to deliver optimal file sizes across browsers. It uses the responsive breakpoints API to generate srcset-ready image variants at optimal width intervals determined by content analysis. AI-based cropping leverages Cloudinary’s g_auto and g_face gravity modes for intelligent subject-aware cropping.

Asset workflows include bulk upload with eager transformations, folder-based organization with metadata tagging, and automated backup to secondary storage. The agent generates URL transformation chains for on-the-fly image manipulation including overlays, artistic filters, and background removal using Cloudinary AI. It monitors usage quotas via the Admin API and optimizes transformation caching to reduce credit consumption.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cloudinary-asset-optimization-agent/)
