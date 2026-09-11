# Nexus

An agent skill by [Antreas Antoniou](https://github.com/AntreasAntoniou). Version 1.0.0; MIT licensed.

## Problem

Unfamiliar repositories invite either shallow guesses or expensive whole-codebase reading.

## Mechanism

Map paths and top-level Python symbols, select investigation questions, trace implementation/contracts/tests, then produce a revision-aware context pack with facts, inferences, and unknowns.

## Why useful

The handoff explains why each area matters and names a bounded change and verification surface. The bundled mapper is a portable adaptation of the original directory-and-Python-symbol method; it uses only the Python standard library.

## Install

With the Agent Skills CLI:

```sh
npx skills add AntreasAntoniou/nexus --skill nexus
```

Use a compatible agent's skill installer with `AntreasAntoniou/nexus`, or clone this repository into that host's configured skills directory under the folder name `nexus`:

```sh
git clone https://github.com/AntreasAntoniou/nexus.git <your-skills-directory>/nexus
```

Replace the destination placeholder first. The repository root is the single discoverable skill, with [SKILL.md](SKILL.md) as its entry point. Installation location and reload/discovery steps vary by host. Installing the skill grants no extra permissions. The host must support Markdown skills; only packages with helpers require Python.

## Example

> Use $nexus on the repository I specify to trace how a request reaches the storage layer. Produce a context pack outside the repository, include existing tests and cite code; do not modify the repository.

### Mapper

Requires Python 3.10+. From this installed skill directory, run:

```sh
python3 scripts/map_directory.py /path/to/authorized-repository /path/to/new-map.md
python3 scripts/map_directory.py --help
```

Replace the illustrative paths. The output parent must exist, the output must be outside the mapped root, and an existing output is never overwritten. On POSIX the new map is created with owner-only mode 0600 (a stricter umask may further restrict it); destination-directory permissions and non-POSIX ACLs remain the operator's responsibility. Use `--ignore-dir NAME` and `--ignore-file GLOB` for additional exclusions, and `--max-source-bytes N` for a source-read bound. Parsing failures appear as exception types, not source excerpts. Directory access gaps are marked. The mapper does not apply `.gitignore`, inspect runtime behavior, or enumerate non-Python symbols. Outputs can still reveal proprietary names; keep them private unless disclosure is approved.

## Trust boundary

Mapping is read-only except for the requested new map file. It never imports repository code and skips symlinks, hidden entries, common caches, and sensitive filename patterns. It is not a secret scanner or a sandbox for hostile concurrent filesystem changes. Review names and context content before sharing; analysis does not authorize edits or publication.

## Validation

From this repository root:

```sh
python3 -m unittest discover -s tests -v
```

Tests use clearly synthetic temporary fixtures, not user data or claimed experimental results. If the official skill-creator validator is installed in your environment, run its `quick_validate.py` against this directory. That checks skill packaging, not the truth of a review or the effectiveness of the workflow.

See [SECURITY.md](SECURITY.md), [CONTRIBUTING.md](CONTRIBUTING.md), and [CHANGELOG.md](CHANGELOG.md).
