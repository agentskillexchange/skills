/**
 * A tiny, dependency-free fixture server for the cdp integration test.
 *
 * Built on node:http only. It serves exactly what the integration test needs:
 *   GET /            -> an HTML page with #app containing "Heimdall OK"
 *   GET /api/health  -> 200 application/json {"ok":true}
 *   POST /start      -> 303 redirect, headers {location:/done, x-run-id:r123}
 *   GET /poll        -> 200 application/json {"ready":true,"id":"r123"}
 *   GET /slow        -> sleeps ~15ms; every 5th request 500s (deterministic 20%
 *                       error rate) — the load-step fixture
 *   GET /events      -> text/event-stream emitting 3 `data:` events then closing
 *                       — the sse-step fixture
 *   GET /events-one  -> text/event-stream emitting 1 `data:` event then holding the
 *                       connection open forever — drives the "fewer than requested,
 *                       then time out" sse path (collects 1, status 200)
 *   GET /events-hang -> text/event-stream that sends NO events and never closes —
 *                       drives the "zero events, time out" sse path (status 0)
 *   POST   /resource     -> 201 {"id":"res-N"}; creates an in-memory resource
 *   GET    /resource?id= -> 200 {"exists":true} if it exists, else 404
 *   DELETE /resource?id= -> 200 {"deleted":true}; removes it
 *   GET    /resources    -> 200 {"count":N,"ids":[...]} — the setup/teardown fixture
 *   DELETE /resources    -> 200 {"cleared":N}; empties the store (teardown cleanup)
 *   GET    /echo-auth    -> 200 {"authorization":"<the request's Authorization header>"}
 *                          — reflects an injected ${env.X} secret back (config fixture)
 *   GET    /a11y-bad     -> 200 HTML with an alt-less <img>, an unlabeled control and a
 *                          duplicated id — the accessibility-violation fixture (#11)
 *   GET    /a11y-good    -> 200 HTML, the same shape made clean (zero a11y violations)
 *   GET    /pixel        -> 200 HTML, a fixed-size, animation-free, deterministic page
 *                          for a stable pixel-diff baseline (#13)
 *   GET    /api/flaky    -> 200 {"ok":true} — a JSON endpoint a test can route-fault (#12)
 *   GET    /flaky-page   -> 200 HTML that fetches /api/flaky and renders success/error
 *                          into #status (drives the faulted-route UI path)
 *   POST   /api/counter  -> 200 {"value":N}; atomically increments a shared counter so
 *                          racing writers each get a unique value (#15)
 *   GET    /api/counter  -> 200 {"value":N}; reads the current counter
 *   GET    /echo-secret  -> 200 {"authorization":"<header>","token":...,"email":...,"ssn":...}
 *                          — reflects the secret header and returns a PII-shaped body (#16)
 *   (anything else)  -> 404
 *
 * It binds to an ephemeral port (listen on 0) on 127.0.0.1 and exposes the
 * concrete port so the test can build a baseUrl. No globals, no side effects on
 * import — call `startFixtureServer()` and `await stop()` when done.
 */
import { createServer, type Server } from "node:http";
import { AddressInfo } from "node:net";

const PAGE = `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Heimdall Fixture</title>
  </head>
  <body>
    <main id="app">Heimdall OK</main>
  </body>
</html>`;

// Accessibility fixtures (#11). A11Y_BAD intentionally carries three defects: an
// <img> with no alt, an unlabeled form control, and a duplicated element id (axe
// flags image-alt + label by default). A11Y_GOOD is the same shape, made clean —
// so a test can assert violations on one page and zero on the other.
const A11Y_BAD = `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>A11y Bad</title>
  </head>
  <body>
    <main id="dup">
      <h1>Broken page</h1>
      <img src="logo.png" />
      <input type="text" />
      <div id="dup">duplicate id</div>
    </main>
  </body>
</html>`;

const A11Y_GOOD = `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>A11y Good</title>
  </head>
  <body>
    <main id="content">
      <h1>Accessible page</h1>
      <img src="logo.png" alt="Heimdall logo" />
      <label for="name">Name</label>
      <input id="name" type="text" />
      <div id="note">unique id</div>
    </main>
  </body>
</html>`;

// Pixel-stability fixture (#13). Fixed dimensions, system colours, no web fonts,
// no animation/transition, no dynamic content — so two screenshots are identical
// and a pixel-diff oracle has a stable baseline.
const PIXEL_PAGE = `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Pixel Stable</title>
    <style>
      * { margin: 0; padding: 0; box-sizing: border-box; }
      html, body { width: 320px; height: 240px; background: #102030; }
      #swatch {
        width: 320px; height: 240px;
        background: #3366cc;
        color: #ffffff;
        font: 16px/240px monospace;
        text-align: center;
      }
    </style>
  </head>
  <body>
    <div id="swatch">STABLE</div>
  </body>
</html>`;

// Route-fault fixture (#12). A page that fetches /api/flaky and renders a clearly
// success-or-error UI into #status, so a test can fault the route (network
// intercept) and watch the error branch render.
const FLAKY_PAGE = `<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <title>Flaky</title>
  </head>
  <body>
    <main id="app">
      <div id="status">loading</div>
    </main>
    <script>
      fetch("/api/flaky")
        .then((r) => {
          if (!r.ok) throw new Error("bad status " + r.status);
          return r.json();
        })
        .then((j) => {
          document.getElementById("status").textContent = j.ok ? "success" : "error";
        })
        .catch(() => {
          document.getElementById("status").textContent = "error";
        });
    </script>
  </body>
</html>`;

export interface FixtureServer {
  /** The chosen ephemeral port. */
  port: number;
  /** Convenience base URL, e.g. http://127.0.0.1:54321 */
  baseUrl: string;
  /** The underlying node:http server. */
  server: Server;
  /** Close the server and resolve once it has fully stopped. */
  stop(): Promise<void>;
}

/**
 * Start the fixture server on an ephemeral port and resolve once listening.
 * `host` defaults to 127.0.0.1; pass "0.0.0.0" so a container can reach it via
 * host.docker.internal (the container integration test needs this).
 */
export function startFixtureServer(host = "127.0.0.1"): Promise<FixtureServer> {
  // Per-server request counter so /slow's flakiness is deterministic regardless
  // of concurrency: every 5th request 500s ⇒ a fixed 20% error rate.
  let slowHits = 0;

  // In-memory resource store for the setup/teardown lifecycle fixture. Per-server
  // (each test gets its own), so the sequence + counts are deterministic.
  const resources = new Set<string>();
  let resourceSeq = 0;

  // Contended-write fixture (#15): a single shared counter. Node's event loop
  // makes the read-modify-write atomic, so racing writers each get a unique value
  // (1..N) with no lost updates — a test can fire N concurrent POSTs and assert
  // the set of returned values is exactly 1..N.
  let counter = 0;

  // Connections deliberately held open by the /events-one and /events-hang SSE
  // fixtures. We destroy them in stop() so a hung stream can never block close().
  const openStreams = new Set<import("node:http").ServerResponse>();

  const server = createServer((req, res) => {
    const url = req.url ?? "/";
    // Normalise away any query string for routing.
    const path = url.split("?")[0];
    const query = url.includes("?") ? new URLSearchParams(url.slice(url.indexOf("?") + 1)) : new URLSearchParams();

    if (req.method === "GET" && path === "/") {
      res.writeHead(200, { "content-type": "text/html; charset=utf-8" });
      res.end(PAGE);
      return;
    }

    if (req.method === "GET" && path === "/api/health") {
      res.writeHead(200, { "content-type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ ok: true }));
      return;
    }

    // Stateful-flow fixtures: POST /start issues a 303 redirect carrying an id in
    // headers (location + x-run-id); GET /poll reports readiness deterministically.
    if (req.method === "POST" && path === "/start") {
      res.writeHead(303, { location: "/done", "x-run-id": "r123" });
      res.end();
      return;
    }

    if (req.method === "GET" && path === "/poll") {
      res.writeHead(200, { "content-type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ ready: true, id: "r123" }));
      return;
    }

    // Load-step fixture: a little latency + a deterministic 1-in-5 failure rate.
    if (req.method === "GET" && path === "/slow") {
      const n = ++slowHits;
      const failing = n % 5 === 0;
      setTimeout(() => {
        if (failing) {
          res.writeHead(500, { "content-type": "application/json; charset=utf-8" });
          res.end(JSON.stringify({ ok: false }));
        } else {
          res.writeHead(200, { "content-type": "application/json; charset=utf-8" });
          res.end(JSON.stringify({ ok: true }));
        }
      }, 15);
      return;
    }

    // SSE-step fixture: emit a few events then end the stream (the client's
    // EventSource sees the close and resolves with what it collected).
    if (req.method === "GET" && path === "/events") {
      res.writeHead(200, {
        "content-type": "text/event-stream; charset=utf-8",
        "cache-control": "no-cache",
        connection: "keep-alive",
      });
      let i = 0;
      const total = 3;
      const tick = () => {
        i += 1;
        res.write(`id: ${i}\n`);
        res.write(`data: ${JSON.stringify({ n: i })}\n\n`);
        if (i >= total) {
          res.end();
        } else {
          setTimeout(tick, 10);
        }
      };
      setTimeout(tick, 10);
      return;
    }

    // SSE partial fixture: emit exactly one event, then hold the stream open so the
    // client never reaches a requested-but-larger event count and must time out. The
    // EventSource resolves with the one event it did collect (status 200, ok true).
    if (req.method === "GET" && path === "/events-one") {
      res.writeHead(200, {
        "content-type": "text/event-stream; charset=utf-8",
        "cache-control": "no-cache",
        connection: "keep-alive",
      });
      openStreams.add(res);
      res.on("close", () => openStreams.delete(res));
      setTimeout(() => {
        if (!res.writableEnded) {
          res.write("id: 1\n");
          res.write(`data: ${JSON.stringify({ n: 1 })}\n\n`);
        }
      }, 10);
      // Intentionally never res.end(): the client must hit its own timeout.
      return;
    }

    // SSE empty fixture: open the stream, send NOTHING, never close. The client
    // collects zero events and times out — the sse step records status 0 (no data).
    if (req.method === "GET" && path === "/events-hang") {
      res.writeHead(200, {
        "content-type": "text/event-stream; charset=utf-8",
        "cache-control": "no-cache",
        connection: "keep-alive",
      });
      openStreams.add(res);
      res.on("close", () => openStreams.delete(res));
      // Intentionally never write nor end: zero events, client-side timeout only.
      return;
    }

    // Setup/teardown lifecycle fixture: a tiny CRUD over an in-memory resource set.
    if (req.method === "POST" && path === "/resource") {
      const id = `res-${++resourceSeq}`;
      resources.add(id);
      res.writeHead(201, { "content-type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ id }));
      return;
    }

    if (req.method === "GET" && path === "/resource") {
      const id = query.get("id") ?? "";
      const exists = resources.has(id);
      res.writeHead(exists ? 200 : 404, { "content-type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ exists }));
      return;
    }

    if (req.method === "DELETE" && path === "/resource") {
      const id = query.get("id") ?? "";
      const deleted = resources.delete(id);
      res.writeHead(200, { "content-type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ deleted }));
      return;
    }

    if (req.method === "GET" && path === "/resources") {
      res.writeHead(200, { "content-type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ count: resources.size, ids: [...resources] }));
      return;
    }

    // Clear the whole store — a teardown-friendly bulk delete that leaves an
    // observable side effect (count → 0), so a test can prove teardown actually ran.
    if (req.method === "DELETE" && path === "/resources") {
      const cleared = resources.size;
      resources.clear();
      res.writeHead(200, { "content-type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ cleared }));
      return;
    }

    // Config/env fixture: reflect the Authorization header so a test can confirm an
    // ${env.X}-interpolated secret actually reached the SUT in the request.
    if (req.method === "GET" && path === "/echo-auth") {
      res.writeHead(200, { "content-type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ authorization: req.headers["authorization"] ?? "" }));
      return;
    }

    // Accessibility fixtures (#11): a deliberately broken page and its clean twin.
    if (req.method === "GET" && path === "/a11y-bad") {
      res.writeHead(200, { "content-type": "text/html; charset=utf-8" });
      res.end(A11Y_BAD);
      return;
    }

    if (req.method === "GET" && path === "/a11y-good") {
      res.writeHead(200, { "content-type": "text/html; charset=utf-8" });
      res.end(A11Y_GOOD);
      return;
    }

    // Pixel-stability fixture (#13): a static, animation-free, deterministic page.
    if (req.method === "GET" && path === "/pixel") {
      res.writeHead(200, { "content-type": "text/html; charset=utf-8" });
      res.end(PIXEL_PAGE);
      return;
    }

    // Route-fault fixtures (#12): a plain 200 JSON endpoint a test can fault via
    // network interception, plus a page that renders success/error off its result.
    if (req.method === "GET" && path === "/api/flaky") {
      res.writeHead(200, { "content-type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ ok: true }));
      return;
    }

    if (req.method === "GET" && path === "/flaky-page") {
      res.writeHead(200, { "content-type": "text/html; charset=utf-8" });
      res.end(FLAKY_PAGE);
      return;
    }

    // Contended-write fixture (#15): POST increments and returns the new value;
    // GET reads the current value. Concurrent POSTs race but never lose an update.
    if (req.method === "POST" && path === "/api/counter") {
      const value = ++counter;
      res.writeHead(200, { "content-type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ value }));
      return;
    }

    if (req.method === "GET" && path === "/api/counter") {
      res.writeHead(200, { "content-type": "application/json; charset=utf-8" });
      res.end(JSON.stringify({ value: counter }));
      return;
    }

    // Secret/PII echo fixture (#16): reflect the Authorization header AND return a
    // PII-shaped token in the body, so a test can prove redaction scrubs both the
    // injected secret and secret-shaped payload from the report/stderr.
    if (req.method === "GET" && path === "/echo-secret") {
      res.writeHead(200, { "content-type": "application/json; charset=utf-8" });
      res.end(
        JSON.stringify({
          authorization: req.headers["authorization"] ?? "",
          token: "sk-live-deadbeefcafebabe0123456789",
          email: "user@example.com",
          ssn: "123-45-6789",
        }),
      );
      return;
    }

    res.writeHead(404, { "content-type": "text/plain; charset=utf-8" });
    res.end("not found");
  });

  return new Promise<FixtureServer>((resolve, reject) => {
    server.once("error", reject);
    // Bind to host:0 -> the OS assigns a free port.
    server.listen(0, host, () => {
      server.removeListener("error", reject);
      const addr = server.address() as AddressInfo;
      const port = addr.port;
      resolve({
        port,
        baseUrl: `http://127.0.0.1:${port}`,
        server,
        stop: () =>
          new Promise<void>((res, rej) => {
            // Force-destroy any deliberately-hung SSE streams, then drop all
            // keep-alive sockets so close() can resolve promptly even if a test
            // left an /events-hang connection open.
            for (const stream of openStreams) stream.destroy();
            openStreams.clear();
            server.closeAllConnections?.();
            server.close((err) => (err ? rej(err) : res()));
          }),
      });
    });
  });
}
