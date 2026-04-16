---
title: "Swagger UI Documentation Deployer"
description: "Deploys interactive Swagger UI documentation sites from OpenAPI specs with custom branding, authentication presets, and CDN-hosted static builds. Integrates with Redoc for alternative rendering."
verification: "security_reviewed"
source: "https://github.com/swagger-api/swagger-ui"
category:
  - "Library &amp; API Reference"
framework:
  - "OpenClaw"
tool_ecosystem:
  github_repo: "swagger-api/swagger-ui"
  github_stars: 28751
  ase_npm_package: "swagger-ui"
  npm_weekly_downloads: 149194
  license: "Apache-2.0"
---

# Swagger UI Documentation Deployer

This skill deploys interactive API documentation portals using Swagger UI and Redoc from OpenAPI specification files. It configures Swagger UI with custom branding including logos, color schemes, and typography matching organizational design systems. Authentication preset configuration enables Try It Out functionality with pre-populated API keys, OAuth2 client credentials, and JWT tokens for developer testing. The deployer generates static HTML builds suitable for CDN hosting on S3, CloudFront, or GitHub Pages with proper cache headers and content security policies. Multiple spec versions are supported through a version selector dropdown with automatic redirect from latest paths. The skill embeds custom CSS and JavaScript plugins for enhanced functionality including request history, response diffing, and webhook simulation. Redoc integration provides an alternative three-panel layout with nested schema visualization. Search functionality indexes endpoint descriptions, parameter names, and schema properties for quick navigation. Analytics integration tracks endpoint usage patterns to identify popular and underutilized API surfaces.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/swagger-ui-documentation-deployer/)
