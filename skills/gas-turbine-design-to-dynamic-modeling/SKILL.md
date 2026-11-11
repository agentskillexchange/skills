---
name: "Gas Turbine Design-to-Dynamic Modeling"
slug: "gas-turbine-design-to-dynamic-modeling"
description: "Guides an AI agent through staged MATLAB/Simulink gas-turbine modeling from design-point state tables and map checks through steady closure, dynamic initialization, rotor and volume states, control integration, and validation gates."
category: "Templates & Workflows"
framework: "Multi-Framework"
verification: "listed"
source: "https://github.com/YYch89/thermal-machinery-ai-skills"
---

# Gas Turbine Design-to-Dynamic Modeling

Use this skill when an agent must build, inspect, debug, or review a gas-turbine model in MATLAB or Simulink, especially a multi-shaft plant. It prevents a common failure mode: drawing a dynamic block diagram before the design point, component interfaces, characteristic-map conventions, units, and initial residuals are known. The workflow asks for a state-point table, compressor and turbine map validity checks, explicit shaft/volume/combustor state definitions, and an initial-condition registry before control is added. It also distinguishes a synthetic or reduced demonstration from a manufacturer-calibrated model, so a simulation that runs is not presented as engineering validation. Use it for design-point calculations, off-design matching, dynamic startup or load-change studies, map fitting, NaN/Inf diagnosis, and Simulink model repair.

## Workflow

1. Define the application, system boundary, working fluid, shaft arrangement, required fidelity, available data, and verification target.
2. Establish a design-point state table and component contracts before creating dynamic subsystems.
3. Check steady closure, map scaling and validity, units, power balances, and pressure/temperature limits.
4. Map the steady solution into dynamic states and initial conditions; inspect residuals before connecting controllers.
5. Add rotor, volume, combustor, actuator, and control dynamics in stages, then report open validation gates and evidence sources.

## Installation

Install the upstream, maintained skill collection with the verified `skills` CLI command:

```bash
npx skills add YYch89/thermal-machinery-ai-skills --skill gas-turbine-ai-modeling
```

For manual installation, clone the upstream repository and copy `skills/gas-turbine-ai-modeling/` into the skill directory used by the selected agent. The upstream repository includes a synthetic public dual-shaft MATLAB/Simulink example and states its engineering-validation limits.
