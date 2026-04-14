---
title: "Appwrite Open Source Backend as a Service Platform"
description: "Appwrite is an open-source, self-hosted backend platform that provides authentication, databases, storage, functions, messaging, and realtime APIs out of the box. It serves as a privacy-first alternative to Firebase and Supabase, packaged as Docker microservices for full data ownership."
verification: security_reviewed
source: "https://github.com/appwrite/appwrite"
category:
  - "Integrations &amp; Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "appwrite/appwrite"
  github_stars: 55674
---

# Appwrite Open Source Backend as a Service Platform

Overview
Appwrite is an end-to-end backend platform for building Web, Mobile, Native, and Backend applications. Packaged as a set of Docker microservices, Appwrite abstracts the complexity of building modern backends and provides a unified API for authentication, databases, file storage, cloud functions, messaging, and hosting.

Key Features

Authentication: Supports 30+ login methods including email/password, OAuth2, phone, magic links, and anonymous sessions via the Appwrite Auth API
Databases: Document-based database with real-time subscriptions, permissions, relationships, and full-text search. Now includes DB operators for advanced querying
Storage: File storage with built-in image manipulation (crop, resize, rotate), encryption at rest, and antivirus scanning
Cloud Functions: Serverless function execution supporting Node.js, Python, PHP, Ruby, Dart, Swift, Kotlin, and more
Messaging: Push notifications, email, and SMS delivery through a unified API
Realtime: WebSocket subscriptions for live updates on any database, storage, or authentication event
Hosting: Built-in static and SSR frontend hosting with automatic SSL

Integration for AI Agents
Appwrite provides official SDKs for web (JavaScript), Flutter, Apple (Swift), Android (Kotlin), and server-side (Node.js, Python, PHP, Ruby, Dart, Kotlin, Swift). Agents can use the REST API or any SDK to programmatically manage users, create database documents, upload files, trigger cloud functions, and subscribe to realtime events. The self-hosted nature makes it ideal for agents that need full control over backend infrastructure without vendor lock-in.

Installation
Appwrite runs via Docker with a single command:

docker run -it --rm --publish 20080:20080 --volume /var/run/docker.sock:/var/run/docker.sock --volume "$(pwd)"/appwrite:/usr/src/code/appwrite:rw --entrypoint="install" appwrite/appwrite:1.9.0
Alternatively, use Appwrite Cloud for a managed deployment at cloud.appwrite.io.

## Installation

Choose the setup that fits your environment:

1. **OpenClaw skill installer**
   - Add this skill through your OpenClaw skills workflow if you use managed installs.
2. **Git clone**
   - Clone the upstream project or skill repo, then follow its setup instructions.
3. **Package manager**
   - Install with the ecosystem package manager when the upstream project publishes one.
4. **Manual copy**
   - Copy the skill folder into your local skills directory and reload your agent.
5. **Container or CI environment**
   - Bake the dependency into your image or automation environment before running the skill.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/appwrite-open-source-backend-as-a-service-platform/)
