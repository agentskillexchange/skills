---
name: "Generate Images and Video with UberLLM"
slug: "generate-images-and-video-with-uberllm"
description: "Discovers current UberLLM image and video models, reads each model's live request schema, checks the price with a free validate call, submits one image request or one idempotent video job, polls the job with a finite budget, and verifies the downloaded file. Use when an agent needs text-to-image, image editing or text/image-to-video through the UberLLM API with the same key it uses for chat models."
verification: "listed"
source: "https://uberllm.dev/docs/media"
category: "Image & Creative Automation"
framework: "Multi-Framework"
---

# Generate Images and Video with UberLLM

Use this skill when an agent needs to make or edit an image, or make a short video, through UberLLM's media API. UberLLM is an OpenAI-compatible API where one key covers chat, image, video, music and speech models from one prepaid balance, so an agent that already calls chat models there does not need a second media account. The skill gives a shell-capable agent one operating sequence: discover a live model, read that model's request schema, preview the payload, check the price with a free `validate` call, make one authorized request, poll video jobs with a finite budget, and inspect the downloaded file. It works for Codex, Claude Code, Cursor, Gemini, OpenClaw and custom agents that can run `curl` and `jq`.

Do not use this skill for chat completions, music or speech; those use other routes on the same API (see the official references). Do not invent model IDs or request fields from memory; the model list and each model's schema change independently of this skill.

## Installation

### OpenClaw

```bash
clawhub install generate-images-and-video-with-uberllm
```

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/generate-images-and-video-with-uberllm ~/.agent-skills/generate-images-and-video-with-uberllm
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill generate-images-and-video-with-uberllm
```

## Requirements and authorization

- Bash, `curl`, `jq`, `file` and `uuidgen`
- An UberLLM API key (`ull_...`) exported as `UBERLLM_API_KEY`, from https://uberllm.dev/signup, and prepaid credit on the account
- User approval for the selected model, payload and price before any billable request
- A finite polling budget for video jobs and an explicit output path

Never print the key, commit it, or include it in logs. Treat every image `POST` and every video job as billable. An image request that times out may still have been made and billed, so never retry an image `POST` automatically. A video job is different: it is started with an `Idempotency-Key`, and sending the same request with the same key again within 24 hours returns the same job instead of a second one.

## 1. Discover the current model and schema

Read the live list immediately before building a request. The list is public; `type` is `image` or `video`:

```bash
WORK=$(mktemp -d)
KIND='image'   # or 'video'

curl -fsS --max-time 30 \
  "https://api.uberllm.dev/v1/models?type=$KIND" \
  -o "$WORK/models.json"

jq -r '
  .data[]
  | select(.available == true and .nsfw == false)
  | [.id, (.endpoints | join(",")), (.input_modalities | join(",")), (.pricing.usd // .pricing.list_usd // "n/a"), .pricing.unit]
  | @tsv
' "$WORK/models.json"
```

Pick an exact model whose route matches the task: `/v1/images/generations` for a new image, `/v1/images/edits` for an edit (ids usually end in `-edit`), `/v1/video/generations` for a video. `input_modalities` containing `image` means the model takes a source picture. Then read that model's request schema; `parameters` is a JSON Schema of the request body:

```bash
MODEL='replace-with-an-exact-live-model-id'
jq -e --arg model "$MODEL" '[.data[] | select(.id == $model and .available == true)] | length == 1' \
  "$WORK/models.json" >/dev/null || { echo "model must match one available entry" >&2; exit 1; }

curl -fsS --max-time 30 "https://api.uberllm.dev/v1/models/$MODEL" -o "$WORK/model.json"
jq '{endpoints, pricing, required: .parameters.required, properties: .parameters.properties}' "$WORK/model.json"
```

Validate every payload field against `parameters`. Required fields must be present and enum values exact (image `size`, video `duration_seconds`, `resolution`, `aspect_ratio`). A source picture is an `https://` link, a `data:` URI or plain base64 of a PNG, JPEG or WebP; edits take it in `image`, image-to-video models in `image_url`.

## 2. Build the payload and check the price without spending

Construct JSON with `jq` rather than string interpolation. This example is for an image model whose schema accepts `prompt` and `size`; omit or replace fields that are not in the selected schema:

```bash
PROMPT='Square editorial product photograph of one matte-black travel mug on pale limestone, soft window light from camera left, no text, no logo, no watermark'

jq -n --arg model "$MODEL" --arg prompt "$PROMPT" \
  '{model: $model, prompt: $prompt, n: 1, size: "1024x1024"}' \
  > "$WORK/request.json"

jq . "$WORK/request.json"
```

For a video, the same shape uses the schema's fields, for example `{model, prompt, duration_seconds: 5}` plus `image_url` for an image-to-video model.

Send the same body with `"validate": true`. Nothing is made and nothing is charged; the answer says whether the request is valid, its listed price (`cost_usd`) and the most it can be billed (`max_cost_usd`). Use the route from the model's `endpoints`:

```bash
ROUTE=$(jq -er '.endpoints[0]' "$WORK/model.json")

jq '. + {validate: true}' "$WORK/request.json" \
  | curl -fsS --max-time 30 \
      -X POST "https://api.uberllm.dev$ROUTE" \
      -H "Authorization: Bearer $UBERLLM_API_KEY" \
      -H 'Content-Type: application/json' \
      --data-binary @- \
      -o "$WORK/quote.json"

jq '{valid, model, cost_usd, max_cost_usd, unit, units, defaults_applied}' "$WORK/quote.json"
```

Show the model ID, the quoted price and the complete payload to the user before submission when they have not already approved those details. To make the approved price a hard limit, add `"max_cost": <US dollars>` to the request; anything that could cost more is refused before it starts. Keep one creative variable per iteration so changes stay attributable.

## 3a. Make an image (one request)

After approval, issue exactly one `POST`. Do not add `curl --retry` and do not wrap this command in a retry loop. The picture comes back in the answer:

```bash
jq '. + {response_format: "url"}' "$WORK/request.json" \
  | curl -fsS --max-time 120 \
      -X POST "https://api.uberllm.dev$ROUTE" \
      -H "Authorization: Bearer $UBERLLM_API_KEY" \
      -H 'Content-Type: application/json' \
      --data-binary @- \
      -o "$WORK/image.json"

OUTPUT_URL=$(jq -er '.data[0].url' "$WORK/image.json")
jq '.usage' "$WORK/image.json"
```

`usage.cost_usd` is what the picture cost. If the command times out or returns no `data`, stop and check Dashboard > Activity at https://uberllm.dev/dashboard/activity before trying again. Image links under `/v1/media/artifacts/` are kept for about 15 minutes, so download right away (step 4), or send `"response_format": "b64_json"` to receive the picture inside the answer.

## 3b. Make a video (one job, then poll with a finite budget)

Start the job once with a new `Idempotency-Key` and keep that key with the job record:

```bash
IDEMPOTENCY_KEY=$(uuidgen)

curl -fsS --max-time 60 \
  -X POST https://api.uberllm.dev/v1/video/generations \
  -H "Authorization: Bearer $UBERLLM_API_KEY" \
  -H 'Content-Type: application/json' \
  -H "Idempotency-Key: $IDEMPOTENCY_KEY" \
  --data-binary @"$WORK/request.json" \
  -o "$WORK/job.json"

JOB_ID=$(jq -er '.id | select(type == "string" and length > 0)' "$WORK/job.json")
jq '{id, status, model, estimated_cost_usd, max_cost_usd}' "$WORK/job.json"
```

If this call times out, send the identical request with the same `IDEMPOTENCY_KEY`: it returns the job that was already started, never a second one. Never resend with a new key unless the user approves a new job.

Status `GET` requests may be repeated. Stop on every terminal state; `succeeded`, `failed`, `canceled` and `expired` are the only ones besides `queued` and `running`:

```bash
for attempt in $(seq 1 60); do
  curl -fsS --max-time 30 \
    -H "Authorization: Bearer $UBERLLM_API_KEY" \
    "https://api.uberllm.dev/v1/video/generations/$JOB_ID" \
    -o "$WORK/status.json" || true

  STATUS=$(jq -r '.status // empty' "$WORK/status.json" 2>/dev/null || true)
  case "$STATUS" in
    succeeded) break ;;
    failed|canceled|expired)
      jq -r '.error.message // ("job ended with status " + .status)' "$WORK/status.json" >&2
      exit 1
      ;;
  esac

  if [[ "$attempt" -eq 60 ]]; then
    echo "Polling budget exhausted; preserve job id $JOB_ID" >&2
    exit 1
  fi
  sleep 10
done

OUTPUT_URL=$(jq -er '.results[0].url' "$WORK/status.json")
```

`failed`, `canceled` and `expired` jobs cost nothing; on `failed`, `error.retryable` says whether a new job can work. Most videos take 1 to 5 minutes. An exhausted budget does not mean the job failed: preserve the job ID and let the user decide whether to check it later. Right after `succeeded`, `usage` may show `cost_pending: true` for a few seconds until the final charge arrives. To stop a job that is no longer needed, send `DELETE` to the same job URL; a job the provider already finished is still billed.

## 4. Download and inspect the file

Result links live on `api.uberllm.dev` and need the same key. Require that host, cap the size, and verify the file type:

```bash
case "$OUTPUT_URL" in
  https://api.uberllm.dev/*) ;;
  *) echo "Refusing unexpected output host" >&2; exit 1 ;;
esac

OUTPUT_PATH='./uberllm-output.bin'
curl -fsS --max-time 120 \
  --proto '=https' \
  --max-filesize 209715200 \
  -H "Authorization: Bearer $UBERLLM_API_KEY" \
  "$OUTPUT_URL" \
  -o "$OUTPUT_PATH"

file --mime-type "$OUTPUT_PATH"
```

Video files are kept for about 3 hours after the job ends; after that the link answers `404 artifact_expired`. Open the image or watch the clip before reporting success. Check dimensions or duration, corruption, prompt-critical subject count and geometry, crop safety, hands and faces, motion artifacts, exact text or logos, unintended watermarks, and any consent, likeness, privacy, trademark or usage-right constraints. A `200` with a file proves only that an output was returned; it is not creative approval.

## Prompt and iteration guidance

These are production heuristics, not model guarantees:

- Lead with the deliverable, aspect ratio, subject and intended placement.
- Specify composition, camera distance, light direction, materials and motion using observable terms.
- Quote required on-image copy exactly, but plan a typography repair pass and inspect every character.
- Express exclusions concretely: `no logo`, `no watermark`, `no extra objects`.
- For edits or image-to-video, pick a live model whose schema accepts the required source picture.
- Log the exact model ID, redacted payload, quoted price, job ID or request cost, file path and review result. Never log credentials.

## Official references

- [UberLLM media guide: images, edits, video, music and speech](https://uberllm.dev/docs/media)
- [UberLLM live model list](https://api.uberllm.dev/v1/models?type=all)
- [Model pages with live prices](https://uberllm.dev/models)
- [UberLLM API keys](https://uberllm.dev/dashboard/keys)
- [OpenAPI spec for every /v1 route](https://uberllm.dev/openapi.json)
