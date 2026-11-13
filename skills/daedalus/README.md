# Daedalus

A standalone agent skill for implementing, refactoring and debugging code through small, deliberate changes. Define success first, inspect the existing code, make one change, review its diff, and verify the result.

> Slow is smooth, smooth is fast.

## Install

From your project's directory, install for Codex with the Skills CLI:

```bash
npx skills add AntreasAntoniou/daedalus-agent-skill --skill daedalus --agent codex
```

Or clone the complete skill into a new project-local skill directory:

```bash
mkdir -p .agents/skills
git clone https://github.com/AntreasAntoniou/daedalus-agent-skill.git .agents/skills/daedalus
```

Keep the complete folder, including `references/` and `agents/`. If a skill directory already exists, review it before replacing anything. Other agents that understand `SKILL.md` can use the same files in their documented skill directory; discovery and invocation depend on the host.

## Use it

Ask your agent:

```text
Use $daedalus to fix this bug. First reproduce it with a failing test,
then make the smallest repair and verify the affected behavior.
```

For investigation:

```text
Use $daedalus to investigate this slowdown. State a falsifiable
hypothesis, measure a baseline, and change one variable at a time.
```

Expect a scoped plan, an observed failure or baseline, focused edits with reviewed diffs, and a report that distinguishes measured results from assumptions. When explicitly summoned as a persona, Daedalus uses the short optional [ARISE entrance](references/arise.md).

## What the method covers

- **Scope and map:** read repository instructions, preserve unrelated changes, and locate implementation, tests and entry points.
- **Define success:** reproduce a bug, specify a behavior, or establish a falsifiable measurement.
- **Edit deliberately:** prefer existing functions, make every line earn its place, and inspect each diff.
- **Verify:** read test output, exercise changed README commands, and state remaining limits.
- **Write for readers:** use meaningful names, coherent functions, explicit contracts, and documentation with working examples.

The [full skill](SKILL.md) includes Python conventions: Python 3.14+, Google Fire for CLIs, type hints, Google-style docstrings, and repository-aware formatting. Python is needed only for Python work; the skill itself runs no code and has no runtime dependencies. The inventory example requires Git and a POSIX shell; targeted searching uses ripgrep.

## Scope and evidence

This is an instruction package, not an enforcement hook or an autonomous runner. It does not grant permission to publish, spend, access private data or launch other agents. Actual behavior depends on the host and model. Packaging and install checks establish that the files are discoverable and self-contained; they do not establish a measured improvement in coding quality or runtime compatibility with every agent.

This public edition generalizes owner-specific wording and replaces a private archive mapper with a portable Git inventory. No private archive, credentials, local paths or external services are required.

## Files

- [SKILL.md](SKILL.md): the method and activation description.
- [references/arise.md](references/arise.md): optional persona entrance.
- [agents/openai.yaml](agents/openai.yaml): Codex display metadata.
- [CHANGELOG.md](CHANGELOG.md): public edition changes.

## License

[MIT](LICENSE).
