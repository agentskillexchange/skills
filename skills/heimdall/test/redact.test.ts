/**
 * Unit tests for the secret redactor (src/redact.ts) and the applyVars → register
 * wiring. These prove the honesty claim in the report path: an `${env.*}` value is
 * tracked and scrubbed from any serialized string, even when it lands in a URL.
 */
import { afterEach, describe, expect, it } from "vitest";

import { clearSecrets, redactDeep, redactString, redactWithSpec, registerSecret, scrubHar } from "../src/redact.js";
import { applyVars } from "../src/execute.js";

afterEach(() => clearSecrets());

describe("redact", () => {
  it("scrubs a registered secret from a plain string", () => {
    registerSecret("super-secret-token");
    expect(redactString("Authorization: super-secret-token")).toBe("Authorization: [redacted]");
    // Untracked text is untouched.
    expect(redactString("nothing to see")).toBe("nothing to see");
  });

  it("ignores trivially short values so unrelated text is never corrupted", () => {
    registerSecret("ab"); // below the min length → not tracked
    expect(redactString("a tab and a cab")).toBe("a tab and a cab");
  });

  it("is a no-op when nothing is registered", () => {
    expect(redactString("anything ${env.X}")).toBe("anything ${env.X}");
    const obj = { a: ["b", { c: "d" }] };
    expect(redactDeep(obj)).toEqual(obj);
  });

  it("deep-redacts every string in a nested structure, leaving non-strings intact", () => {
    registerSecret("Bearer leaked-xyz");
    const report = {
      results: [
        {
          observed: "request failed at http://x/api?t=Bearer leaked-xyz",
          status: 200,
          evidence: { responses: [{ url: "/api?t=Bearer leaked-xyz", status: 200 }] },
          failures: ["timeout hitting /api?t=Bearer leaked-xyz"],
        },
      ],
    };
    const out = redactDeep(report);
    expect(JSON.stringify(out)).not.toContain("leaked-xyz");
    expect(out.results[0]!.evidence.responses[0]!.url).toBe("/api?t=[redacted]");
    // Numbers and shape survive.
    expect(out.results[0]!.status).toBe(200);
    expect(out.results[0]!.evidence.responses[0]!.status).toBe(200);
  });

  it("applyVars registers an env-resolved value so the redactor can later scrub it", () => {
    const KEY = "HEIMDALL_REDACT_TEST";
    process.env[KEY] = "env-resolved-secret";
    try {
      const url = applyVars("/api?token=${env.HEIMDALL_REDACT_TEST}", {});
      expect(url).toBe("/api?token=env-resolved-secret");
      // The very value spliced into the URL is now redactable everywhere.
      expect(redactString(url)).toBe("/api?token=[redacted]");
    } finally {
      delete process.env[KEY];
    }
  });
});

describe("redactWithSpec", () => {
  it("masks the value of a configured header key (case-insensitive)", () => {
    const out = redactWithSpec(
      { headers: { Authorization: "Bearer abc", "content-type": "application/json" } },
      { headers: ["authorization"] },
    );
    expect(out.headers.Authorization).toBe("[redacted]");
    // Unlisted headers survive untouched.
    expect(out.headers["content-type"]).toBe("application/json");
  });

  it("replaces every regex-pattern match in any string", () => {
    const out = redactWithSpec({ note: "api key sk-abc123 leaked", n: 7 }, { patterns: ["sk-[a-z0-9]+"] });
    expect(out.note).toBe("api key [redacted] leaked");
    // Non-strings are preserved.
    expect(out.n).toBe(7);
  });

  it("still scrubs env-registered secrets even when a spec is supplied", () => {
    registerSecret("topsecretvalue");
    const out = redactWithSpec({ a: "x topsecretvalue y" }, { headers: ["authorization"] });
    expect(out.a).toBe("x [redacted] y");
  });

  it("is byte-identical to legacy redactDeep when the spec is omitted", () => {
    registerSecret("leakme123");
    const obj = { a: ["leakme123", { b: "ok" }], n: 1 };
    expect(JSON.stringify(redactWithSpec(obj))).toBe(JSON.stringify(redactDeep(obj)));
  });

  it("returns the identical reference (no copy) when there is nothing to scrub", () => {
    const obj = { a: "b" };
    // No secrets, no spec → same legacy fast-path identity as redactDeep.
    expect(redactWithSpec(obj)).toBe(redactDeep(obj));
  });
});

describe("scrubHar", () => {
  function craftHar() {
    return {
      log: {
        version: "1.2",
        entries: [
          {
            request: {
              url: "https://api.example.com/u?email=jane@doe.com",
              headers: [
                { name: "Authorization", value: "Bearer xyz" },
                { name: "Accept", value: "application/json" },
              ],
              postData: { text: "email=jane@doe.com&ok=1" },
            },
            response: {
              headers: [{ name: "Set-Cookie", value: "sid=abc" }],
              content: { text: "contact jane@doe.com now" },
            },
          },
        ],
      },
    };
  }

  it("blanks configured header values and regex-matches in URLs/bodies, emitting valid JSON", () => {
    const har = craftHar();
    const out = scrubHar(har, { headers: ["authorization", "set-cookie"], patterns: ["[a-z]+@[a-z.]+"] }) as ReturnType<
      typeof craftHar
    >;
    const json = JSON.stringify(out);
    // Still valid, parseable JSON.
    expect(() => JSON.parse(json)).not.toThrow();
    // PII pattern scrubbed from URL + request body + response body.
    expect(json).not.toContain("jane@doe.com");
    // Configured header values blanked in both request and response.
    expect(json).not.toContain("Bearer xyz");
    expect(json).not.toContain("sid=abc");
    // Unlisted header preserved.
    expect(out.log.entries[0]!.request.headers[1]!.value).toBe("application/json");
    // Pure: the input object is left unmutated.
    expect(har.log.entries[0]!.request.headers[0]!.value).toBe("Bearer xyz");
    expect(har.log.entries[0]!.request.url).toContain("jane@doe.com");
  });

  it("never throws on absent/odd fields", () => {
    expect(() => scrubHar({}, { headers: ["x"], patterns: ["y"] })).not.toThrow();
    expect(() => scrubHar({ log: { entries: [{}, null] } }, {})).not.toThrow();
    expect(() => scrubHar(null)).not.toThrow();
    expect(() => scrubHar({ log: { entries: "not-an-array" } }, { patterns: ["z"] })).not.toThrow();
  });
});
