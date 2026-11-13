/**
 * Heimdall public API — import the runner and schemas to embed Heimdall in your
 * own tooling (e.g. the live-test skill builds plans and calls `runPlan`).
 */
export * from "./schema.js"; // includes parsePlan, planJsonSchema, and all types
export { runPlan, type RunOptions } from "./runner.js";
export { evaluateOracles, getByPath, type Observation, type ObservedResponse } from "./oracle.js";
export {
  formatReport,
  exitCodeFor,
  groupResults,
  type ReportFormatOptions,
  type CaseMeta,
} from "./reporter.js";
export {
  diffReports,
  formatDiff,
  isCleanDiff,
  writeDiffReport,
  type RegressionDiff,
  type DiffCase,
} from "./reporters/diff.js";
export { loadConfig, HeimdallConfig } from "./config.js";
export { VERSION } from "./version.js";
// Accessibility (axe) + visual-diff oracles, exposed for embedders/the live-test skill.
export { runAxe, filterViolations, type A11yReport, type AxeViolation, type AxeNode, type AxeBridge, type AxeResultLike, type AxeContextOptions, type Impact } from "./a11y.js";
export { comparePng, DimensionMismatchError, type PngCompareResult, type PngCompareOptions } from "./visualDiff.js";
// Extension-manifest emitter + the --merge-results loader for externally-produced results.
export {
  buildExtensionManifest,
  loadExternalResults,
  type ExtensionManifest,
  type ExtensionManifestCase,
} from "./commands/extensions.js";
