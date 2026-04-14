---
title: "Planka Self-Hosted Kanban Board for Project Management"
description: "Planka is an elegant, self-hosted Kanban-style project management tool and open-source Trello alternative. With 11,000+ GitHub stars and 35+ language translations, it provides real-time collaborative boards, markdown support, drag-and-drop task management, and OpenID Connect SSO."
verification: security_reviewed
source: "https://github.com/plankanban/planka"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "plankanban/planka"
  github_stars: 11822
---

# Planka Self-Hosted Kanban Board for Project Management

Planka is a self-hosted, Kanban-style project management platform designed as a lightweight, privacy-respecting alternative to Trello and similar SaaS tools. With over 11,000 GitHub stars, active development (last commit April 2026), and a growing community of contributors, Planka has established itself as one of the leading open-source project management solutions.

Core Features
Planka provides collaborative Kanban boards with real-time synchronization across all connected users — no manual refresh needed. Teams can create projects, boards, lists, and cards with an intuitive drag-and-drop interface. Card descriptions support rich Markdown formatting through a built-in editor. The notification system integrates with over 100 providers, making it flexible enough for any team workflow.

Authentication and Deployment
Planka supports single sign-on via OpenID Connect integration, making it enterprise-ready. Deployment is straightforward with Docker Compose, and the platform includes full internationalization support with 35+ languages. The project offers both a Community edition under a Fair Use License and a Pro edition with additional features.

Agent Integration Points
AI agents can interact with Planka through its REST API to automate project management workflows: creating boards and cards from issue trackers, moving cards through pipeline stages based on CI/CD events, assigning tasks based on team availability, and generating project status reports. The Docker-based deployment makes it easy to spin up alongside other agent infrastructure.

Technical Stack
Built with React on the frontend and Node.js on the backend, Planka uses PostgreSQL for data storage. The real-time sync is powered by WebSockets. Installation requires Docker and Docker Compose:

docker-compose up -d
Configuration is managed through environment variables, with detailed documentation available at docs.planka.cloud.

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/planka-self-hosted-kanban-board-project-management/)
