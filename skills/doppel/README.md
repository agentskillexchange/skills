# Doppel

A consent-first Agent Skill for building a **digital twin of your own writing voice** from your own words.

An editing assistant can make a paragraph smoother while removing the way you think on the page. Doppel gives it something more concrete than “make this sound like me”: evidence of how you introduce an idea, change direction, compress an argument, or leave a thought unresolved.

Use it when you want help drafting or revising an essay, technical explanation, outreach message, or social post without handing over authorship. For example, your technical notes can guide the cadence of a release announcement while today's release facts determine what it actually says. The result is a draft for you to review—not permission for the agent to speak on your behalf.

Here, **voice means writing**. This is not audio synthesis, a personality simulation, or a claim to reproduce your private mind.

## Why the boundaries matter

Doppel separates three things that are often collapsed:

1. **Voice evidence**: subject-authored text used to learn cadence and reasoning movement.
2. **Fact authority**: current sources used to support claims.
3. **Publication authority**: the human who reviews and approves the exact final artefact.

Old writing can show how you make an argument; it cannot establish what you believe today or which claims are currently true. Keeping those authorities separate lets the agent use your prose as editorial evidence without treating it as a biography or a standing instruction to publish.

## How it works

1. You confirm consent for the task and identify subject-authored source files in a local manifest.
2. The Python helper checks the manifest's consent/authorship declarations and each source's SHA-256 hash. It ranks paragraphs by register and word overlap with the task, removes duplicate excerpts, and builds a size-bounded Markdown context pack.
3. Your agent reads that pack to infer recurring reasoning moves, cadence, emphasis, and register. It drafts from your intent and independently supported facts.
4. The agent checks meaning and voice, removes copied distinctive phrases and invented claims, and returns a draft for your approval of that exact version.

The repository provides [the skill workflow](SKILL.md), a [manifest schema](schema/voice-manifest.schema.json), the context builder, safety guidance, and synthetic tests. It does **not** ship a trained model, a drafting service, a personal voice profile, or a private corpus. The helper assembles evidence; your agent does the interpretation and writing.

The tangible outputs are a local, source-linked context pack and an agent-produced editorial draft. Only context-pack construction is deterministic; the draft and its fidelity depend on the evidence, model, and human review.

## Quick start

```bash
git clone https://github.com/AntreasAntoniou/doppel.git
cd doppel
python3 scripts/validate_package.py
cp examples/voice-manifest.example.json examples/voice-manifest.local.json
python3 scripts/build_voice_context.py --hash examples/source.example.md
```

The supplied source is synthetic and safe for a smoke test. For real use, keep your writing outside version control, point the **local manifest** at those files, update consent scope and register labels, and record each source's SHA-256. Relative source paths are resolved from the manifest's directory. Then build a context pack:

```bash
python3 scripts/build_voice_context.py \
  --manifest examples/voice-manifest.local.json \
  --task "Describe a small software release" \
  --audience "other maintainers" \
  --register technical \
  --max-chars 12000 \
  --output voice-context.local.md
```

The output is deterministic for the same manifest, source bytes, and CLI arguments. It is deliberately marked as local evidence and a draft input—not publishable prose.

## Install as a skill

```bash
npx skills add AntreasAntoniou/doppel
```

Or copy/symlink this repository into the skills directory used by your agent. The directory name should remain `doppel`, with `SKILL.md` at its root.

## Test

```bash
python3 -m unittest discover -s tests -v
python3 scripts/validate_package.py
```

The test suite creates neutral synthetic fixtures in temporary directories. It does not depend on or inspect a private corpus.

## Safety model

The workflow refuses unconsented imitation, third-party impersonation, and autonomous attribution. The helper rejects missing consent declarations, non-subject authorship declarations, and hash drift, but a manifest cannot independently prove consent or authorship. The subject must approve the exact final draft before it is sent, submitted, attributed, or published.

Keep real sources, manifests, profiles, context packs, and drafts out of Git. The builder makes no model or network calls, but local files do **not** make a hosted agent local: excerpts read by your agent may be processed by its model provider. Choose an execution environment and data policy appropriate to the material before using it.

Read [references/safety-and-consent.md](references/safety-and-consent.md) and [SECURITY.md](SECURITY.md) before handling real sources.

## Relation to other Doppels

The Doppel family covers consented digital-twin work. This public skill owns the narrow **writing-voice** layer: subject-authored evidence in, human-ratified prose out. It does not perform the believed-human embodiment, full personality simulation, dialogic reconstruction, or identity persistence associated with a whole-person doppel.

## Relation to agent and knowledge graphs

Doppel is one authorship boundary around a broader agent work graph. It does **not** implement a knowledge graph, integrate with Anthropic's knowledge-graph cookbook, or modify Karpathy's `autoresearch`. The [composition map](docs/COMPOSITION.md) distinguishes execution topology from knowledge topology and links the primary sources precisely.

## License

MIT. See [LICENSE](LICENSE).
