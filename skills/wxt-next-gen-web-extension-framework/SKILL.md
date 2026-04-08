---
title: WXT Next-Generation Web Extension Framework for Browser Extensions
description: 'WXT is a modern framework for building web browser extensions, created
  by Aaron Klinker (@aklinker1). It dramatically simplifies the extension development
  experience with features borrowed from modern web frameworks while handling the
  complexities of cross-browser extension APIs. Developer Experience WXT provides
  a Vite-powered dev server with hot module replacement (HMR) and fast reload for
  extension development. Developers define entrypoints using a file-based routing
  convention — background scripts, content scripts, popups, options pages, and sidepanels
  are all discovered automatically from the file structure. TypeScript is supported
  out of the box with full type inference for browser extension APIs. Cross-Browser
  Support WXT builds extensions that work across Chrome, Firefox, Safari, Edge, and
  all Chromium-based browsers. It handles the differences between Manifest V2 and
  Manifest V3 automatically, allowing developers to target both manifest versions
  from the same codebase. This is particularly valuable during the ongoing MV2 to
  MV3 transition period. Framework Agnostic While WXT handles extension-specific concerns
  (manifest generation, background scripts, content script injection), it is agnostic
  about the frontend framework used for UI components. Developers can use React, Vue,
  Svelte, Solid, or plain HTML/CSS for popups, options pages, and side panels. Official
  starter templates are available for each framework. Module System WXT includes a
  module system for sharing reusable code between extensions. Modules can add entrypoints,
  modify the build configuration, or inject runtime code. The community has published
  modules for common patterns like storage synchronization, analytics, and permission
  management. Build and Publishing The build system generates optimized extension
  packages for each target browser. WXT includes built-in commands for zipping extensions
  for store submission and supports automated publishing workflows. Bundle analysis
  tools help developers understand and optimize their extension size. The project
  has over 9,000 GitHub stars and is actively maintained under the MIT license. Getting
  Started Bootstrap a new project with: npx wxt@latest init . The CLI walks through
  framework selection, TypeScript configuration, and creates a ready-to-develop project
  structure. Documentation is available at wxt.dev with comprehensive guides for every
  feature.'
verification: security_reviewed
source: https://github.com/wxt-dev/wxt
category:
- Developer Tools
framework:
- Custom Agents
tool_ecosystem:
  github_repo: wxt-dev/wxt
  github_stars: 9534
---

# WXT Next-Generation Web Extension Framework for Browser Extensions

WXT is a modern framework for building web browser extensions, created by Aaron Klinker (@aklinker1). It dramatically simplifies the extension development experience with features borrowed from modern web frameworks while handling the complexities of cross-browser extension APIs. Developer Experience WXT provides a Vite-powered dev server with hot module replacement (HMR) and fast reload for extension development. Developers define entrypoints using a file-based routing convention — background scripts, content scripts, popups, options pages, and sidepanels are all discovered automatically from the file structure. TypeScript is supported out of the box with full type inference for browser extension APIs. Cross-Browser Support WXT builds extensions that work across Chrome, Firefox, Safari, Edge, and all Chromium-based browsers. It handles the differences between Manifest V2 and Manifest V3 automatically, allowing developers to target both manifest versions from the same codebase. This is particularly valuable during the ongoing MV2 to MV3 transition period. Framework Agnostic While WXT handles extension-specific concerns (manifest generation, background scripts, content script injection), it is agnostic about the frontend framework used for UI components. Developers can use React, Vue, Svelte, Solid, or plain HTML/CSS for popups, options pages, and side panels. Official starter templates are available for each framework. Module System WXT includes a module system for sharing reusable code between extensions. Modules can add entrypoints, modify the build configuration, or inject runtime code. The community has published modules for common patterns like storage synchronization, analytics, and permission management. Build and Publishing The build system generates optimized extension packages for each target browser. WXT includes built-in commands for zipping extensions for store submission and supports automated publishing workflows. Bundle analysis tools help developers understand and optimize their extension size. The project has over 9,000 GitHub stars and is actively maintained under the MIT license. Getting Started Bootstrap a new project with: npx wxt@latest init . The CLI walks through framework selection, TypeScript configuration, and creates a ready-to-develop project structure. Documentation is available at wxt.dev with comprehensive guides for every feature.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wxt-next-gen-web-extension-framework/)
