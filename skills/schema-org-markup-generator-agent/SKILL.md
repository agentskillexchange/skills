---
name: "Schema.org Markup Generator"
description: "Generates structured data markup using Schema.org vocabulary in JSON-LD format. Supports Article, Product, FAQPage, HowTo, and LocalBusiness schemas with Google Rich Results Test API validation."
verification: security_reviewed
source: "https://agentskillexchange.com/skills/schema-org-markup-generator-agent/"
category:
  - "Content Writing &amp; SEO"
framework:
  - "MCP"
---

# Schema.org Markup Generator

Schema.org Markup Generator creates valid JSON-LD structured data for web pages following the Schema.org vocabulary specification. It analyzes page content and generates appropriate markup for types including Article, Product, FAQPage, HowTo, LocalBusiness, BreadcrumbList, and VideoObject.
The agent constructs nested schema objects with proper @context, @type, and @id references, handling multi-entity pages with @graph arrays. For Product schema, it includes AggregateRating, Offer with priceValidUntil, and Review markup meeting Google's merchant listing requirements.
Validates generated markup against Google's Rich Results Test API (https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run) and Schema.org's official validator. Handles conditional properties like isAccessibleForFree for paywalled content and speakable for voice search optimization. Outputs ready-to-embed <script type="application/ld+json"> blocks with proper escaping.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/schema-org-markup-generator-agent/)
