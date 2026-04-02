---
name: WXT Next-Generation Web Extension Framework for Browser Extensions
description: >-
  WXT is an open-source, next-generation framework for building browser
  extensions. It supports all browsers, both Manifest V2 and V3, and provides
  dev mode with HMR, file-based entrypoints, TypeScript, auto-imports, and
  automated publishing.
version: 1.0.0
category: Developer Tools
source: https://github.com/wxt-dev/wxt
verification: listed
---

# WXT Next-Generation Web Extension Framework

WXT is a modern framework for building web browser extensions that dramatically simplifies the extension development experience with features borrowed from modern web frameworks while handling the complexities of cross-browser extension APIs.

## Developer Experience

WXT provides a Vite-powered dev server with hot module replacement (HMR) and fast reload for extension development. Developers define entrypoints using a file-based routing convention — background scripts, content scripts, popups, options pages, and sidepanels are all discovered automatically from the file structure. TypeScript is supported out of the box with full type inference for browser extension APIs.

## Cross-Browser Support

WXT builds extensions that work across Chrome, Firefox, Safari, Edge, and all Chromium-based browsers. It handles the differences between Manifest V2 and Manifest V3 automatically, allowing developers to target both manifest versions from the same codebase.

## Framework Agnostic

While WXT handles extension-specific concerns (manifest generation, background scripts, content script injection), it is agnostic about the frontend framework used for UI components. Developers can use React, Vue, Svelte, Solid, or plain HTML/CSS for popups, options pages, and side panels.

## Module System

WXT includes a module system for sharing reusable code between extensions. Modules can add entrypoints, modify the build configuration, or inject runtime code.

## Installation

```bash
# npm
npm install wxt

# pnpm
pnpm add wxt

# yarn
yarn add wxt

# bun
bun add wxt
```

Or create a new extension project:

```bash
npx wxt@latest init my-extension
```

## Documentation

- [WXT Documentation](https://wxt.dev)

## Source

- [GitHub](https://github.com/wxt-dev/wxt)
- [Agent Skill Exchange](https://agentskillexchange.com/skills/wxt-next-gen-web-extension-framework/)
