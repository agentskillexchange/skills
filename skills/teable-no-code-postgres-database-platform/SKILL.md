---
name: Teable No-Code Postgres Database Platform and Airtable Alternative
description: Teable is an open source no-code database platform built on PostgreSQL
  that uses a spreadsheet-like interface for creating powerful database applications.
  It supports real-time collaboration, scales to millions of rows, and provides a
  REST API for programmatic access.
verification: security_reviewed
source: https://github.com/teableio/teable
category:
- Data Extraction &amp; Transformation
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: teableio/teable
  github_stars: 21084
---
# Teable No-Code Postgres Database Platform and Airtable Alternative

Teable is an open source, high-performance no-code database platform that combines the familiarity of a spreadsheet interface with the power of PostgreSQL underneath. Positioned as a next-generation Airtable alternative, Teable enables teams to build database applications without writing code while maintaining the full capabilities of a relational database.
Core Features
Teable provides a comprehensive set of database features through its visual interface: custom column types, formula support, filtering, sorting, grouping, aggregation, validation, and batch editing. It supports attachments, comments, field conversion between types, and full undo/redo history. The platform handles millions of rows efficiently, making it suitable for production workloads that exceed typical no-code platform limits.
Multiple Views
Data can be visualized through multiple view types: Grid View (spreadsheet-style), Form View (data entry), Kanban View (board-style), Gallery View (card-based), and Calendar View (time-based). Each view provides a different perspective on the same underlying data, and users can create multiple views per table.
API and Integration
Teable exposes a REST API for programmatic access to all database operations. Agents can create tables, define fields, insert and query records, manage views, and automate workflows through the API. The platform also supports SQL queries directly against the underlying PostgreSQL database, providing maximum flexibility for data operations.
Self-Hosting and Deployment
Teable is built with Next.js (frontend) and NestJS (backend) on top of PostgreSQL. It can be self-hosted via Docker Compose or deployed to platforms like Railway. The core packages are MIT licensed while the application layer uses AGPL 3.0. Teable supports plugins for extensibility and includes built-in charting capabilities.
Agent Use Cases
AI agents can use Teable as a structured data backend for managing project data, tracking workflows, building internal tools, or creating custom databases. Its API enables automated data entry, report generation, and integration with other services in agent workflows.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/teable-no-code-postgres-database-platform/)
