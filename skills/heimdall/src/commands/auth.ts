/**
 * `heimdall auth save` — capture a Playwright storageState for injected auth.
 *
 * Opens a real (headed) browser at a login URL, waits for you to sign in
 * manually (so passwords/MFA never touch Heimdall), then saves cookies +
 * localStorage to a file you pass to `run --storage-state`. The cdp/container
 * lanes reuse that session instead of scripting a brittle login per run.
 */
import { createInterface } from "node:readline";
import { resolve } from "node:path";
import { chromium } from "playwright";
import { log, c } from "../log.js";

function waitForEnter(prompt: string): Promise<void> {
  const rl = createInterface({ input: process.stdin, output: process.stderr });
  return new Promise((res) => rl.question(prompt, () => (rl.close(), res())));
}

export interface AuthSaveOpts {
  url: string;
  out: string;
}

export async function authSaveCommand(opts: AuthSaveOpts): Promise<void> {
  const out = resolve(opts.out);
  log.info(`Opening ${c.cyan(opts.url)} — sign in, then return here.`);
  const browser = await chromium.launch({ headless: false });
  try {
    const context = await browser.newContext();
    const page = await context.newPage();
    await page.goto(opts.url);
    await waitForEnter(c.yellow("→ Press Enter once you are logged in to save the session… "));
    await context.storageState({ path: out });
    log.ok(`saved session to ${c.bold(out)}`);
    log.warn("this file contains live cookies/tokens — it is gitignored; do not share it.");
    log.info(c.dim(`  use it: heimdall run plan.json --storage-state ${opts.out}`));
  } finally {
    await browser.close();
  }
}
