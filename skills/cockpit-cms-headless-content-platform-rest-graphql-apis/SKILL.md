---
name: Cockpit CMS Headless Content Platform with REST and GraphQL APIs
description: Cockpit CMS is a lightweight headless content platform for teams that
  want flexible models, REST and GraphQL APIs, and self-hosted deployment without
  a heavy stack. It supports websites, apps, and multi-language content workflows
  with either SQLite or MongoDB backends.
verification: security_reviewed
source: https://github.com/Cockpit-HQ/Cockpit
category:
- WordPress &amp; CMS
framework:
- Multi-Framework
---
# Cockpit CMS Headless Content Platform with REST and GraphQL APIs

Cockpit CMS is a self-hosted headless content platform maintained by Cockpit-HQ. The project focuses on a practical setup for structured content, API delivery, and lightweight administration rather than an all-in-one page-builder model. That makes it appealing when a team wants a content backend for a custom frontend, mobile app, dashboard, or multi-channel publishing workflow.
The upstream README positions Cockpit around collections, singletons, trees, REST APIs, GraphQL support, multilingual content, and deploy-anywhere ownership of data. It also offers a small-footprint operational model, with SQLite or MongoDB storage and Docker-based setup options. For agents and developers, that translates into a clear job-to-be-done: define content models, expose them through APIs, and let separate clients consume the result. It is especially useful for projects that need a headless CMS without committing to a larger enterprise framework.
This candidate passes intake because the official GitHub repository is live, the project has published documentation at getcockpit.com, and the repo shows recent maintenance activity with hundreds of stars. The official quick-start includes a Docker run command for local deployment, which is a concrete integration point for operators. For ASE, Cockpit is a real upstream tool with a distinct CMS use case, strong enough evidence, and no exact existing title match in the current catalog.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/cockpit-cms-headless-content-platform-rest-graphql-apis/)
