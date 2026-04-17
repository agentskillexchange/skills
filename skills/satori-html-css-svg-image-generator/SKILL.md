---
title: "Satori HTML and CSS to SVG Image Generator by Vercel"
description: "Overview\nSatori is an enlightened library created by Vercel that converts HTML and CSS into SVG format. It is the engine behind Vercel’s @vercel/og Open Graph image generation service, enabling developers to create dynamic, beautifully styled images from markup without running a headless browser. Satori runs in Node.js, Deno, and the browser via WebAssembly, making it one of the most versatile image generation solutions available.\nHow It Works\nSatori takes a React-like JSX element tree (or HTML via satori-html) and a configuration object specifying dimensions and fonts, then renders the layout using its own CSS engine. It supports the full Flexbox specification, common text styling properties (fonts, colors, line-height, letter-spacing), background images and gradients, border radius, box shadows, and more. The output is a clean SVG string that can be converted to PNG using resvg-js or other SVG rasterizers.\nKey Features\n\nJSX-to-SVG rendering: Write image templates as JSX components with full CSS Flexbox\nCustom font loading: Load .ttf/.otf fonts for brand-consistent typography\nEmoji support: Built-in Twemoji and OpenMoji rendering\nMulti-language text: CJK, Arabic, Thai, Devanagari with automatic text segmentation\nEdge-compatible: Runs on Edge Runtime, Cloudflare Workers, and Deno Deploy\nNo headless browser: Pure layout engine — fast, lightweight, deterministic output\nDynamic image generation: Perfect for OG images, social cards, certificates, receipts\n\nAgent Integration\nAI agents can use Satori to programmatically generate branded images from data: creating Open Graph cards for blog posts, generating social media preview images from article metadata, building visual report cards, or producing dynamic certificate and badge images. The JSX API makes it natural to template images using variables extracted from content.\nInstallation\nnpm install satori\nFor PNG output: npm install @resvg/resvg-js. For HTML input: npm install satori-html\nQuick Example\nimport satori from \"satori\";\nconst svg = await satori(\n  { type: \"div\", props: { style: { display: \"flex\", fontSize: 40 }, children: \"Hello World\" } },\n  { width: 1200, height: 630, fonts: [{ name: \"Inter\", data: fontBuffer }] }\n);"
verification: security_reviewed
source: "https://github.com/vercel/satori"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "vercel/satori"
  github_stars: 13234
---

# Satori HTML and CSS to SVG Image Generator by Vercel

Overview
Satori is an enlightened library created by Vercel that converts HTML and CSS into SVG format. It is the engine behind Vercel’s @vercel/og Open Graph image generation service, enabling developers to create dynamic, beautifully styled images from markup without running a headless browser. Satori runs in Node.js, Deno, and the browser via WebAssembly, making it one of the most versatile image generation solutions available.
How It Works
Satori takes a React-like JSX element tree (or HTML via satori-html) and a configuration object specifying dimensions and fonts, then renders the layout using its own CSS engine. It supports the full Flexbox specification, common text styling properties (fonts, colors, line-height, letter-spacing), background images and gradients, border radius, box shadows, and more. The output is a clean SVG string that can be converted to PNG using resvg-js or other SVG rasterizers.
Key Features

JSX-to-SVG rendering: Write image templates as JSX components with full CSS Flexbox
Custom font loading: Load .ttf/.otf fonts for brand-consistent typography
Emoji support: Built-in Twemoji and OpenMoji rendering
Multi-language text: CJK, Arabic, Thai, Devanagari with automatic text segmentation
Edge-compatible: Runs on Edge Runtime, Cloudflare Workers, and Deno Deploy
No headless browser: Pure layout engine — fast, lightweight, deterministic output
Dynamic image generation: Perfect for OG images, social cards, certificates, receipts

Agent Integration
AI agents can use Satori to programmatically generate branded images from data: creating Open Graph cards for blog posts, generating social media preview images from article metadata, building visual report cards, or producing dynamic certificate and badge images. The JSX API makes it natural to template images using variables extracted from content.
Installation
npm install satori
For PNG output: npm install @resvg/resvg-js. For HTML input: npm install satori-html
Quick Example
import satori from "satori";
const svg = await satori(
  { type: "div", props: { style: { display: "flex", fontSize: 40 }, children: "Hello World" } },
  { width: 1200, height: 630, fonts: [{ name: "Inter", data: fontBuffer }] }
);

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/satori-html-css-svg-image-generator
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/satori-html-css-svg-image-generator` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/satori-html-css-svg-image-generator/)
