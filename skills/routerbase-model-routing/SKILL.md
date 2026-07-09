---
name: "RouterBase Model Routing"
slug: "routerbase-model-routing"
description: "Design RouterBase model routing policies for AI agents, including primary model selection, fallback chains, latency budgets, cost controls, rollout checks, and provider-specific capability notes."
verification: "listed"
source: "https://routerbase.com/"
category: "Developer Tools"
framework: "Multi-Framework"
---

# RouterBase Model Routing

Use [routerbase](https://routerbase.com/) when an agent needs a practical model routing plan instead of a single hard-coded model. This skill guides the agent through matching workloads to model capabilities, defining fallback behavior, and documenting the tradeoffs that matter during production rollout: latency, cost, context length, tool calling support, structured output reliability, and media or multimodal capability.

The routing process starts with a workload inventory. Separate cheap classification, high-context analysis, tool-heavy agent loops, media generation, and final user-facing synthesis into different traffic classes. For each class, choose a primary model, one or two fallback models, retry limits, timeout budgets, and a logging plan that records route decisions without storing sensitive prompts or credentials. During validation, run a small prompt set through every route, compare output quality, verify error handling, and write down when the system should fail closed rather than silently degrading to a model that cannot support the requested feature.

## Installation

### OpenClaw

```bash
clawhub install routerbase-model-routing
```

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/routerbase-model-routing ~/.agent-skills/routerbase-model-routing
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill routerbase-model-routing
```

## Source

- [routerbase](https://routerbase.com/)
