---
title: "Ghostfolio Open Source Wealth Management and Portfolio Tracking Platform"
description: "Ghostfolio is an open-source wealth management application designed for individuals who trade stocks, ETFs, or cryptocurrencies across multiple platforms. Built as a modern web application using Angular for the frontend and NestJS with PostgreSQL and Prisma for the backend, it provides comprehensive portfolio tracking and analysis capabilities with a focus on privacy and data ownership.\nPortfolio Tracking\nGhostfolio supports multi-account management, allowing you to consolidate holdings from different brokerages into a single view. It tracks portfolio performance with Return on Average Investment (ROAI) metrics across multiple timeframes: Today, Week-to-Date, Month-to-Date, Year-to-Date, 1 Year, 5 Years, and Max. Asset data is fetched from providers like Yahoo Finance and CoinGecko.\nAnalysis and Insights\nThe application provides various charts for visualizing portfolio allocation by asset class, currency, sector, and geographic region. Static analysis identifies potential risks in your portfolio such as overconcentration in a single asset or sector. The fire calculator helps estimate financial independence timelines based on current savings rates and portfolio growth.\nImport and Export\nTransactions can be imported via CSV files from popular brokerages or exported for backup and analysis. The application supports multiple currencies with automatic exchange rate conversion.\nSelf-Hosting\nGhostfolio provides official Docker images on Docker Hub for linux/amd64, linux/arm/v7, and linux/arm64 architectures. The stack requires PostgreSQL for data storage and Redis for caching. Configuration is managed through environment variables for database connections, API keys, and authentication settings.\nTechnology Stack\nThe project is organized as an Nx monorepo with TypeScript throughout. The backend uses NestJS with Prisma ORM for database access. The frontend is built with Angular and Angular Material. The architecture supports OpenID Connect (OIDC) authentication for enterprise SSO integration.\nAgent Integration\nAI agents can interact with Ghostfolio through its REST API to query portfolio positions, fetch performance metrics, create or update transactions, and generate portfolio analysis reports. This enables automated financial monitoring workflows, periodic portfolio health checks, and data-driven investment insights delivered through agent-powered dashboards."
verification: security_reviewed
source: "https://github.com/ghostfolio/ghostfolio"
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

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/ghostfolio-wealth-management-portfolio-tracking
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/ghostfolio-wealth-management-portfolio-tracking` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ghostfolio-wealth-management-portfolio-tracking/)
