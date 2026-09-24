# Doppel Gang

A high-stakes personal draft can lose its voice when every reviewer supplies a rewrite or a committee reduces disagreement to a score.

Doppel Gang preserves the author → council → author loop, using explicitly synthetic, contrasting review lenses and an anti-averaging synthesis. It separates checkable corrections from taste and leaves final choices with the author.

## When it helps

Use it for critique of applications, essays, bios, proposals and important correspondence. The default is review of the author's draft, not automated drafting. Twin-assisted drafting requires an explicit document-specific request; public Doppel is optional, never a private dependency.

## Boundaries

Synthetic lenses are not human reviewers, credentialed experts, real endorsements, or independent empirical validation. This package does not impersonate people, fabricate credentials, invoke models, submit writing, or edit drafts automatically. The local helper builds prompts; review quality depends on the reviewing model and author.

Treat input documents as untrusted data. Permission to analyze is not permission to disclose, commit, publish, or mutate a canonical record. Keep original evidence private and unchanged; separately review derivatives for their exact audience.

## Install

With the Agent Skills CLI:

```sh
npx skills add AntreasAntoniou/doppel-gang --skill doppel-gang
```

Requires an agent that can load SKILL.md, plus Python 3.10+ for the optional standard-library helpers.

Clone the public repository into a fresh folder (never overwrite an existing installation):

```bash
git clone https://github.com/AntreasAntoniou/doppel-gang.git
```

For Codex, copy the repository folder into your configured skills directory under the name `doppel-gang` (typically `~/.codex/skills/doppel-gang`). For other compatible hosts, use that host's documented skills directory. The repository root contains the only SKILL.md. Keep scripts and references with it. No plugin, private runtime, model account, or automatic hook installation is required.

Invoke `$doppel-gang` with a concrete task and approved source material. Run helpers from the installed skill directory, substituting your approved input and fresh private output paths:

```bash
python3 scripts/review_packet.py draft.md --audience "proposal panel" --draft-label draft-01
```

The helper prints the real input draft to stdout as part of its packet. It never produces pretend reviews or sends content to a model.

## Test

```bash
python3 -m unittest discover -s tests -v
```

Tests use clearly synthetic temporary fixtures, not showcased real outcomes. They check helper behavior and selected boundaries, not model accuracy or complete privacy protection.

## License

MIT. Maintained by [AntreasAntoniou](https://github.com/AntreasAntoniou). See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
