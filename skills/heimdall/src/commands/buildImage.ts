import { buildImage, dockerAvailable, IMAGE_TAG } from "../drivers/container.js";
import { log } from "../log.js";

export async function buildImageCommand(tag?: string): Promise<void> {
  if (!(await dockerAvailable())) {
    log.err("Docker is not available — start Docker Desktop or install docker first.");
    process.exitCode = 1;
    return;
  }
  await buildImage(tag ?? IMAGE_TAG);
}
