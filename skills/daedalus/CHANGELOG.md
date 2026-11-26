# Changelog

## 1.1.0 — 2026-11-13

- Corrects the incomplete 1.0.0 bundle: restores the original map-first workflow and includes `map_directory.py`, `ingest_content.py` and `ingest_github_repo.py`.
- Preserves the mapper's directory tree and top-level Python class/function outlines, local content concatenation, and shallow repository ingestion with branch and extension selection.
- Replaces private absolute script paths with paths relative to the installed skill, and adds pinned Fire/Rich requirements and runnable Python 3.14 examples.
- Skips symlinks and the tools' own output files; sorts map entries; excludes Git metadata from remote ingestion and separates clone options from the repository argument.
- Adds CLI integration tests for mapping, ingestion, filtering, branch selection, help and traversal boundaries. Retains the original ARISE reference and Codex metadata.

## 1.0.0 — 2026-11-13

- First standalone public edition of Daedalus.
- Includes deliberate implementation, refactoring, debugging and measurement workflows.
- Retains reader-focused naming, function contracts, README guidance and Python conventions.
- Generalizes owner-specific wording and replaces the private mapper with a portable Git inventory.
- Bundles the optional ARISE entrance and Codex display metadata.
- Documents installation, permissions, dependencies and evidence limits.
