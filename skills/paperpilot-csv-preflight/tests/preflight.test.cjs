"use strict";
// First-party synthetic/fixture checks for the bundled FREE dependency-free
// module. Tests do not call a network service, wallet, env, or paid endpoint.
const test = require("node:test");
const assert = require("node:assert/strict");
const fs = require("node:fs");
const path = require("node:path");
const { inspectCsv, parseCsv, MAX_BYTES } = require("../scripts/csv-local-preview.cjs");
const skill = fs.readFileSync(path.join(__dirname, "..", "SKILL.md"), "utf8");
const normal = "id,name\n1,Ada\n2,Lin\n";

test("synthetic two-column CSV preserves row and header counts", () => {
  const r = inspectCsv(normal);
  assert.equal(r.ok, true);
  assert.equal(r.dataRows, 2);
  assert.equal(r.columns, 2);
  assert.equal(r.duplicateRows, 0);
  assert.equal(r.raggedRows, 0);
});
test("quoted commas stay in one cell", () => {
  const rows = parseCsv('id,comment\n1,"Hello, world"\n');
  assert.equal(rows.length, 2);
  assert.equal(rows[1][1], "Hello, world");
});
test("doubled quotes remain literal, not column separators", () => {
  const rows = parseCsv('id,comment\n1,"Ada says ""yes"""\n');
  assert.equal(rows[1][1], 'Ada says "yes"');
});
test("embedded newlines inside quotes do not create phantom trades", () => {
  assert.equal(inspectCsv('id,notes\n1,"multi\nline"\n2,done\n').dataRows, 2);
});
test("CRLF and UTF-8 BOM remain supported", () => {
  const r = inspectCsv("\uFEFFid,name\r\n1,Ada\r\n");
  assert.equal(r.ok, true);
  assert.equal(r.dataRows, 1);
  assert.equal(r.columns, 2);
});
test("uneven-length records and missing cells are counted, not dropped", () => {
  const r = inspectCsv("id,name,amount\n1,A\n2,B,5,extra\n");
  assert.equal(r.dataRows, 2);
  assert.equal(r.raggedRows, 2);
  assert.equal(r.missingCells, 1);
});
test("duplicate records produce warnings without deletion", () => {
  const r = inspectCsv("id,name\n1,A\n1,A\n");
  assert.equal(r.dataRows, 2);
  assert.equal(r.duplicateRows, 1);
});
test("duplicate headers compare trim and case, plus blank headers", () => {
  const r = inspectCsv("ID, id ,  \n1,2,3\n");
  assert.equal(r.columns, 3);
  assert.equal(r.duplicateHeaders, 1);
  assert.equal(r.blankHeaders, 1);
});
test("spreadsheet formula warnings are heuristic, not sanitizer output", () => {
  const r = inspectCsv("id,amount\n1,=1+1\n2,+SUM(A1:A2)\n3,-7\n");
  assert.equal(r.formulaWarnings, 2);
  assert.match(r.caveat, /Heuristic/);
});
test("non-numeric leading minus is flagged, ordinary negative amounts are not", () => {
  const r = inspectCsv("id,val\n1,-cmd\n2,-12.50\n");
  assert.equal(r.formulaWarnings, 1);
});
test("malformed unclosed quotes fail closed", () => {
  const r = inspectCsv('id,note\n1,"unclosed\n');
  assert.equal(r.ok, false);
  assert.match(r.error, /Unclosed quoted/);
});
test("unescaped quotes fail closed", () => {
  assert.equal(inspectCsv('id,note\n1,bad"quote\n').ok, false);
});
test("CSV length limit is exactly 32768 UTF-8 bytes, not character count", () => {
  assert.equal(MAX_BYTES, 32 * 1024);
  const huge = "id,val\n1," + "🙂".repeat(8200) + "\n";
  assert.ok(Buffer.byteLength(huge, "utf8") > MAX_BYTES);
  assert.equal(inspectCsv(huge).ok, false);
});
test("free install command chooses frontmatter NAME, not ASE slug", () => {
  assert.match(skill, /^name: "PaperPilot CSV Preflight"$/m);
  assert.match(skill, /^slug: "paperpilot-csv-preflight"$/m);
  assert.ok(skill.includes('npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill "PaperPilot CSV Preflight"'));
  assert.ok(skill.includes('npm exec --package=skills@1.5.7 -- skills add livastic-vm1-primary/paperpilot-tools --skill paperpilot-csv-preflight'));
  assert.doesNotMatch(skill, /npx skills add agentskillexchange\/skills --skill paperpilot-csv-preflight/);
});
test("optional remote paid API is never represented as this local skill's checkout", () => {
  assert.match(skill, /Never make a paid request automatically/);
  assert.match(skill, /only if the \*\*buyer explicitly asks\*\*/i);
  assert.match(skill, /0\.005 native Circle USDC on Base/);
});
