import { writeFile } from "node:fs/promises";
import { resolve } from "node:path";
import { planJsonSchema } from "../schema.js";
import { log, c } from "../log.js";

export async function schemaCommand(out?: string): Promise<void> {
  const text = JSON.stringify(planJsonSchema(), null, 2);
  if (out) {
    const path = resolve(out);
    await writeFile(path, text + "\n", "utf8");
    log.ok(`wrote JSON Schema to ${c.bold(path)}`);
  } else {
    process.stdout.write(text + "\n");
  }
}
