# Heimdall container runner.
#
# Based on the official Playwright image, which already bundles Chromium plus the
# OS libraries and Xvfb needed for headed/headless runs — so each container has
# its own virtual display (its own OS input focus), which is what lets the
# `container` driver run isolated headed sessions in parallel.
#
# IMPORTANT: keep this Playwright version in lockstep with the EXACT-pinned
# `playwright` dependency in package.json, or the bundled browser revision won't
# match (the in-container Playwright errors out demanding the matching image).
FROM mcr.microsoft.com/playwright:v1.61.0-jammy

ENV PLAYWRIGHT_BROWSERS_PATH=/ms-playwright
ENV PLAYWRIGHT_SKIP_BROWSER_DOWNLOAD=1
ENV NODE_ENV=production

WORKDIR /opt/heimdall

# Install runtime deps against the prebuilt dist (no dev deps, reuse base browsers).
COPY package.json ./
RUN npm install --omit=dev --no-audit --no-fund

# Ship the compiled CLI.
COPY dist ./dist

# `docker run heimdall:local run /work/in/plan.json --out /work/out ...`
ENTRYPOINT ["node", "/opt/heimdall/dist/cli.js"]
