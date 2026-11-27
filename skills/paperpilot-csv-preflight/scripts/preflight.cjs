#!/usr/bin/env node
"use strict";
/**
 * PaperPilot agent skill: bounded FREE offline CSV heuristic.
 * No HTTP, wallet code, telemetry, env tokens, writes, or uploaded content.
 * Never prints the input data or local file names.
 */
const fs = require("node:fs");
const {inspectCsv, MAX_BYTES} = require("./csv-local-preview.cjs");
const SYNTHETIC = Buffer.from(
  'id,name,amount\n1,Ada,15\n2,,20\n2,,20\n3,"=HYPERLINK(""https://example.invalid"", ""not safe"")",45\n4,Bob\n',
  "utf8"
);
function fail(message) {
  return {ok:false,error:message,localOnly:true,networkRequests:0,chargedUSDC:"0"};
}
async function readStdin() {
  const parts = [];
  let bytes = 0;
  for await (const part of process.stdin) {
    bytes += part.length;
    if (bytes > MAX_BYTES) return null;
    parts.push(part);
  }
  return Buffer.concat(parts);
}
async function main(args) {
  if (args.length === 1 && (args[0] === "--help" || args[0] === "-h")) {
    process.stdout.write("Usage: node preflight.cjs --demo | --file nonsecret.csv | --stdin\nFree offline heuristic, UTF-8 up to 32768 bytes. No payment.\n");
    return 0;
  }
  if (!(args.length === 1 && ["--demo","--stdin"].includes(args[0]))
      && !(args.length === 2 && args[0] === "--file" && args[1] && !args[1].startsWith("-"))) {
    process.stdout.write(JSON.stringify(fail("Use exactly --demo, --stdin, or --file <CSV path>")) + "\n");
    return 2;
  }
  let bytes;
  try {
    if (args[0] === "--demo") bytes = SYNTHETIC;
    else if (args[0] === "--stdin") bytes = await readStdin();
    else {
      const stat = fs.statSync(args[1]);
      if (!stat.isFile()) {
        process.stdout.write(JSON.stringify(fail("Not a regular local file.")) + "\n");
        return 2;
      }
      if (stat.size > MAX_BYTES) bytes = null;
      else bytes = fs.readFileSync(args[1]);
    }
    if (bytes === null || bytes.length > MAX_BYTES) {
      process.stdout.write(JSON.stringify(fail("CSV exceeds the 32 KiB input limit.")) + "\n");
      return 2;
    }
    const csv = new TextDecoder("utf-8", {fatal:true}).decode(bytes);
    const report = inspectCsv(csv);
    process.stdout.write(JSON.stringify({
      ...report,localOnly:true,networkRequests:0,chargedUSDC:"0",
      note:"Heuristic only; not data correctness or spreadsheet safety certification."
    }) + "\n");
    return report.ok ? 0 : 2;
  } catch (error) {
    // Avoid printing private path, environment, supplied input or stack.
    const reason = error instanceof TypeError ? "Input is not valid UTF-8." : "Cannot read the local input.";
    process.stdout.write(JSON.stringify(fail(reason)) + "\n");
    return 2;
  }
}
main(process.argv.slice(2)).then(code => { process.exitCode = code; }).catch(() => {
  process.stdout.write(JSON.stringify(fail("Unexpected local check failure.")) + "\n");
  process.exitCode = 2;
});
