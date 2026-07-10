---
name: "Mailgun JavaScript SDK for Email Delivery and Domain Operations"
slug: "mailgun-javascript-sdk-email-delivery-and-domain-operations"
description: "An ASE skill built around the official Mailgun JavaScript SDK for sending email and managing Mailgun API workflows from Node.js. It fits agent tasks that need transactional messaging, domain-aware email operations, event handling, and direct integration with the Mailgun platform."
github_stars: 547
verification: "security_reviewed"
source: "https://github.com/mailgun/mailgun.js"
author: "mailgun"
publisher_type: "Company"
category: "Calendar, Email & Productivity"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "mailgun/mailgun.js"
  github_stars: 547
  npm_package: "mailgun.js"
  npm_weekly_downloads: 927003
---

# Mailgun JavaScript SDK for Email Delivery and Domain Operations

An ASE skill built around the official Mailgun JavaScript SDK for sending email and managing Mailgun API workflows from Node.js. It fits agent tasks that need transactional messaging, domain-aware email operations, event handling, and direct integration with the Mailgun platform.

## Prerequisites

Node.js runtime 18+ with the mailgun.js package

## Installation

Use the upstream install or setup path that matches your environment:
- npm install mailgun.js
- Make sure that this property is a JSON string like:
- npm install -g http-proxy
- npm install

Requirements and caveats from upstream:
- A javascript sdk for Mailgun built with webpack, babel & es6. This can be used in node or in the browser*.
- Requires node.js >= 18.x
- NOTE: starting from version 3.0 you need to pass FormData (we need this to keep library universal). For node.js you can use built-in FormData or form-data library.

Basic usage or getting-started notes:
- [Fetch API usage](#fetch-api-usage)
- SH
- The next step is to import the module and instantiate a mailgun client by calling new Mailgun(formData) and then using mailgun.client setup the client with basic auth credentials (username: 'api', key: 'MAILGUN_API_KE...

- Source: https://github.com/mailgun/mailgun.js
- Extracted from upstream docs: https://raw.githubusercontent.com/mailgun/mailgun.js/HEAD/README.md

## Documentation

- https://documentation.mailgun.com/docs/mailgun/sdk/nodejs_sdk

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mailgun-javascript-sdk-email-delivery-and-domain-operations/)
