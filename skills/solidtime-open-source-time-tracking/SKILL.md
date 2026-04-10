---
title: "solidtime Modern Open Source Time Tracking for Freelancers and Agencies"
description: "solidtime is a modern open-source time tracking application built for freelancers and agencies, featuring project and client management, billable rates, task assignment, multi-organization support, and data import from Toggl and Clockify. Self-hostable with Docker."
slug: "solidtime-open-source-time-tracking"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
verification: "security_reviewed"
source: "https://github.com/solidtime-io/solidtime"
---

# solidtime Modern Open Source Time Tracking for Freelancers and Agencies

solidtime is a modern open-source time tracking application built for freelancers and agencies, featuring project and client management, billable rates, task assignment, multi-organization support, and data import from Toggl and Clockify. Self-hostable with Docker.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install solidtime-open-source-time-tracking
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

solidtime is a modern open-source time tracking platform designed specifically for freelancers and agencies who need to track billable hours across projects and clients. Built with Laravel and Vue.js, it offers a polished web interface with 8,000+ GitHub stars and active development under the AGPL-3.0 license.
Core Features
The application provides a full-featured time tracking workflow: start and stop timers, log manual entries, assign time to projects and tasks, and set billable rates at multiple levels (organization, member, project, or project member). Each entry can be tagged with a project, task, client, and billability status. The dashboard shows real-time summaries of tracked hours with filtering by date range, project, and team member.
Project and Client Management
solidtime includes built-in project management with client assignment, budget tracking, and member roles. Projects can have multiple tasks, and each task inherits or overrides the project billable rate. Clients are top-level entities that group related projects. The multi-organization feature lets users switch between separate workspaces (useful for freelancers working with multiple agencies).
Data Portability and Import
Time tracking data can be imported from Toggl, Clockify, and generic CSV Timeentry formats. This makes migration from other platforms straightforward. The REST API provides full programmatic access to all entities — time entries, projects, tasks, clients, and organizations — enabling custom integrations and reporting.
Self-Hosting and Deployment
solidtime is designed for self-hosting with Docker. The official documentation at docs.solidtime.io provides deployment guides for Docker Compose, Coolify, and other platforms. A managed cloud option is available at solidtime.io for teams who prefer not to self-host. The PHP/Laravel backend runs on standard LAMP or containerized stacks, and the Vue.js frontend is served as a single-page application.
Agent Integration
AI agents can interact with solidtime through its REST API to automate time entry creation, generate project reports, calculate billable totals, or sync time data with invoicing systems. The structured API responses make it straightforward to build workflows that bridge time tracking with accounting, project management, or productivity analysis tools.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/solidtime-open-source-time-tracking/)
