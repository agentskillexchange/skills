---
name: "Thermal Machinery Dynamic Modeling"
slug: "thermal-machinery-dynamic-modeling"
description: "Guides an AI agent through topology, stream ledgers, component contracts, steady-state closure, dynamic initialization, and validation for thermal-power and energy-conversion models in MATLAB/Simulink."
category: "Templates & Workflows"
framework: "Multi-Framework"
verification: "listed"
source: "https://github.com/YYch89/thermal-machinery-ai-skills"
---

# Thermal Machinery Dynamic Modeling

Use this skill for a thermal-power or energy-conversion model that needs more discipline than a direct equation or block-diagram request. It covers Brayton and Rankine cycles, refrigeration and heat-pump systems, compressors, turbines, combustors, heat exchangers, recuperators, and coupled thermo-fluid plants. The workflow begins with topology and a node-by-node stream ledger, so every temperature, pressure, flow, composition or phase variable, unit, source, and calculation status is visible. It then defines component contracts, balances, dynamic storage states, and the mapping from a design or steady solution into Simulink initial conditions. The skill makes the requested model depth explicit and requires mass, energy, pressure, state-consistency, constraint, and provenance checks before control or optimization conclusions are claimed.

## Workflow

1. Set the model boundary, fluids, topology, required depth, control objective, and evidence available.
2. Create stream ledgers and component contracts before selecting equations or implementation blocks.
3. Establish design-point or steady closure and identify which quantities become dynamic states, parameters, lookup tables, or controller references.
4. Add only physically justified storage and actuator dynamics, then validate balances, initialization residuals, constraints, and data provenance.
5. Document assumptions and open gates rather than treating a successful simulation as proof of a validated plant.

## Installation

Install the upstream, maintained skill collection with the verified `skills` CLI command:

```bash
npx skills add YYch89/thermal-machinery-ai-skills --skill thermal-machinery-dynamic-modeling
```

For manual installation, clone the upstream repository and copy `skills/thermal-machinery-dynamic-modeling/` into the skill directory used by the selected agent. The upstream repository supplies linked references and a compact synthetic heat-pump ledger example; it does not claim certified engineering models.
