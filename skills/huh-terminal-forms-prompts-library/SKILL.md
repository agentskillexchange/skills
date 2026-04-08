---
title: Huh Interactive Terminal Forms and Prompts Library for Go
description: 'Huh is an open-source Go library by Charmbracelet for building interactive
  terminal forms and prompts. It provides a rich set of form components — text inputs,
  selects, multi-selects, text areas, and confirmation dialogs — that can be composed
  into multi-page forms with validation, theming, and first-class accessibility support.
  What It Does Huh lets developers create sophisticated terminal-based forms with
  minimal code. Forms are composed of groups (pages) containing fields. Each field
  type handles user interaction, validation, and rendering automatically. The library
  supports both standalone usage and integration with Bubble Tea applications. Key
  Features Rich Field Types: Input (single-line text), Text (multi-line), Select (single
  choice from list), MultiSelect (multiple choices with optional limit), and Confirm
  (yes/no). Each field supports titles, descriptions, placeholders, and custom validation
  functions. Multi-Page Forms: Group fields into logical pages that the user navigates
  through sequentially. Each group can contain any combination of field types. Built-in
  Validation: Attach validation functions to any field. The form highlights invalid
  fields with error messages and prevents submission until all validations pass. Dynamic
  Forms: Forms can change based on previous input — show or hide fields, modify options,
  or branch to different groups based on user selections. Theming and Styling: Comes
  with multiple built-in themes (Charm, Dracula, Catppuccin, Base 16) and supports
  custom themes via Lip Gloss styles. Every visual aspect is configurable. Accessibility:
  Includes a first-class accessible mode designed for screen readers, ensuring terminal
  forms work for all users. Standalone Shorthand: Individual fields can be run directly
  without wrapping them in a form, making quick single-prompt interactions trivial.
  How Agents Use It AI coding agents building Go CLI tools that require user input
  can use Huh to generate interactive configuration wizards, setup flows, or data
  collection prompts. Agents working on Go TUI applications can integrate Huh forms
  directly into Bubble Tea programs. The library is particularly useful for scaffolding
  tools, project initializers, and any CLI that needs structured user input with validation.
  Installation go get charm.land/huh/v2 Integration Points Huh integrates with Bubble
  Tea for embedding forms in TUI applications, uses Lip Gloss for styling, and works
  with the Glamour markdown renderer for rich form descriptions. It is part of the
  Charmbracelet ecosystem alongside Gum (shell script forms), Bubble Tea (TUI framework),
  and other terminal tools.'
verification: security_reviewed
source: https://github.com/charmbracelet/huh
category:
- Developer Tools
framework:
- Multi-Framework
---

# Huh Interactive Terminal Forms and Prompts Library for Go

Huh is an open-source Go library by Charmbracelet for building interactive terminal forms and prompts. It provides a rich set of form components — text inputs, selects, multi-selects, text areas, and confirmation dialogs — that can be composed into multi-page forms with validation, theming, and first-class accessibility support. What It Does Huh lets developers create sophisticated terminal-based forms with minimal code. Forms are composed of groups (pages) containing fields. Each field type handles user interaction, validation, and rendering automatically. The library supports both standalone usage and integration with Bubble Tea applications. Key Features Rich Field Types: Input (single-line text), Text (multi-line), Select (single choice from list), MultiSelect (multiple choices with optional limit), and Confirm (yes/no). Each field supports titles, descriptions, placeholders, and custom validation functions. Multi-Page Forms: Group fields into logical pages that the user navigates through sequentially. Each group can contain any combination of field types. Built-in Validation: Attach validation functions to any field. The form highlights invalid fields with error messages and prevents submission until all validations pass. Dynamic Forms: Forms can change based on previous input — show or hide fields, modify options, or branch to different groups based on user selections. Theming and Styling: Comes with multiple built-in themes (Charm, Dracula, Catppuccin, Base 16) and supports custom themes via Lip Gloss styles. Every visual aspect is configurable. Accessibility: Includes a first-class accessible mode designed for screen readers, ensuring terminal forms work for all users. Standalone Shorthand: Individual fields can be run directly without wrapping them in a form, making quick single-prompt interactions trivial. How Agents Use It AI coding agents building Go CLI tools that require user input can use Huh to generate interactive configuration wizards, setup flows, or data collection prompts. Agents working on Go TUI applications can integrate Huh forms directly into Bubble Tea programs. The library is particularly useful for scaffolding tools, project initializers, and any CLI that needs structured user input with validation. Installation go get charm.land/huh/v2 Integration Points Huh integrates with Bubble Tea for embedding forms in TUI applications, uses Lip Gloss for styling, and works with the Glamour markdown renderer for rich form descriptions. It is part of the Charmbracelet ecosystem alongside Gum (shell script forms), Bubble Tea (TUI framework), and other terminal tools.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/huh-terminal-forms-prompts-library/)
