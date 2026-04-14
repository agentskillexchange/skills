---
title: "solidtime Modern Open Source Time Tracking for Freelancers and Agencies"
description: "solidtime is a modern open-source time tracking application built for freelancers and agencies, featuring project and client management, billable rates, task assignment, multi-organization support, and data import from Toggl and Clockify. Self-hostable with Docker."
verification: security_reviewed
source: "https://github.com/solidtime-io/solidtime"
category:
  - "Calendar, Email &amp; Productivity"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "solidtime-io/solidtime"
  github_stars: 8399
---

# solidtime Modern Open Source Time Tracking for Freelancers and Agencies

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

- [Agent Skill Exchange](https://agentskillexchange.com/skills/solidtime-open-source-time-tracking/)
