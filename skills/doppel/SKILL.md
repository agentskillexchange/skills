---
name: "Doppel — Digital Twin Writing Voice"
slug: "doppel"
description: "Build a consent-first, provenance-aware digital twin of a person's own writing voice from local subject-authored material, then use that writing-voice Doppel to draft or revise text for the subject's review. Use when someone wants a digital twin of their own cadence, reasoning movement, and registers across essays, technical writing, outreach, or social posts without uploading a private corpus. Not a personality twin, believed-human simulation, third-party clone, or autonomous publisher."
category: "Content Writing & SEO"
framework: "Codex"
verification: "listed"
source: "https://github.com/AntreasAntoniou/doppel"
---

# Doppel — Digital Twin Writing Voice

Build a bounded digital twin of how a consenting person moves through writing. A Doppel models writing voice from evidence; it does not simulate the whole person. The subject remains the author and final ratifier, and every output remains a draft.

## Boundaries

- Use only material authored by the subject and supplied with explicit consent for this task.
- Refuse third-party impersonation, non-consensual cloning, deceptive attribution, or requests to speak *as* a public figure.
- Keep corpora, manifests, profiles, context packs, and drafts local and out of Git.
- Never send, submit, post, publish, or attribute a draft without the subject's approval of that exact artefact.
- Voice evidence is not fact authority. Verify current claims independently and never invent beliefs, feelings, results, or relationships.
- Avoid reproducing distinctive source phrases. Preserve movement, emphasis, cadence, and decision patterns—not memorised sentences.

Read [references/safety-and-consent.md](references/safety-and-consent.md) before handling source material.

## Workflow

1. Confirm the subject owns the source material, consents to its use, and will ratify the final text.
2. Copy `examples/voice-manifest.example.json` to an ignored local filename such as `voice-manifest.local.json`. Add subject-authored sources and their SHA-256 hashes.
3. Validate and build a deterministic, local conditioning pack:

   ```bash
   python3 scripts/build_voice_context.py \
     --manifest voice-manifest.local.json \
     --task "Explain the project launch" \
     --audience "technical peers" \
     --register public-essay \
     --output voice-context.local.md
   ```

4. Read the context pack completely. Extract recurring reasoning moves, compression/expansion patterns, boundaries, and register shifts. Treat that evidence-backed model as the writing-voice Doppel; do not reduce the person to punctuation or catchphrases.
5. Draft from the subject's intent and current facts. Label the output as a draft requiring their ratification.
6. Review twice: first for factual/semantic correctness, then for whether one mind appears to move through the piece. Remove copied phrases, invented claims, and generic polish.
7. Return the draft to the subject. Publication requires explicit approval of that exact version.

For a read-only invocation, validate sources and build the context in memory or in a temporary directory; do not leave a manifest, context pack, or draft in the source project.

For narrow edits, preserve the original structure and strongest authored lines. For a new piece, ask only for missing intent or facts that would materially change the result.

## Installation and upstream provenance

The upstream skill identifier is `doppel`. Install its instructions into a Codex project using the version-pinned, third-party Vercel Labs installer:

```bash
npx --yes skills@1.5.23 add AntreasAntoniou/doppel --skill doppel --agent codex --yes
```

Skill installation is separate from runtime setup. Read the [upstream README](https://github.com/AntreasAntoniou/doppel#readme) for required tools, platform constraints, optional integrations, and execution instructions. A successful skill install does not establish that every runtime integration has been exercised or is available on the current host. Do not install credentials, private archives, mail, writing corpora, or session logs with this package.

This contribution preserves the upstream instructions and accompanying MIT [license](LICENSE), with ASE catalogue metadata and this installation section added. The source snapshot is [`38b172dad2a4`](https://github.com/AntreasAntoniou/doppel/tree/38b172dad2a42763c1e6dd43a082800b17a37b29). The `listed` tier identifies a source-backed submission; it is not a security-review claim.
