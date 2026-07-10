---
name: "Inspect BullMQ agent job queues with Bull Board"
slug: "inspect-bullmq-agent-job-queues-with-bull-board"
description: "Use Bull Board to add a protected dashboard for Bull and BullMQ queues so operators can inspect, retry, pause, clean, and debug background agent jobs."
github_stars: 3399
verification: "security_reviewed"
source: "https://github.com/felixmosh/bull-board"
author: "Bull Board contributors"
publisher_type: "open_source"
category: "Monitoring & Alerts"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "felixmosh/bull-board"
  github_stars: 3399
  npm_package: "@bull-board/api"
  npm_weekly_downloads: 1528459
---

# Inspect BullMQ agent job queues with Bull Board

Use Bull Board to add a protected dashboard for Bull and BullMQ queues so operators can inspect, retry, pause, clean, and debug background agent jobs.

## Prerequisites

Bull or BullMQ queues, Redis, Bull Board API/UI package, one supported server adapter such as Express, Fastify, Koa, Hapi, NestJS, Hono, H3, Elysia, or Bun

## Installation

Use the upstream install or setup path that matches your environment:
- npm install @bull-board/api @bull-board/express
- git clone git@github.com:felixmosh/bull-board.git
- yarn && yarn dev:docker && yarn build && yarn dev

Requirements and caveats from upstream:
- const express = require('express');
- const { Queue } = require('bullmq');
- const { createBullBoard } = require('@bull-board/api');

Basic usage or getting-started notes:
- Pick the adapter for your framework:
- js
- const queue = new Queue('emails', { connection: { host: 'localhost', port: 6379 } });

- Source: https://github.com/felixmosh/bull-board
- Extracted from upstream docs: https://raw.githubusercontent.com/felixmosh/bull-board/HEAD/README.md

## Documentation

- https://felixmosh.github.io/bull-board/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/inspect-bullmq-agent-job-queues-with-bull-board/)
