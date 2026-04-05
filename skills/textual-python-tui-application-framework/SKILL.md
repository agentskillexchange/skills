---
name: "Textual Python TUI Application Framework by Textualize"
description: "Textual is a lean application framework for Python that lets you build sophisticated terminal user interfaces with a simple API. Apps built with Textual run in the terminal and can also be served in a web browser, making it ideal for dashboards, data explorers, and developer tools."
category: "Developer Tools"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/Textualize/textual"
tool_ecosystem:
  github_repo: "Textualize/textual"
  github_stars: 35232
---
# Textual Python TUI Application Framework by Textualize

Textual is a lean application framework for Python that lets you build sophisticated terminal user interfaces with a simple API. Apps built with Textual run in the terminal and can also be served in a web browser, making it ideal for dashboards, data explorers, and developer tools.

Overview

Textual is a Python framework for building rich terminal user interfaces (TUIs) created by Textualize, the team behind Rich. It combines modern Python async patterns with concepts borrowed from web development — CSS-like styling, reactive state management, and a component-based widget system — to make terminal app development accessible and productive.



Core Capabilities

Textual provides a complete widget library including buttons, data tables, tree views, text inputs, text areas, markdown viewers, tabbed content, and more. The layout system uses a CSS dialect that supports flexbox-style arrangements, grids, docking, and layering. Every widget supports theming with predefined color schemes that work across terminal emulators.



The framework is built on Python’s asyncio, so integrating with async libraries, network calls, or background tasks is straightforward. For developers who don’t need async, Textual doesn’t force it — synchronous patterns work fine for simpler apps.



Agent Integration

For AI coding agents, Textual is valuable as both a build target and an inspection tool. Agents can scaffold complete TUI applications from natural language descriptions, generate widget layouts programmatically, and create interactive data exploration tools. The built-in testing framework (textual.testing) enables agents to verify UI behavior without manual interaction.



Installation and Usage

Install via pip: pip install textual. The framework requires Python 3.8 or later. A minimal app is under 20 lines of code — subclass App, define a compose() method yielding widgets, and call app.run(). Textual apps can also be served over HTTP using textual serve for browser-based access.



Documentation and Community

Full documentation is available at textual.textualize.io with guides, tutorials, widget galleries, and API references. The project has over 35,000 GitHub stars, an active Discord community, and regular releases. It is licensed under MIT.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill textual-python-tui-application-framework
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill textual-python-tui-application-framework -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill textual-python-tui-application-framework -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill textual-python-tui-application-framework -a codex
```

### OpenClaw

```bash
clawhub install textual-python-tui-application-framework
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/textual-python-tui-application-framework/)
