---
title: "Ghostfolio Open Source Wealth Management and Portfolio Tracking Platform"
description: "Ghostfolio is an open-source wealth management application for tracking stocks, ETFs, and cryptocurrencies across multiple platforms. Built with Angular, NestJS, and Prisma on PostgreSQL, it provides portfolio performance analysis, allocation insights, and data-driven investment decision support."
verification: "security_reviewed"
source: "https://github.com/ghostfolio/ghostfolio"
category:
  - "Integrations & Connectors"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "ghostfolio/ghostfolio"
  github_stars: 8115
---

# Ghostfolio Open Source Wealth Management and Portfolio Tracking Platform

Ghostfolio is an open-source wealth management application designed for individuals who trade stocks, ETFs, or cryptocurrencies across multiple platforms. Built as a modern web application using Angular for the frontend and NestJS with PostgreSQL and Prisma for the backend, it provides comprehensive portfolio tracking and analysis capabilities with a focus on privacy and data ownership.


Portfolio Tracking
Ghostfolio supports multi-account management, allowing you to consolidate holdings from different brokerages into a single view. It tracks portfolio performance with Return on Average Investment (ROAI) metrics across multiple timeframes: Today, Week-to-Date, Month-to-Date, Year-to-Date, 1 Year, 5 Years, and Max. Asset data is fetched from providers like Yahoo Finance and CoinGecko.


Analysis and Insights
The application provides various charts for visualizing portfolio allocation by asset class, currency, sector, and geographic region. Static analysis identifies potential risks in your portfolio such as overconcentration in a single asset or sector. The fire calculator helps estimate financial independence timelines based on current savings rates and portfolio growth.


Import and Export
Transactions can be imported via CSV files from popular brokerages or exported for backup and analysis. The application supports multiple currencies with automatic exchange rate conversion.


Self-Hosting
Ghostfolio provides official Docker images on Docker Hub for linux/amd64, linux/arm/v7, and linux/arm64 architectures. The stack requires PostgreSQL for data storage and Redis for caching. Configuration is managed through environment variables for database connections, API keys, and authentication settings.


Technology Stack
The project is organized as an Nx monorepo with TypeScript throughout. The backend uses NestJS with Prisma ORM for database access. The frontend is built with Angular and Angular Material. The architecture supports OpenID Connect (OIDC) authentication for enterprise SSO integration.


Agent Integration
AI agents can interact with Ghostfolio through its REST API to query portfolio positions, fetch performance metrics, create or update transactions, and generate portfolio analysis reports. This enables automated financial monitoring workflows, periodic portfolio health checks, and data-driven investment insights delivered through agent-powered dashboards.

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ghostfolio-wealth-management-portfolio-tracking/)
