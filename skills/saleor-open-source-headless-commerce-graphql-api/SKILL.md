---
name: "Saleor Open Source Headless Commerce Platform with GraphQL API"
description: "Saleor is a leading open source headless e-commerce platform built with Python and Django. It provides a GraphQL API for building custom storefronts, managing products, processing orders, and orchestrating commerce across web, mobile, and agentic channels."
category: "Integrations &amp; Connectors"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/saleor/saleor"
---
# Saleor Open Source Headless Commerce Platform with GraphQL API

Saleor is a leading open source headless e-commerce platform built with Python and Django. It provides a GraphQL API for building custom storefronts, managing products, processing orders, and orchestrating commerce across web, mobile, and agentic channels.

Saleor is the most popular open source headless commerce platform, built with Python and Django and backed by over 22,000 GitHub stars. It provides a comprehensive GraphQL API that decouples the commerce backend from the frontend, allowing developers to build custom storefronts using any technology while Saleor handles products, orders, payments, shipping, and inventory management.

Architecture and API Design

Saleor follows a MACH architecture (Microservices, API-first, Cloud-native, Headless) with GraphQL as the primary API interface. The GraphQL schema covers the complete commerce domain including product catalog management with variants and attributes, order lifecycle from cart to fulfillment, payment gateway integration with multiple processors, shipping zone configuration and rate calculation, tax computation with country-specific rules, and customer account management with address books.

Omnichannel Commerce

The platform supports multi-channel operations where a single Saleor instance can power web storefronts, mobile applications, retail point-of-sale systems, and agentic commerce interfaces. Each channel can have its own currency, pricing, product availability, and fulfillment configuration. This makes Saleor suitable for businesses that sell across multiple regions and platforms from a unified backend.

Extension and Integration

Saleor provides a webhook system for event-driven integrations, allowing external services to react to commerce events like order placement, payment capture, or inventory changes. The App framework lets developers build extensions that integrate directly into the Saleor Dashboard. Built-in support exists for payment gateways including Stripe, Adyen, and Braintree, along with shipping integrations and tax calculation services.

Developer Experience

The platform ships with a React-based Dashboard for store management, Saleor CLI for project scaffolding and deployment, and comprehensive API documentation with a GraphQL Playground for interactive query testing. Self-hosting is supported via Docker Compose with PostgreSQL and Redis dependencies. The Saleor Cloud managed hosting option is also available for teams that prefer not to manage infrastructure.

Agent Automation Potential

AI agents can leverage Saleor’s GraphQL API to automate product catalog updates, process bulk order operations, generate sales reports and analytics, manage inventory levels across warehouses, and build conversational commerce experiences. The structured GraphQL schema makes it particularly well-suited for LLM-driven commerce automation.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill saleor-open-source-headless-commerce-graphql-api
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill saleor-open-source-headless-commerce-graphql-api -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill saleor-open-source-headless-commerce-graphql-api -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill saleor-open-source-headless-commerce-graphql-api -a codex
```

### OpenClaw

```bash
clawhub install saleor-open-source-headless-commerce-graphql-api
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/saleor-open-source-headless-commerce-graphql-api/)
