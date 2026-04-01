---
name: "Wasp Batteries-Included Full-Stack Web Framework for React and Node.js"
description: "Wasp is a Rails-like full-stack web framework that uses a declarative DSL to generate React and Node.js applications with built-in auth, background jobs, email sending, and one-command deployment. Build production-ready apps in a fraction of the time by abstracting away boilerplate while retainin..."
category: "Developer Tools"
framework: "Multi-Framework"
verification: "listed"
source: "https://github.com/wasp-lang/wasp"
---

# Wasp Batteries-Included Full-Stack Web Framework for React and Node.js

## Overview

Wasp (Web Application Specification) is an open-source, batteries-included full-stack framework for building modern web applications with React, Node.js, and Prisma. It introduces a high-level declarative DSL (.wasp files) that describes the structure of your app — routes, pages, auth, background jobs, email — while you write your actual business logic in standard TypeScript/JavaScript.

## How It Works

Wasp uses a compiler-based approach: you define your application spec in a concise .wasp configuration file, and the Wasp compiler generates the entire full-stack codebase. The generated code includes a React frontend, an Express.js backend, and Prisma ORM for database access. You write your custom logic in .ts/.tsx files that the .wasp file references.

## Key Features

- **Full-stack authentication** — Email/password, Google, GitHub, and Keycloak auth out of the box with session management.
- **Type-safe RPC** — Client-server operations (queries and actions) with automatic cache invalidation and end-to-end TypeScript type safety.
- **Background jobs** — Declarative job definitions backed by pg-boss, with retry logic and scheduling.
- **Email sending** — Built-in email integration with Mailgun, SendGrid, or SMTP providers.
- **One-command deployment** — Deploy to Fly.io or Railway with `wasp deploy`.
- **AI-ready by design** — The structured DSL gives AI coding agents clear guardrails and architecture awareness.

## Agent Integration

Agents can use Wasp to scaffold and generate complete web applications from a specification. The declarative .wasp file format is particularly well-suited for AI-assisted development: an agent can generate the app spec, implement the referenced TypeScript modules, and deploy — all through CLI commands. The `wasp new`, `wasp start`, `wasp db migrate-dev`, and `wasp deploy` commands form a complete workflow from ideation to production.

## Installation

`curl -sSL https://get.wasp-lang.dev/installer.sh | sh`

## Requirements

Node.js 18+. Wasp CLI installs as a standalone binary.

## Installation

Install this skill using one of these methods:

```bash
# ClawHub
clawhub install wasp-full-stack-web-framework

# OpenClaw CLI
openclaw skills install wasp-full-stack-web-framework

# Git
git clone https://github.com/agentskillexchange/skills.git
cp -r skills/skills/wasp-full-stack-web-framework ~/.openclaw/workspace/skills/

# Manual download
# Download from: https://agentskillexchange.com/skills/wasp-full-stack-web-framework/
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/wasp-full-stack-web-framework/)
