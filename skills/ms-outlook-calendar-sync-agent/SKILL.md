---
name: "Microsoft Outlook Calendar Sync Agent"
slug: "ms-outlook-calendar-sync-agent"
description: "Synchronizes calendar events bidirectionally using the Microsoft Graph API /me/calendar/events endpoint. Handles delta queries with deltaToken for incremental sync, manages recurrence patterns, and resolves timezone conflicts."
verification: "security_reviewed"
source: "https://learn.microsoft.com/en-us/graph/outlook-calendar-concept-overview"
category: "Calendar, Email & Productivity"
framework: "Custom Agents"
---

# Microsoft Outlook Calendar Sync Agent

Synchronizes calendar events bidirectionally using the Microsoft Graph API /me/calendar/events endpoint. Handles delta queries with deltaToken for incremental sync, manages recurrence patterns, and resolves timezone conflicts.

## Installation

Requirements and caveats from upstream:
- Access to this page requires authorization. You can try signing in or changing directories .
- Access to this page requires authorization. You can try changing directories .
- Save overhead in storing and managing app data in external data stores. With Microsoft Graph, you can store custom app data as open extensions in individual resource instances. If you require the data to be typed or w...

Basic usage or getting-started notes:
- Outlook customers can apply categories to events, messages, contacts, tasks, and group posts in a consistent way to enhance organization and discovery. The calendar API lets you access and define a user's master list...
- The calendar API lets you get calendar items of the signed-in user, or users who have shared or delegated their calendars to the signed-in user. For example, if Garth has shared a calendar with John, or if Garth has d...
- As an example in Outlook, customers can organize a meeting and include attendees joining from a conference room in Seattle, a coffee shop in Paris, and a home office in China. Programmatically, the event locations pro...

- Source: https://learn.microsoft.com/en-us/graph/outlook-calendar-concept-overview

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/ms-outlook-calendar-sync-agent/)
