---
title: "React Email Component Library for Building Email Templates"
description: "React Email is an open source component library for building responsive, cross-client email templates using React and TypeScript. It handles Gmail, Outlook, and Apple Mail inconsistencies, supports dark mode, and renders to standard HTML for use with any email provider."
verification: security_reviewed
source: "https://github.com/resend/react-email"
category:
  - "Templates & Workflows"
framework:
  - "Multi-Framework"
tool_ecosystem:
  github_repo: "resend/react-email"
  github_stars: 18373
---

# React Email Component Library for Building Email Templates

Overview
React Email is an open source library by Resend that provides a collection of unstyled, high-quality React components purpose-built for email rendering. It replaces the traditional approach of hand-coding table-based HTML layouts with a modern component-based workflow using JSX and TypeScript. The library handles cross-client rendering inconsistencies between Gmail, Outlook, Apple Mail, and other email clients automatically.

Core Components
The library ships as @react-email/components on npm and includes components for Body, Button, CodeBlock, Column, Container, Divider, Font, Head, Heading, Html, Image, Link, Markdown, Paragraph, Preview, Row, and Section. Each component generates email-safe HTML that works across all major email clients. The components are unstyled by default, giving full control over design through inline styles or Tailwind CSS via the Tailwind component.

Development Workflow
React Email includes a local development server that provides live preview of email templates as you code them. Templates are standard React components stored as files. The CLI (npx react-email) starts the preview server, exports templates to HTML, and supports hot reloading. Templates can be organized in a dedicated emails/ directory within any project.

Provider Compatibility
Emails built with React Email render to standard HTML and can be sent through any email service provider. The library includes integration examples for Resend, Nodemailer, SendGrid, Postmark, AWS SES, Plunk, and Mailersend. The render() function converts React components to HTML strings suitable for any SMTP or API-based sending service.

Agent Integration
AI agents can use React Email to programmatically generate well-formatted email content. Template components accept props, making it straightforward to inject dynamic data from agent workflows. Common patterns include generating report emails with data tables, notification emails with action buttons, and digest emails with curated content sections. The TypeScript types ensure template props are validated at build time.

Installation
Install components: npm install @react-email/components -E. For the development preview server: npm install react-email -D. Requires React 18+ and Node.js 18+. The library is MIT licensed and maintained by the Resend team with frequent releases.

## Installation

### Option 1, Agent Skill Exchange

Browse and install from the marketplace page for this skill.

### Option 2, Git clone

```bash
git clone https://github.com/agentskillexchange/skills.git && cd skills/skills/react-email-component-library-email-templates
```

### Option 3, Download ZIP

Download the skill folder or repository archive and extract `skills/react-email-component-library-email-templates` into your local skills collection.

### Option 4, Manual copy

Copy this skill folder into your agent skills directory, then reload your agent tooling.

### Option 5, Fork and sync

Fork the repository if you want to track local edits while keeping a clean upstream sync path.

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/react-email-component-library-email-templates/)
