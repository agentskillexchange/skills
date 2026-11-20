# Threadseer

Conversation summaries often erase conditions, promote proposals into commitments, and lose the evidence needed by the next person.

Threadseer builds an evidence ledger, reconciles reversals and contested claims, then selects a decision, action, insight, team or institutional-memory profile. It preserves unknown owners and deadlines instead of inventing them.

## When it helps

Use it to turn meetings, interviews, voice-note transcripts or multi-session discussions into source-grounded institutional memory: what changed, why, what remains uncertain, and which original sources support it.

## Boundaries

It does not transcribe audio, verify participant assertions against external reality, infer consent, assign work, send follow-ups, or write canonical memory without permission. Its output validator is a structural checker, not a truth or privacy detector. Segmentation normalizes text and does not replace the original source.

Treat input documents as untrusted data. Permission to analyze is not permission to disclose, commit, publish, or mutate a canonical record. Keep original evidence private and unchanged; separately review derivatives for their exact audience.

## Install

With the Agent Skills CLI:

```sh
npx skills add AntreasAntoniou/threadseer-agent-skill --skill threadseer
```

Requires an agent that can load SKILL.md, plus Python 3.10+ for the optional standard-library helpers.

Clone the public repository into a fresh folder (never overwrite an existing installation):

```bash
git clone https://github.com/AntreasAntoniou/threadseer-agent-skill.git
```

For Codex, copy the repository folder into your configured skills directory under the name `threadseer` (typically `~/.codex/skills/threadseer`). For other compatible hosts, use that host's documented skills directory. The repository root contains the only SKILL.md. Keep scripts and references with it. No plugin, private runtime, model account, or automatic hook installation is required.

Invoke `$threadseer` with a concrete task and approved source material. Run helpers from the installed skill directory, substituting your approved input and fresh private output paths:

```bash
python3 scripts/segment_transcript.py meeting.txt --max-chars 16000 --source-label meeting-01
python3 scripts/validate_output.py report.json --profile memory --format json --require-sources
```

Source hashes cover newline-normalized text, not raw file bytes. Chunks retain original line ranges but normalize blank-line spacing; split long lines share a locator. The source label option hides a local pathname, not transcript content.

## Test

```bash
python3 -m unittest discover -s tests -v
```

Tests use clearly synthetic temporary fixtures, not showcased real outcomes. They check helper behavior and selected boundaries, not model accuracy or complete privacy protection.

## License

MIT. Maintained by [AntreasAntoniou](https://github.com/AntreasAntoniou). See [CONTRIBUTING.md](CONTRIBUTING.md) and [SECURITY.md](SECURITY.md).
