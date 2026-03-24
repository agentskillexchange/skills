---
name: "Python Type Stub Generator"
description: "Generates Python type stubs (.pyi files) using mypy stubgen and MonkeyType runtime tracing. Handles C extension modules via stubtest validation against the typeshed repository."
category: "Library & API Reference"
framework: "Claude Agents"
verification: listed  # one of: security_reviewed, verified_metadata, listed
rating: 0  # real rating only, 0 if none
reviews: 0  # real reviews only, 0 if none
creator: ""  # real creator only, empty if none
creator_handle: ""
creator_verified: false
source: "https://agentskillexchange.com/skills/python-type-stub-generator-2/"
---

# Python Type Stub Generator

Generates Python type stubs (.pyi files) using mypy stubgen and MonkeyType runtime tracing. Handles C extension modules via stubtest validation against the typeshed repository.

## Overview

The Python Type Stub Generator skill automates creation of type annotation stubs for untyped Python libraries. It combines static analysis via mypy stubgen with runtime type collection using MonkeyType (Instagram/MonkeyType) to produce accurate .pyi stub files.

For C extension modules where static analysis fails, the skill uses ctypes introspection and pybind11 signature extraction to infer parameter and return types. Generated stubs are validated against the typeshed repository patterns to ensure compatibility with type checkers.

The stubtest tool (mypy.stubtest) performs automated verification that stubs match the runtime module interface, catching missing methods, incorrect signatures, and type annotation errors. The skill handles complex patterns including overloaded functions (@overload), generic types (TypeVar), and Protocol classes.

Integration with pyright and pylance ensures stubs work across the major Python type-checking ecosystem. The generator respects existing partial stubs (py.typed marker files) and merges generated annotations with manually written ones. Output follows PEP 561 packaging conventions for distributable stub packages.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill python-type-stub-generator-2
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill python-type-stub-generator-2 -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill python-type-stub-generator-2 -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill python-type-stub-generator-2 -a codex
```

### OpenClaw

```bash
clawhub install python-type-stub-generator-2
```

## Source

- Marketplace: https://agentskillexchange.com/skills/python-type-stub-generator-2/
