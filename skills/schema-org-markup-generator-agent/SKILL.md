---
title: "Schema.org Markup Generator"
description: "Generates structured data markup using Schema.org vocabulary in JSON-LD format. Supports Article, Product, FAQPage, HowTo, and LocalBusiness schemas with Google Rich Results Test API validation."
slug: "schema-org-markup-generator-agent"
category:
  - "Content Writing &amp; SEO"
framework:
  - "MCP"
verification: "security_reviewed"
source: "https://agentskillexchange.com/skills/schema-org-markup-generator-agent/"
---

# Schema.org Markup Generator

Generates structured data markup using Schema.org vocabulary in JSON-LD format. Supports Article, Product, FAQPage, HowTo, and LocalBusiness schemas with Google Rich Results Test API validation.

## Installation

### Method 1: OpenClaw Control UI
1. Open OpenClaw Control UI.
2. Search for this skill by name or slug.
3. Review the skill details and install it.

### Method 2: OpenClaw Chat
1. Ask OpenClaw to install this skill from Agent Skill Exchange.
2. Confirm the install when prompted.

### Method 3: ClawHub CLI
```bash
clawhub install schema-org-markup-generator-agent
```

### Method 4: Manual download
1. Download or clone the skill files.
2. Place them in your local skills directory.
3. Reload OpenClaw or your agent runtime.

### Method 5: From source
1. Open the upstream source linked below.
2. Follow the project setup instructions there.

Schema.org Markup Generator creates valid JSON-LD structured data for web pages following the Schema.org vocabulary specification. It analyzes page content and generates appropriate markup for types including Article, Product, FAQPage, HowTo, LocalBusiness, BreadcrumbList, and VideoObject.
The agent constructs nested schema objects with proper @context, @type, and @id references, handling multi-entity pages with @graph arrays. For Product schema, it includes AggregateRating, Offer with priceValidUntil, and Review markup meeting Google’s merchant listing requirements.
Validates generated markup against Google’s Rich Results Test API (https://searchconsole.googleapis.com/v1/urlTestingTools/mobileFriendlyTest:run) and Schema.org’s official validator. Handles conditional properties like isAccessibleForFree for paywalled content and speakable for voice search optimization. Outputs ready-to-embed <script type="application/ld+json"> blocks with proper escaping.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/schema-org-markup-generator-agent/)
