/**
 * Self-contained HTML report — one file you can open or share, with screenshots
 * inlined as base64 so there are no external dependencies.
 */
import { readFile, writeFile } from "node:fs/promises";
import { basename } from "node:path";
import type { Result, RunReport } from "../schema.js";
import { groupResults, type ReportFormatOptions } from "../reporter.js";

const esc = (s: string): string =>
  s.replace(/[&<>"']/g, (ch) => ({ "&": "&amp;", "<": "&lt;", ">": "&gt;", '"': "&quot;", "'": "&#39;" })[ch]!);

const STATUS_COLOR: Record<Result["status"], string> = {
  pass: "#1a7f37",
  fail: "#cf222e",
  error: "#cf222e",
  blocked: "#9a6700",
  skipped: "#6e7781",
};

async function inlineScreenshot(path: string): Promise<string | undefined> {
  try {
    const buf = await readFile(path);
    return `data:image/png;base64,${buf.toString("base64")}`;
  } catch {
    return undefined;
  }
}

async function renderCase(r: Result): Promise<string> {
  const color = STATUS_COLOR[r.status];
  const shot = r.evidence.screenshots.at(-1);
  const dataUri = shot ? await inlineScreenshot(shot) : undefined;
  const failures = r.failures.length
    ? `<ul class="failures">${r.failures.map((f) => `<li>${esc(f)}</li>`).join("")}</ul>`
    : "";
  const consoleErrs = r.evidence.consoleErrors.length
    ? `<details><summary>${r.evidence.consoleErrors.length} console error(s)</summary><pre>${esc(
        r.evidence.consoleErrors.join("\n"),
      )}</pre></details>`
    : "";
  const responses = r.evidence.responses.length
    ? `<details><summary>${r.evidence.responses.length} response(s)</summary><pre>${esc(
        r.evidence.responses.map((x) => `${x.status} ${x.method} ${x.url}`).join("\n"),
      )}</pre></details>`
    : "";
  const img = dataUri
    ? `<a href="${dataUri}" target="_blank"><img src="${dataUri}" alt="${esc(r.id)} screenshot"/></a>`
    : "";
  const artifacts = [
    r.evidence.trace ? `trace: <code>${esc(r.evidence.trace)}</code>` : "",
    r.evidence.video ? `video: <code>${esc(r.evidence.video)}</code>` : "",
    r.evidence.har ? `har: <code>${esc(r.evidence.har)}</code>` : "",
  ]
    .filter(Boolean)
    .join(" · ");
  const artifactLine = artifacts ? `<p class="artifacts">${artifacts}</p>` : "";
  const attempts = r.attempts && r.attempts > 1 ? `<span class="badge">×${r.attempts}</span>` : "";

  return `<section class="case ${r.status}">
    <header>
      <span class="status" style="background:${color}">${r.status.toUpperCase()}</span>
      <h3>${esc(r.id)}</h3>
      <span class="meta">${esc(r.driver)} · ${esc(r.fidelityTier)} · ${r.durationMs}ms</span>${attempts}
    </header>
    <p class="observed">${esc(r.observed)}</p>
    ${failures}${consoleErrs}${responses}${artifactLine}
    ${img}
  </section>`;
}

function tally(results: Result[]): { pass: number; fail: number } {
  let pass = 0;
  let fail = 0;
  for (const r of results) {
    if (r.status === "pass") pass++;
    else if (r.status === "fail" || r.status === "error") fail++;
  }
  return { pass, fail };
}

export async function buildHtml(report: RunReport, opts?: ReportFormatOptions): Promise<string> {
  const s = report.summary;

  // Body: flat by default, or grouped sections when a grouping is requested.
  let body: string;
  if (opts?.groupBy) {
    const groups = groupResults(report.results, opts.groupBy, opts.meta);
    const sections = await Promise.all(
      groups.map(async ([label, rs]) => {
        const rendered = (await Promise.all(rs.map(renderCase))).join("\n");
        const t = tally(rs);
        return `<section class="group">
    <h2 class="group-h">${esc(opts.groupBy!)}: ${esc(label)} <span class="grouptally">${t.pass} pass · ${t.fail} fail · ${rs.length} total</span></h2>
    ${rendered}
  </section>`;
      }),
    );
    body = sections.join("\n");
  } else {
    body = (await Promise.all(report.results.map(renderCase))).join("\n");
  }

  // Prominent rundown of everything that did not run (opt-in, keeps default bytes intact).
  const showBlocked = opts ? opts.blocked !== false : false;
  const deferred = report.results.filter((r) => r.status === "blocked" || r.status === "skipped");
  const blockedPanel =
    showBlocked && deferred.length
      ? `<section class="blocked-panel">
    <h2>Blocked (${deferred.length})</h2>
    <ul>${deferred
      .map(
        (r) =>
          `<li><strong>${esc(r.id)}</strong> <em>[${esc(r.status)}]</em> — ${esc(
            r.observed || r.notes || "(no reason given)",
          )}</li>`,
      )
      .join("")}</ul>
  </section>`
      : "";

  // Extra CSS only emitted when options are supplied, so the default document is unchanged.
  const extraCss = opts
    ? `
  .group { margin-bottom: 1.5rem; }
  .group-h { font-size: 1rem; border-bottom: 1px solid #d0d7de; padding-bottom: .35rem; }
  .grouptally { color: #6e7781; font-size: .8rem; font-weight: 400; }
  .blocked-panel { border: 1px solid #9a6700; background: #9a670011; border-radius: 8px; padding: .5rem 1rem; margin-bottom: 1.5rem; }
  .blocked-panel h2 { margin: .25rem 0 .5rem; font-size: 1rem; color: #9a6700; }
  .blocked-panel ul { margin: 0; padding-left: 1.2rem; }
  .blocked-panel em { color: #9a6700; font-style: normal; }`
    : "";

  const middle = blockedPanel ? `${blockedPanel}\n  ${body}` : body;

  return `<!doctype html>
<html lang="en"><head><meta charset="utf-8"/>
<meta name="viewport" content="width=device-width, initial-scale=1"/>
<title>Heimdall — ${esc(report.plan)}</title>
<style>
  :root { color-scheme: light dark; }
  body { font: 14px/1.5 -apple-system, system-ui, sans-serif; margin: 0; padding: 2rem; max-width: 960px; margin-inline: auto; }
  h1 { margin: 0 0 .25rem; }
  .sub { color: #6e7781; margin: 0 0 1.5rem; }
  .summary { display: flex; gap: .5rem; flex-wrap: wrap; margin-bottom: 1.5rem; }
  .pill { padding: .25rem .6rem; border-radius: 999px; font-weight: 600; background: #eaeef2; }
  .pill.pass { background: #1a7f3722; color: #1a7f37; }
  .pill.fail, .pill.error { background: #cf222e22; color: #cf222e; }
  .pill.blocked { background: #9a670022; color: #9a6700; }
  .case { border: 1px solid #d0d7de; border-radius: 8px; padding: 1rem; margin-bottom: 1rem; }
  .case header { display: flex; align-items: center; gap: .6rem; }
  .case h3 { margin: 0; font-size: 1rem; }
  .status { color: #fff; padding: .1rem .5rem; border-radius: 4px; font-size: .75rem; font-weight: 700; }
  .meta { color: #6e7781; font-size: .8rem; }
  .badge { background: #6e7781; color: #fff; border-radius: 4px; padding: 0 .35rem; font-size: .75rem; }
  .observed { color: #57606a; }
  .failures { color: #cf222e; margin: .5rem 0; }
  img { max-width: 100%; border: 1px solid #d0d7de; border-radius: 6px; margin-top: .5rem; }
  pre { background: #f6f8fa; padding: .5rem; border-radius: 6px; overflow: auto; }
  details { margin: .35rem 0; }
  .artifacts { font-size: .8rem; color: #57606a; }
  code { background: #f6f8fa; padding: 0 .3rem; border-radius: 4px; }${extraCss}
</style></head>
<body>
  <h1>Heimdall — ${esc(report.plan)}</h1>
  <p class="sub">${esc(report.startedAt)} · ${report.durationMs}ms · v${esc(report.heimdallVersion)}</p>
  <div class="summary">
    <span class="pill pass">${s.pass} pass</span>
    <span class="pill fail">${s.fail} fail</span>
    <span class="pill error">${s.error} error</span>
    <span class="pill blocked">${s.blocked} blocked</span>
    <span class="pill">${s.skipped} skipped</span>
    <span class="pill">of ${s.total}</span>
  </div>
  ${middle}
</body></html>`;
}

export async function writeHtmlReport(
  report: RunReport,
  htmlPath: string,
  opts?: ReportFormatOptions,
): Promise<string> {
  await writeFile(htmlPath, await buildHtml(report, opts), "utf8");
  return basename(htmlPath);
}
