# Daedalus

A standalone agent skill for implementing, refactoring and debugging code through small, deliberate changes. Define success first, inspect the existing code, make one change, review its diff, and verify the result.

> Slow is smooth, smooth is fast.

## Install

From your project's directory, install for Codex with the Skills CLI:

```bash
npx skills@1.8.1 add AntreasAntoniou/daedalus-agent-skill --skill daedalus --agent codex
```

Or clone the complete skill into a new project-local skill directory:

```bash
mkdir -p .agents/skills
git clone https://github.com/AntreasAntoniou/daedalus-agent-skill.git .agents/skills/daedalus
```

Keep the complete folder, including `scripts/`, `requirements.txt`, `references/` and `agents/`. If a skill directory already exists, review it before replacing anything. Other agents that understand `SKILL.md` can use the same files in their documented skill directory; discovery and invocation depend on the host.

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

The [full skill](SKILL.md) includes Python conventions: Python 3.14+, Google Fire for CLIs, type hints, Google-style docstrings, and repository-aware formatting.

## Bundled tools

All three tools referenced by the original skill are included. They use Python 3.14+, [Google Fire](https://github.com/google/python-fire) for command-line arguments and [Rich](https://github.com/Textualize/rich) for console output. [requirements.txt](requirements.txt) pins the tested direct dependencies. The commands below use `uv` to select Python 3.14 and provide those dependencies without changing the project's environment. Repository ingestion also needs Git; the examples use a POSIX shell.

From the project where you installed the skill, set its location once. For a global install, set `SKILL_DIR` to that installation's actual absolute directory instead:

```bash
REPO_ROOT=$(git rev-parse --show-toplevel)
SKILL_DIR="$REPO_ROOT/.agents/skills/daedalus"
CONTEXT_DIR=$(mktemp -d "${TMPDIR:-/tmp}/daedalus-context.XXXXXX")
```

**Map the checkout, including Python classes and functions:**

```bash
uv run --no-project --python 3.14 --with-requirements "$SKILL_DIR/requirements.txt" python \
  "$SKILL_DIR/scripts/map_directory.py" "$REPO_ROOT" "$CONTEXT_DIR/directory-map.md" \
  --ignore_dirs='[".git",".venv","venv","__pycache__",".mypy_cache",".pytest_cache",".ruff_cache",".cache",".chronicle",".remember","node_modules","dist","build"]'
```

The Markdown output contains a directory tree and simplified signatures for top-level Python functions, async functions and classes. It parses source with `ast`; it does not execute the mapped code. It omits nested methods and full type/default signatures, and records parse failures in the map. Directory ignores match names, not `.gitignore` rules.

**Combine a selected local directory into readable context:**

```bash
uv run --no-project --python 3.14 --with-requirements "$SKILL_DIR/requirements.txt" python \
  "$SKILL_DIR/scripts/ingest_content.py" "$SKILL_DIR/scripts" "$CONTEXT_DIR/tool-content.txt" \
  --extensions='[".py"]'
```

Replace the input directory with the task-relevant source directory. The output preserves each file's relative path in start/end markers and includes its text. Local extension filters include a leading dot. This tool does not apply `.gitignore` or the mapper's ignored-directory list, so select the input directory deliberately.

**Inspect a remote repository without retaining its checkout:**

```bash
uv run --no-project --python 3.14 --with-requirements "$SKILL_DIR/requirements.txt" python \
  "$SKILL_DIR/scripts/ingest_github_repo.py" \
  --repo_url=https://github.com/AntreasAntoniou/daedalus-agent-skill.git \
  --output_file="$CONTEXT_DIR/repository-content.txt" --branch=main \
  --extensions='[".py",".md"]'
```

The tool shallow-clones the selected branch into a temporary directory, combines matching files with relative-path markers, then removes the temporary checkout. Omit `--branch` to use the remote's default branch. Clone and content operations do not install or run repository code. Git uses your existing Git configuration and access.

All three tools skip symlinks; local tools exclude their own output file and remote ingestion excludes `.git` metadata. They do not redact secrets or decide what may be shared. Read the output before using it as context. The inherited ingestion tools may log a failure or no matches without returning a nonzero exit code; verify a fresh, nonempty output and read their diagnostics. Local ingestion ignores undecodable UTF-8 bytes; repository ingestion falls back to Latin-1. Extension selection is not binary detection.

Append `--help` to any script invocation to see its Fire-generated help.

## Verification

From this skill's checkout:

```bash
uv run --no-project --python 3.14 --with-requirements requirements.txt python \
  -m unittest discover -s tests -v
```

The integration tests invoke the real CLIs in disposable directories and a local Git repository. They check Python outlines, ignored directories, content preservation, extension filtering, branch selection, generated help, symlink boundaries and output self-exclusion.

## Scope and evidence

This is an instruction package, not an enforcement hook or an autonomous runner. It does not grant permission to publish, spend, access private data or launch other agents. Actual behavior depends on the host and model. Packaging and install checks establish that the files are discoverable and self-contained; they do not establish a measured improvement in coding quality or runtime compatibility with every agent.

This public edition generalizes owner-specific wording and bundles the mapper and both ingestion scripts previously referenced from a private archive. Version 1.0.0 omitted those tools and substituted a Git inventory; version 1.1.0 corrects that incomplete release. No private archive or owner-specific filesystem path is required.

## Files

- [SKILL.md](SKILL.md): the method and activation description.
- [references/arise.md](references/arise.md): optional persona entrance.
- [agents/openai.yaml](agents/openai.yaml): Codex display metadata.
- [scripts/map_directory.py](scripts/map_directory.py): directory tree and Python outline.
- [scripts/ingest_content.py](scripts/ingest_content.py): selected local file contents.
- [scripts/ingest_github_repo.py](scripts/ingest_github_repo.py): temporary clone and content ingestion.
- [requirements.txt](requirements.txt): tested Fire and Rich versions.
- [tests/test_tools.py](tests/test_tools.py): CLI integration checks.
- [CHANGELOG.md](CHANGELOG.md): public edition changes.

## License

[MIT](LICENSE).
