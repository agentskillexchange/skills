---
title: "Schema.org Structured Data Generator"
description: "This skill automatically generates valid JSON-LD structured data markup following the Schema.org vocabulary for SEO-critical page types. It supports multiple schema types: Article (with author, datePublished, dateModified, publisher), Product (with offers, aggregateRating, review), FAQPage (with mainEntity Question/Answer pairs), HowTo (with step, tool, supply, totalTime), BreadcrumbList (with itemListElement), and LocalBusiness (with address, geo, openingHours). The skill analyzes page content to extract relevant entities and properties, populating schema fields from existing HTML elements using CSS selectors or natural language extraction. For e-commerce pages, it generates Product schema with Offer properties including price, priceCurrency, availability (InStock/OutOfStock/PreOrder), and priceValidUntil. The FAQ schema generator parses content for question patterns and generates compliant FAQPage markup with proper mainEntity arrays. Validation runs against two endpoints: Google&#8217;s Rich Results Test API (POST to https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run) and Schema.org&#8217;s validator. The skill outputs minified JSON-LD wrapped in tags ready for HTML injection. It handles nested schema relationships using @id references for connected entities and supports schema inheritance for complex page types."
source: "https://agentskillexchange.com/skills/schema-org-structured-data-generator/"
verification: "security_reviewed"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Gemini"
---

# Schema.org Structured Data Generator

This skill automatically generates valid JSON-LD structured data markup following the Schema.org vocabulary for SEO-critical page types. It supports multiple schema types: Article (with author, datePublished, dateModified, publisher), Product (with offers, aggregateRating, review), FAQPage (with mainEntity Question/Answer pairs), HowTo (with step, tool, supply, totalTime), BreadcrumbList (with itemListElement), and LocalBusiness (with address, geo, openingHours). The skill analyzes page content to extract relevant entities and properties, populating schema fields from existing HTML elements using CSS selectors or natural language extraction. For e-commerce pages, it generates Product schema with Offer properties including price, priceCurrency, availability (InStock/OutOfStock/PreOrder), and priceValidUntil. The FAQ schema generator parses content for question patterns and generates compliant FAQPage markup with proper mainEntity arrays. Validation runs against two endpoints: Google&#8217;s Rich Results Test API (POST to https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run) and Schema.org&#8217;s validator. The skill outputs minified JSON-LD wrapped in tags ready for HTML injection. It handles nested schema relationships using @id references for connected entities and supports schema inheritance for complex page types.

## Installation

- From OpenClaw: Browse Agent Skill Exchange and install with one click.
- From source: Clone the upstream repository linked below.
- From package manager: Install from npm, pip, cargo, or the ecosystem-native registry when available.
- Manual setup: Follow the project documentation for local configuration and secrets.
- Containerized: Use Docker or devcontainer support if the project ships it.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/schema-org-structured-data-generator/)
