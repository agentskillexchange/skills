import { describe, it, expect, beforeAll, afterAll } from "vitest";
import { mkdtemp, rm, writeFile } from "node:fs/promises";
import { tmpdir } from "node:os";
import { join } from "node:path";
import { buildExtensionManifest, loadExternalResults } from "../src/commands/extensions.js";
import { parsePlan } from "../src/schema.js";

describe("buildExtensionManifest", () => {
  it("emits ONLY the extension-driver cases (plan default + per-case override), with their steps/oracles + a tap hint", () => {
    const plan = parsePlan({
      name: "mixed",
      defaultDriver: "cdp",
      baseUrl: "http://sut.local",
      cases: [
        // cdp by inheritance — excluded
        { id: "api", steps: [{ action: "fetch", url: "/x", as: "r" }], oracle: [{ assert: "status", equals: 200, of: "r" }] },
        // explicit extension — included, has a goto for the tap-hint start URL
        {
          id: "login-ui",
          title: "Log in as the real user",
          driver: "extension",
          steps: [{ action: "goto", url: "/login" }, { action: "click", selector: "#go" }],
          oracle: [{ assert: "visible", selector: "#dash" }],
        },
        // container — excluded
        { id: "ctr", driver: "container", steps: [{ action: "goto", url: "/" }], oracle: [{ assert: "visible", selector: "body" }] },
      ],
    });

    const m = buildExtensionManifest(plan);
    expect(m.driver).toBe("extension");
    expect(m.plan).toBe("mixed");
    expect(m.cases.map((c) => c.id)).toEqual(["login-ui"]); // ONLY the extension case
    const only = m.cases[0]!;
    expect(only.title).toBe("Log in as the real user");
    expect(only.steps).toHaveLength(2);
    expect(only.oracle).toHaveLength(1);
    // tap hint names the case and the goto start URL + step/oracle counts
    expect(only.tapHint).toContain("Log in as the real user");
    expect(only.tapHint).toContain("/login");
    expect(only.tapHint).toContain("2 step(s) + 1 oracle(s)");
  });

  it("returns an empty case list when no case resolves to the extension driver", () => {
    const plan = parsePlan({
      name: "none",
      defaultDriver: "cdp",
      cases: [{ id: "a", steps: [{ action: "goto", url: "/" }], oracle: [{ assert: "visible", selector: "body" }] }],
    });
    expect(buildExtensionManifest(plan).cases).toEqual([]);
  });
});

describe("loadExternalResults", () => {
  let dir: string;
  beforeAll(async () => {
    dir = await mkdtemp(join(tmpdir(), "heimdall-ext-results-"));
  });
  afterAll(async () => {
    if (dir) await rm(dir, { recursive: true, force: true }).catch(() => {});
  });

  const aResult = {
    id: "login-ui",
    status: "pass",
    driver: "extension",
    fidelityTier: "high",
    observed: "driven by the agent in real Chrome",
    failures: [],
    evidence: { screenshots: [], consoleErrors: [], responses: [] },
    durationMs: 1234,
  };

  it("accepts a bare Result[] array and validates it against the schema", async () => {
    const f = join(dir, "bare.json");
    await writeFile(f, JSON.stringify([aResult]), "utf8");
    const out = await loadExternalResults(f);
    expect(out).toHaveLength(1);
    expect(out[0]!.id).toBe("login-ui");
    expect(out[0]!.fidelityTier).toBe("high");
  });

  it("also accepts a { results: [...] } RunReport-shaped wrapper", async () => {
    const f = join(dir, "wrapped.json");
    await writeFile(f, JSON.stringify({ results: [aResult] }), "utf8");
    const out = await loadExternalResults(f);
    expect(out.map((r) => r.id)).toEqual(["login-ui"]);
  });

  it("rejects a file whose results are not valid Result objects (no silent garbage in)", async () => {
    const f = join(dir, "bad.json");
    await writeFile(f, JSON.stringify([{ id: "x", status: "totally-made-up" }]), "utf8");
    await expect(loadExternalResults(f)).rejects.toThrow();
  });
});
