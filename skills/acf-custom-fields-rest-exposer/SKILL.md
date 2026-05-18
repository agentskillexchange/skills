---
name: "ACF Custom Fields REST Exposer"
slug: "acf-custom-fields-rest-exposer"
description: "Exposes Advanced Custom Fields data through the WordPress REST API using register_rest_field and acf_format_value. Handles repeater fields, flexible content layouts, and gallery fields with proper serialization."
verification: "listed"
source: "https://www.advancedcustomfields.com/resources/wp-rest-api-integration/"
author: "WP Engine"
category: "WordPress & CMS"
framework: "Cursor"
---

# ACF Custom Fields REST Exposer

Exposes Advanced Custom Fields data through the WordPress REST API using register_rest_field and acf_format_value. Handles repeater fields, flexible content layouts, and gallery fields with proper serialization.

## Installation

Requirements and caveats from upstream:
- POST requests allow you to update any ACF fields, and require you to authenticate to perform the request.

Basic usage or getting-started notes:
- In the following example, we’ve configured a custom post type book , and an ACF field group for all books, with Author (Text), Author Bio (WYSIWYG), and Author Image (Image) fields. We’ll add data to each book for the...
- Performing an OPTIONS request to a WordPress REST API endpoint allows you to see the schema for that data object, i.e., the available fields and their properties. For ACF fields, it allows you to see details for the f...
- In our example post above, making an OPTIONS request will return the schema for the book, including data about the ACF fields we’ve set up.

- Source: https://www.advancedcustomfields.com/resources/wp-rest-api-integration/

## Documentation

- https://www.advancedcustomfields.com/resources/wp-rest-api-integration/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/acf-custom-fields-rest-exposer/)
