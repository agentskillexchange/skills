---
title: "Umami Privacy-Focused Web Analytics Platform"
description: "Umami is a modern, privacy-focused, open-source web analytics platform and a self-hostable alternative to Google Analytics, Mixpanel, and Amplitude. It collects website traffic data without cookies and is fully GDPR compliant."
verification: security_reviewed
source: "https://github.com/umami-software/umami"
category:
  - "Monitoring & Alerts"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "umami-software/umami"
  github_stars: 35941
---

# Umami Privacy-Focused Web Analytics Platform

Umami is a modern, open-source web analytics platform that provides a privacy-focused alternative to Google Analytics. With over 35,000 GitHub stars and an active development community, it is one of the most popular self-hosted analytics solutions available. Umami does not use cookies, does not track users across websites, and is fully compliant with GDPR, CCPA, and PECR privacy regulations.

Core Features
Umami provides real-time website visitor tracking with a clean, intuitive dashboard. It displays key metrics including unique visitors, page views, bounce rate, average visit duration, referrer sources, browser and OS breakdowns, device types, and geographic locations. The dashboard supports custom date ranges and comparison periods for trend analysis.

Event Tracking and Custom Data
Beyond page views, Umami supports custom event tracking. You can track button clicks, form submissions, file downloads, and other user interactions by adding simple data attributes to your HTML elements or using the JavaScript tracking API. Events can carry custom properties for more granular analysis.

Teams and Sharing
Umami supports multiple websites and user accounts, making it suitable for agencies and teams managing multiple properties. You can create shareable dashboard links with public URLs that do not require authentication, useful for sharing analytics with clients or stakeholders.

Technical Stack and Deployment
Umami is built with Next.js and supports PostgreSQL as its database. Deployment is straightforward using Docker Compose, which bundles both the application and the database. The tracking script is under 2 KB, significantly lighter than Google Analytics, resulting in minimal performance impact on tracked websites. The application can be deployed on any platform that supports Node.js 18+ and PostgreSQL 12+.

API and Agent Integration
Umami provides a comprehensive REST API for programmatic access to all analytics data. AI agents can query visitor statistics, page view data, event counts, and session information via the API. This enables automated performance reporting, traffic anomaly detection, and integration with SEO or content optimization workflows.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/umami-privacy-focused-web-analytics
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/umami-privacy-focused-web-analytics` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/umami-privacy-focused-web-analytics/)
