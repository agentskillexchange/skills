---
title: Chartbrew Open Source Reporting Platform for API and Database Dashboards
description: 'Chartbrew is an open-source reporting platform that connects directly
  to databases and APIs to create interactive charts and dashboards. With over 3,600
  GitHub stars and active development, it provides a self-hosted alternative to tools
  like Metabase and Redash with a focus on API-first data visualization and embeddable
  chart components. Data Source Integrations Chartbrew connects to a wide range of
  data sources out of the box: SQL databases — MySQL, PostgreSQL with direct query
  support NoSQL databases — MongoDB, Firebase Firestore, Firebase Realtime Database
  REST APIs — Any HTTP API with configurable authentication, headers, and pagination
  Google Analytics — Direct integration for web analytics data Key Features The platform
  includes a visual chart builder that supports line charts, bar charts, pie charts,
  tables, and custom visualizations powered by Chart.js. Users create datasets by
  configuring API requests or database queries, then map the response data to chart
  axes and series. Chartbrew includes an AI assistant that helps users write queries
  and configure data transformations. Dashboards can be shared publicly or embedded
  in other applications using iframe or direct chart embedding. Reports can be scheduled
  for automatic refresh and email delivery. Architecture and Deployment Chartbrew
  runs as a Node.js application with a React frontend and Express backend. It requires
  MySQL or PostgreSQL for its own data storage, plus Redis for job scheduling. Deployment
  options include: Docker containers via the official razvanilin/chartbrew image DigitalOcean
  1-click marketplace droplet Manual deployment with git clone and npm run setup Agent
  Integration For AI agents and automation, Chartbrew provides a REST API for managing
  charts, dashboards, and data connections programmatically. Agents can create new
  data connections, build chart configurations, trigger data refreshes, and export
  chart images or data. The API-first design makes it straightforward to automate
  dashboard creation and reporting workflows. Installation git clone https://github.com/chartbrew/chartbrew.git
  cd chartbrew && npm run setup Or with Docker: docker pull razvanilin/chartbrew docker
  run -p 4019:4019 -p 4018:4018 razvanilin/chartbrew Use Cases Chartbrew is used for
  internal analytics dashboards, client reporting portals, KPI tracking, API monitoring
  dashboards, and any scenario where teams need to visualize data from multiple sources
  in a single, self-hosted platform. The embeddable charts feature makes it particularly
  useful for SaaS products that need to provide analytics to their own users.'
verification: security_reviewed
source: https://github.com/chartbrew/chartbrew
category:
- Monitoring &amp; Alerts
framework:
- Multi-Framework
---

# Chartbrew Open Source Reporting Platform for API and Database Dashboards

Chartbrew is an open-source reporting platform that connects directly to databases and APIs to create interactive charts and dashboards. With over 3,600 GitHub stars and active development, it provides a self-hosted alternative to tools like Metabase and Redash with a focus on API-first data visualization and embeddable chart components. Data Source Integrations Chartbrew connects to a wide range of data sources out of the box: SQL databases — MySQL, PostgreSQL with direct query support NoSQL databases — MongoDB, Firebase Firestore, Firebase Realtime Database REST APIs — Any HTTP API with configurable authentication, headers, and pagination Google Analytics — Direct integration for web analytics data Key Features The platform includes a visual chart builder that supports line charts, bar charts, pie charts, tables, and custom visualizations powered by Chart.js. Users create datasets by configuring API requests or database queries, then map the response data to chart axes and series. Chartbrew includes an AI assistant that helps users write queries and configure data transformations. Dashboards can be shared publicly or embedded in other applications using iframe or direct chart embedding. Reports can be scheduled for automatic refresh and email delivery. Architecture and Deployment Chartbrew runs as a Node.js application with a React frontend and Express backend. It requires MySQL or PostgreSQL for its own data storage, plus Redis for job scheduling. Deployment options include: Docker containers via the official razvanilin/chartbrew image DigitalOcean 1-click marketplace droplet Manual deployment with git clone and npm run setup Agent Integration For AI agents and automation, Chartbrew provides a REST API for managing charts, dashboards, and data connections programmatically. Agents can create new data connections, build chart configurations, trigger data refreshes, and export chart images or data. The API-first design makes it straightforward to automate dashboard creation and reporting workflows. Installation git clone https://github.com/chartbrew/chartbrew.git cd chartbrew && npm run setup Or with Docker: docker pull razvanilin/chartbrew docker run -p 4019:4019 -p 4018:4018 razvanilin/chartbrew Use Cases Chartbrew is used for internal analytics dashboards, client reporting portals, KPI tracking, API monitoring dashboards, and any scenario where teams need to visualize data from multiple sources in a single, self-hosted platform. The embeddable charts feature makes it particularly useful for SaaS products that need to provide analytics to their own users.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/chartbrew-open-source-reporting-dashboard-platform/)
