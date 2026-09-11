# Five skills around agent graphs and graph-grounded work

Two different structures are often called an “agent graph”:

1. A **work graph** describes execution: which agents branch, what each may see, where evidence is challenged, and who integrates the result.
2. A **knowledge graph** describes durable state: entities, typed relations, provenance, and the paths used to support a claim.

Anthropic's March 2026 [Knowledge Graph Construction with Claude](https://platform.claude.com/cookbook/capabilities-knowledge-graph-guide) cookbook is an example of the second structure. It covers structured entity and relation extraction, entity resolution, graph assembly, multi-hop querying, and precision/recall evaluation.

Andrej Karpathy's [`autoresearch`](https://github.com/karpathy/autoresearch) is a separate primary source: a bounded autonomous loop with a human-authored `program.md`, one mutable training file, a fixed five-minute budget per experiment, and a measurable keep-or-discard decision.

A recent, independently compiled “Graph Engineering” synthesis combined these threads and was subsequently circulated as a Karpathy or Anthropic publication. It is neither. The distinction matters because provenance is one of the properties graph-grounded systems are meant to preserve.

The five skills below are an unaffiliated control layer for the **work graph** around agent activity. They do not implement Anthropic's knowledge-graph cookbook, and they have not been tested as an integration with it or with `autoresearch`.

| Skill | Role in the work graph | Boundary |
| --- | --- | --- |
| [Agent Orchestra](https://github.com/AntreasAntoniou/agent-orchestra) | Defines isolated roles, parallel lanes, dependencies, adversarial review, and one integration owner. | It is an orchestration grammar, not a graph database or entity extractor. |
| [Plus Ultra](https://github.com/AntreasAntoniou/plus-ultra) | Separates proposal, arbitration, mutation, and plan-blind reality verification. | It does not turn model judgment into factual ground truth by itself. |
| [Cross Agent Sync](https://github.com/AntreasAntoniou/cross-agent-sync) | Preserves concise source-linked hand-offs across harnesses and sessions. | Its ledger is not a shared knowledge graph or a claim of shared agent memory. |
| [Visual QA](https://github.com/AntreasAntoniou/visual-qa) | Adds deterministic rendered evidence and independent review when the output has a UI. | It evaluates visible artefacts, not graph extraction quality. |
| [Doppel](https://github.com/AntreasAntoniou/doppel) | Builds a local, consent-first digital twin of the subject's writing voice for subject-ratified prose. | It is not a whole-person simulation, autonomous publication, third-party impersonation, or a public voice corpus. |

## Puzzle-piece view

```text
                         durable knowledge
                entities + relations + provenance
                              ▲
                              │ evidence can be grounded here
                              │
human objective ──► Agent Orchestra ──► isolated work graph
                              │
                         Plus Ultra
                  propose → arbitrate → apply
                              │
                    fresh reality verification
                       ┌──────┴──────┐
                Cross Agent Sync   Visual QA
                durable hand-off   rendered evidence
                       └──────┬──────┘
                             Doppel
               local evidence → human-ratified words
```

The composition is optional. Use a knowledge graph only when relationships, multi-hop reasoning, or cross-session provenance justify it. Use a multi-agent work graph only when branches create genuinely independent evidence. A small linear task should remain small and linear.
