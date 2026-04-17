---
title: "Appwrite Open Source Backend as a Service Platform"
description: "Overview\nAppwrite is an end-to-end backend platform for building Web, Mobile, Native, and Backend applications. Packaged as a set of Docker microservices, Appwrite abstracts the complexity of building modern backends and provides a unified API for authentication, databases, file storage, cloud functions, messaging, and hosting.\nKey Features\n\nAuthentication: Supports 30+ login methods including email/password, OAuth2, phone, magic links, and anonymous sessions via the Appwrite Auth API\nDatabases: Document-based database with real-time subscriptions, permissions, relationships, and full-text search. Now includes DB operators for advanced querying\nStorage: File storage with built-in image manipulation (crop, resize, rotate), encryption at rest, and antivirus scanning\nCloud Functions: Serverless function execution supporting Node.js, Python, PHP, Ruby, Dart, Swift, Kotlin, and more\nMessaging: Push notifications, email, and SMS delivery through a unified API\nRealtime: WebSocket subscriptions for live updates on any database, storage, or authentication event\nHosting: Built-in static and SSR frontend hosting with automatic SSL\n\nIntegration for AI Agents\nAppwrite provides official SDKs for web (JavaScript), Flutter, Apple (Swift), Android (Kotlin), and server-side (Node.js, Python, PHP, Ruby, Dart, Kotlin, Swift). Agents can use the REST API or any SDK to programmatically manage users, create database documents, upload files, trigger cloud functions, and subscribe to realtime events. The self-hosted nature makes it ideal for agents that need full control over backend infrastructure without vendor lock-in.\nInstallation\nAppwrite runs via Docker with a single command:\ndocker run -it --rm --publish 20080:20080 --volume /var/run/docker.sock:/var/run/docker.sock --volume \"$(pwd)\"/appwrite:/usr/src/code/appwrite:rw --entrypoint=\"install\" appwrite/appwrite:1.9.0\nAlternatively, use Appwrite Cloud for a managed deployment at cloud.appwrite.io."
verification: security_reviewed
source: "https://github.com/appwrite/appwrite"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/appwrite-open-source-backend-as-a-service-platform
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/appwrite-open-source-backend-as-a-service-platform` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/appwrite-open-source-backend-as-a-service-platform/)
