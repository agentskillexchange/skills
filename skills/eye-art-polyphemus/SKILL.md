---
name: Eye.Art Polyphemus Image Creation
slug: eye-art-polyphemus
description: Use Eye.Art Polyphemus as a no-key hosted MCP for conversational image creation, reference-preserving edits, artist-guided art, site-matched visuals, editable SVG, and supported motion.
category: Image & Creative Automation
framework: MCP
verification: listed
source: https://eye.art/polyphemus/api
---

# Eye.Art Polyphemus Image Creation

Use Eye.Art Polyphemus when a user wants to create or refine an image, generate an editable vector, or match visual assets to a webpage. It is a hosted service accessed through a single remote MCP endpoint; the workflow implementation stays server-side.

## Installation

Add the following remote Streamable HTTP MCP server to an MCP-capable agent. No API key or local service is required:

```json
{
  "mcpServers": {
    "eye-art": {
      "url": "https://eye.art/api/eye-mcp"
    }
  }
}
```

For a graphical client, use its remote MCP server settings and enter the same URL. Do not add an authorization header. The agent host must expose the Eye.Art tools to the conversation before invoking them.

## Choose and continue the workflow

- For a new raster image, call `eye_art_make_image` with `mode: "image"` and describe the subject, composition, aspect ratio, and mood.
- For an artist-guided image, select a supported muse such as Dali, Goya, Matisse, Leonardo, Van Gogh, Rothko, or Bob Ross. Treat the name as visual guidance, preserve the requested subject, and never imply endorsement or exact imitation.
- For icons or compact illustrations, request `small_art` and state the size, silhouette, contrast, and background.
- For webpage-matched visuals, use `site_match`; provide the relevant HTML/CSS/JS/TS in `pageReferences` and identify the target section, crop, palette, and copy-safe area.
- For an edit, call `eye_art_edit_image` and attach the original as `imageDataUrl`. State the exact change and what must remain fixed. Keep the source image attached on follow-up edits to reduce subject drift.
- For an editable vector, call `eye_art_make_svg` and save the returned SVG source. Use it for icons, line art, diagrams, and flat scenes; it does not trace a raster image or animate SVG.
- Use `eye_art_prompt_ideas` to explore prompt directions. Use `mode: "motion"` only for a supported motion request.

For related turns, pass the returned `conversationId` so chat context and attached references can persist. Start a new conversation or clear references for unrelated work. If a tool returns a `jobId`, poll `eye_art_image_status` until it reports completion or failure; do not claim a queued generation succeeded. Inspect edits against the source and retry with the source attached and a narrower instruction when the result drifts.

## Limits and privacy

Eye.Art is free to try without an API key, with anonymous generations rate-limited to 20 per hour per caller network identity. Longer staged workflows may take several minutes; report actual job status rather than promising a fixed time. References are sent to the hosted service. Prompts, references, outputs, and conversations may be retained for up to 30 days. Do not send private or sensitive material without the user's direction. See the live API guide for current tool schemas and limitations: https://eye.art/polyphemus/api.
