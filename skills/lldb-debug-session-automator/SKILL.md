---
name: "LLDB Debug Session Automator"
description: "Automates LLDB debugging sessions with scripted breakpoint management and expression evaluation. Uses the LLDB Python SB API (lldb.SBDebugger, SBTarget, SBProcess) for programmatic debug control."
category: "Developer Tools"
framework: "Custom Agents"
verification: security_reviewed  # one of: security_reviewed, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/lldb-debug-session-automator/"
---

# LLDB Debug Session Automator

Automates LLDB debugging sessions with scripted breakpoint management and expression evaluation. Uses the LLDB Python SB API (lldb.SBDebugger, SBTarget, SBProcess) for programmatic debug control.

## Overview

The LLDB Debug Session Automator provides programmatic control over debugging sessions using the LLDB Python Scripting Bridge API. It creates automated debug workflows using lldb.SBDebugger instances with custom command interpreters and breakpoint callback functions.

The agent generates Python scripts that leverage SBTarget for binary loading, SBBreakpoint for conditional breakpoint creation with hit counts and thread filtering, and SBProcess for execution control including step-in, step-over, and continue operations. It supports SBFrame expression evaluation for variable inspection and modification during stopped states.

Advanced features include watchpoint configuration via SBWatchpoint for memory access monitoring, custom data formatter registration using SBTypeCategory and SBTypeSummary for complex structure visualization, and remote debugging setup via SBPlatform with platform connect to debug targets over network. The agent also generates .lldbinit configurations and command aliases for frequently used debug patterns.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill lldb-debug-session-automator
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill lldb-debug-session-automator -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill lldb-debug-session-automator -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill lldb-debug-session-automator -a codex
```

### OpenClaw

```bash
clawhub install lldb-debug-session-automator
```

## Source

- Marketplace: https://agentskillexchange.com/skills/lldb-debug-session-automator/
