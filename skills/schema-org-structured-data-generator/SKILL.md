---
title: "Schema.org Structured Data Generator"
description: "Generates JSON-LD structured data markup for articles, products, FAQs, and how-to pages using Schema.org vocabulary. Validates output against Google Rich Results Test API and SchemaValidator.org endpoints."
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/schema-org-structured-data-generator/"
category:
  - "Content Writing &amp; SEO"
framework:
  - "Gemini"
---

# Schema.org Structured Data Generator

This skill automatically generates valid JSON-LD structured data markup following the Schema.org vocabulary for SEO-critical page types. It supports multiple schema types: Article (with author, datePublished, dateModified, publisher), Product (with offers, aggregateRating, review), FAQPage (with mainEntity Question/Answer pairs), HowTo (with step, tool, supply, totalTime), BreadcrumbList (with itemListElement), and LocalBusiness (with address, geo, openingHours). The skill analyzes page content to extract relevant entities and properties, populating schema fields from existing HTML elements using CSS selectors or natural language extraction. For e-commerce pages, it generates Product schema with Offer properties including price, priceCurrency, availability (InStock/OutOfStock/PreOrder), and priceValidUntil. The FAQ schema generator parses content for question patterns and generates compliant FAQPage markup with proper mainEntity arrays. Validation runs against two endpoints: Google’s Rich Results Test API (POST to https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run) and Schema.org’s validator. The skill outputs minified JSON-LD wrapped in

## Installation

Choose whichever fits your setup:

1. Copy this skill folder into your local skills directory.
2. Clone the repo and symlink or copy the skill into your agent workspace.
3. Add the repo as a git submodule if you manage shared skills centrally.
4. Install it through your internal provisioning or packaging workflow.
5. Download the folder directly from GitHub and place it in your skills collection.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/schema-org-structured-data-generator/)
