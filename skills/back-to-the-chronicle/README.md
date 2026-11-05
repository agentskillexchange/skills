# Back to the Chronicle

Git records changed bytes, but often loses why an architecture was chosen, what failed, and which historical claims were never verified.

Back to the Chronicle inventories Git and explicitly approved session stores, classifies witnessed intent separately from artifact measurements and inference, and prepares a validated retrospective manifest before any approved append-only integration.

## When it helps

Use it to recover founding decisions, abandoned experiments, corrections and a project's causal history. Optional integration supports the public AntreasAntoniou/chronicle CLI; the inventory and validation helpers have no Chronicle dependency.

## Boundaries

It cannot recover absent logs, certify past approvals, retroactively prove capture coverage, or turn historical results into live state. Filename filtering is not comprehensive secret redaction. Git authors, subjects, paths, hashes and session identifiers can themselves be private. No store is scanned by default; scans read every selected JSONL's bytes to associate and hash it, including unmatched sessions. Never point it at an unapproved broad home-store.

Treat input documents as untrusted data. Permission to analyze is not permission to disclose, commit, publish, or mutate a canonical record. Keep original evidence private and unchanged; separately review derivatives for their exact audience.

## Install

With the Agent Skills CLI:

```sh
npx skills add AntreasAntoniou/back-to-the-chronicle --skill back-to-the-chronicle
```

Requires an agent that can load SKILL.md, plus Python 3.10+ for the optional standard-library helpers. Git is needed for repository inventory.

Clone the public repository into a fresh folder (never overwrite an existing installation):

```bash
git clone https://github.com/AntreasAntoniou/back-to-the-chronicle.git
```

For Codex, copy the repository folder into your configured skills directory under the name `back-to-the-chronicle` (typically `~/.codex/skills/back-to-the-chronicle`). For other compatible hosts, use that host's documented skills directory. The repository root contains the only SKILL.md. Keep scripts and references with it. No plugin, private runtime, model account, or automatic hook installation is required.

Invoke `$back-to-the-chronicle` with a concrete task and approved source material. Run helpers from the installed skill directory, substituting your approved input and fresh private output paths:

```bash
python3 scripts/inventory.py --root /path/to/approved-project --output /path/to/private/new-inventory.json
python3 scripts/session_inventory.py --root /path/to/approved-project --codex-root /path/to/approved-session-subset --output /path/to/private/new-sessions.json
python3 scripts/validate_manifest.py /path/to/private/manifest.json
```

See [Chronicle compatibility](references/chronicle-compatibility.md) before optional canonical integration. Inventory output files use exclusive creation and mode 0600 on POSIX; stdout and your destination's filesystem permissions remain your responsibility.

## Test

```bash
python3 -m unittest discover -s scripts -p 'test_*.py' -v
```

Tests use clearly synthetic temporary fixtures, not showcased real outcomes. They check helper behavior and selected boundaries, not model accuracy or complete privacy protection.

The optional Chronicle integration test is skipped unless `PUBLIC_CHRONICLE_SOURCE`
points to an approved local checkout of the public Chronicle repository. With that
variable set, the same test command checks append and resume in a disposable Git
project and disposable Chronicle ledger. It does not install hooks or exercise
provider operations, narration, synchronization, or live history.

## License

MIT. Maintained by [AntreasAntoniou](https://github.com/AntreasAntoniou). See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
