---
name: "Figma REST API Asset Exporter"
slug: "figma-rest-api-asset-exporter"
description: "Exports design assets from Figma files using the GET /v1/files/:key and /v1/images/:key endpoints. Supports SVG, PNG, and PDF export with scale and format parameters."
verification: "listed"
source: "https://developers.figma.com/docs/rest-api/"
author: "Figma"
category: "Image & Creative Automation"
framework: "Custom Agents"
---

# Figma REST API Asset Exporter

Exports design assets from Figma files using the GET /v1/files/:key and /v1/images/:key endpoints. Supports SVG, PNG, and PDF export with scale and format parameters.

## Installation

Use the upstream install or setup path that matches your environment:
- Make requests for different resources:

Requirements and caveats from upstream:
- Once granted access, you can use the Figma API to inspect a JSON representation of the file. Every layer or object in a file will be represented within the file by a node (subtree). You will then be able to access and...

Basic usage or getting-started notes:
- The Figma API supports access and interactions with Figma's different products. This gives you the ability to do things such as view and extract any objects or layers, and their properties from files, get usage data,...
- Get usage and analytics data:
- For example: GET https://api.figma.com/v1/files/:key

- Source: https://developers.figma.com/docs/rest-api/

## Documentation

- https://developers.figma.com/docs/rest-api/

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/figma-rest-api-asset-exporter/)
