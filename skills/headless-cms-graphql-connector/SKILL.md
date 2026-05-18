---
name: "Headless CMS GraphQL Connector"
slug: "headless-cms-graphql-connector"
description: "Connects headless CMS backends (WordPress WPGraphQL, Strapi, Contentful) to frontend frameworks using Apollo Client and urql. Handles content previews, ISR cache invalidation, and webhook-driven rebuilds."
verification: "listed"
source: "https://graphql.org/learn/queries/"
author: "GraphQL Foundation"
category: "WordPress & CMS"
framework: "Gemini"
---

# Headless CMS GraphQL Connector

Connects headless CMS backends (WordPress WPGraphQL, Strapi, Contentful) to frontend frameworks using Apollo Client and urql. Handles content previews, ISR cache invalidation, and webhook-driven rebuilds.

## Installation

Requirements and caveats from upstream:
- When creating a GraphQL document we always start with a root operation type (the Query Object type for this example) because it serves as an entry point to the API. From there we must specify the selection set of fiel...
- Variable definitions can be optional or required. In the case above, since there isn’t an ! next to the Episode type, it’s optional. But if the field you are passing the variable into requires a non-null argument, the...

Basic usage or getting-started notes:
- In the previous example, we just asked for the name of our hero which returned a String , but fields can also return Object types (and lists thereof). In that case, you can make a sub-selection of fields for that Obje...
- Note that in this example, the friends field returns an array of items. GraphQL queries look the same for single items or lists of items; however, we know which one to expect based on what is indicated in the schema.
- Arguments can be of many different types. In the above example, we have used an Enum type, which represents one of a finite set of options (in this case, units of length, either METER or FOOT ). GraphQL comes with a d...

- Source: https://graphql.org/learn/queries/

## Documentation

- https://graphql.org/learn/queries/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/headless-cms-graphql-connector/)
