---
name: "Schema.org Structured Data Generator"
description: "Generates JSON-LD structured data markup for articles, products, FAQs, and how-to pages using Schema.org vocabulary. Validates output against Google Rich Results Test API and SchemaValidator.org endpoints."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/schema-org-structured-data-generator/"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Gemini"
---

# Schema.org Structured Data Generator

This skill automatically generates valid JSON-LD structured data markup following the Schema.org vocabulary for SEO-critical page types. It supports multiple schema types: Article (with author, datePublished, dateModified, publisher), Product (with offers, aggregateRating, review), FAQPage (with mainEntity Question/Answer pairs), HowTo (with step, tool, supply, totalTime), BreadcrumbList (with itemListElement), and LocalBusiness (with address, geo, openingHours). The skill analyzes page content to extract relevant entities and properties, populating schema fields from existing HTML elements using CSS selectors or natural language extraction. For e-commerce pages, it generates Product schema with Offer properties including price, priceCurrency, availability (InStock/OutOfStock/PreOrder), and priceValidUntil. The FAQ schema generator parses content for question patterns and generates compliant FAQPage markup with proper mainEntity arrays. Validation runs against two endpoints: Google's Rich Results Test API (POST to https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run) and Schema.org's validator. The skill outputs minified JSON-LD wrapped in  tags ready for HTML injection. It handles nested schema relationships using @id references for connected entities and supports schema inheritance for complex page types.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/schema-org-structured-data-generator/)
