---
name: "WordPress Playground WebAssembly Runtime for In-Browser WordPress"
slug: "wordpress-playground-wasm-runtime"
description: "WordPress Playground runs a full WordPress instance entirely in the browser using WebAssembly-compiled PHP. It enables zero-setup WordPress testing, plugin previews, and interactive demos without any server infrastructure."
github_stars: 1926
verification: "listed"
source: "https://github.com/WordPress/wordpress-playground"
category: "WordPress & CMS"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "WordPress/wordpress-playground"
  github_stars: 1926
---

# WordPress Playground WebAssembly Runtime for In-Browser WordPress

WordPress Playground runs a full WordPress instance entirely in the browser using WebAssembly-compiled PHP. It enables zero-setup WordPress testing, plugin previews, and interactive demos without any server infrastructure.

## Installation

Use the upstream install or setup path that matches your environment:
- npx @wp-playground/cli server --auto-mount
- git clone -b trunk --single-branch --depth 1 --recurse-submodules https://github.com/WordPress/wordpress-playground.git
- npm install
- npm run dev

Requirements and caveats from upstream:
- The best part? You can run it directly using npx, Node.js's package runner. To get started, navigate to your plugin or theme directory and run:
- Any changes you make to .ts files will be live-reloaded. Changes to Dockerfile require a full rebuild.

Basic usage or getting-started notes:
- WordPress Playground has a [live demo](https://developer.wordpress.org/playground/demo/) available.
- You can embed WordPress Playground in your project via an <iframe> – find out how in the [documentation](https://wordpress.github.io/wordpress-playground/). **Note the embed is experimental and may break or change wit...
- You can connect to the Playground using the JavaScript client. Here's an example of how to do it in the browser using an iframe HTML element and the startPlaygroundWeb function from the @wp-playground/client package.

- Source: https://github.com/WordPress/wordpress-playground
- Extracted from upstream docs: https://raw.githubusercontent.com/WordPress/wordpress-playground/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wordpress-playground-wasm-runtime/)
