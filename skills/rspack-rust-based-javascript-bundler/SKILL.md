---
title: Rspack High-Performance Rust-Based JavaScript Bundler
description: 'What is Rspack? Rspack is a high-performance web bundler built in Rust
  by the ByteDance web-infra team. It implements a modernized version of the webpack
  API, allowing teams to migrate from webpack with minimal configuration changes while
  gaining 5-10x faster build speeds. With over 12,500 GitHub stars, Rspack has become
  one of the most adopted next-generation bundlers in the JavaScript ecosystem. Core
  Capabilities The @rspack/core and @rspack/cli npm packages provide a complete bundling
  solution. Rspack supports JavaScript, TypeScript, JSX, CSS, CSS Modules, and asset
  handling out of the box. Its built-in incremental compilation mechanism delivers
  lightning-fast Hot Module Replacement (HMR), making it capable of handling large-scale
  projects with thousands of modules. The bundler supports code splitting, tree shaking,
  minification, and all standard optimization techniques expected of a production
  bundler. Webpack Compatibility Rspack is designed as a webpack-compatible replacement.
  It supports webpack loaders (babel-loader, sass-loader, etc.) and a growing number
  of webpack plugins. Configuration files follow the same schema as webpack.config.js,
  with the rspack.config.js entry point. Teams can migrate incrementally by swapping
  the bundler while keeping their existing loader and plugin configurations largely
  intact. Module Federation Rspack provides first-class support for Module Federation,
  the micro-frontend architecture pattern. This enables multiple independently deployed
  applications to share modules at runtime, making it a strong choice for large organizations
  with distributed frontend teams. Installation and Usage Install via npm: npm install
  -D @rspack/core @rspack/cli . Create an rspack.config.js (or .ts ) configuration
  file and run npx rspack build for production builds or npx rspack serve for the
  development server. The Rspack ecosystem also includes Rsbuild (a higher-level build
  tool), Rspress (a static site generator), and Rslib (a library bundler). Agent Integration
  AI agents use Rspack for scaffolding new web projects with fast build tooling, migrating
  existing webpack projects to Rspack for performance gains, and configuring Module
  Federation setups for micro-frontend architectures. The webpack-compatible API means
  agents can apply their existing webpack knowledge directly.'
verification: security_reviewed
source: https://github.com/web-infra-dev/rspack
category:
- Developer Tools
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: web-infra-dev/rspack
  github_stars: 12599
---

# Rspack High-Performance Rust-Based JavaScript Bundler

What is Rspack? Rspack is a high-performance web bundler built in Rust by the ByteDance web-infra team. It implements a modernized version of the webpack API, allowing teams to migrate from webpack with minimal configuration changes while gaining 5-10x faster build speeds. With over 12,500 GitHub stars, Rspack has become one of the most adopted next-generation bundlers in the JavaScript ecosystem. Core Capabilities The @rspack/core and @rspack/cli npm packages provide a complete bundling solution. Rspack supports JavaScript, TypeScript, JSX, CSS, CSS Modules, and asset handling out of the box. Its built-in incremental compilation mechanism delivers lightning-fast Hot Module Replacement (HMR), making it capable of handling large-scale projects with thousands of modules. The bundler supports code splitting, tree shaking, minification, and all standard optimization techniques expected of a production bundler. Webpack Compatibility Rspack is designed as a webpack-compatible replacement. It supports webpack loaders (babel-loader, sass-loader, etc.) and a growing number of webpack plugins. Configuration files follow the same schema as webpack.config.js, with the rspack.config.js entry point. Teams can migrate incrementally by swapping the bundler while keeping their existing loader and plugin configurations largely intact. Module Federation Rspack provides first-class support for Module Federation, the micro-frontend architecture pattern. This enables multiple independently deployed applications to share modules at runtime, making it a strong choice for large organizations with distributed frontend teams. Installation and Usage Install via npm: npm install -D @rspack/core @rspack/cli . Create an rspack.config.js (or .ts ) configuration file and run npx rspack build for production builds or npx rspack serve for the development server. The Rspack ecosystem also includes Rsbuild (a higher-level build tool), Rspress (a static site generator), and Rslib (a library bundler). Agent Integration AI agents use Rspack for scaffolding new web projects with fast build tooling, migrating existing webpack projects to Rspack for performance gains, and configuring Module Federation setups for micro-frontend architectures. The webpack-compatible API means agents can apply their existing webpack knowledge directly.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/rspack-rust-based-javascript-bundler/)
