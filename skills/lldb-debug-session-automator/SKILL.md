---
name: LLDB Debug Session Automator
description: Automates LLDB debugging sessions with scripted breakpoint management
  and expression evaluation. Uses the LLDB Python SB API (lldb.SBDebugger, SBTarget,
  SBProcess) for programmatic debug control.
verification: security_reviewed
source: https://agentskillexchange.com/skills/lldb-debug-session-automator/
category:
- Developer Tools
framework:
- Custom Agents
---
# LLDB Debug Session Automator

The LLDB Debug Session Automator provides programmatic control over debugging sessions using the LLDB Python Scripting Bridge API. It creates automated debug workflows using lldb.SBDebugger instances with custom command interpreters and breakpoint callback functions.
The agent generates Python scripts that leverage SBTarget for binary loading, SBBreakpoint for conditional breakpoint creation with hit counts and thread filtering, and SBProcess for execution control including step-in, step-over, and continue operations. It supports SBFrame expression evaluation for variable inspection and modification during stopped states.
Advanced features include watchpoint configuration via SBWatchpoint for memory access monitoring, custom data formatter registration using SBTypeCategory and SBTypeSummary for complex structure visualization, and remote debugging setup via SBPlatform with platform connect to debug targets over network. The agent also generates .lldbinit configurations and command aliases for frequently used debug patterns.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/lldb-debug-session-automator/)
