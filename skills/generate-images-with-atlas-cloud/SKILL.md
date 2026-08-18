---
name: "Generate Images with Atlas Cloud"
slug: "generate-images-with-atlas-cloud"
description: "Discovers current Atlas Cloud image models, validates model-specific schemas, submits a single asynchronous image-generation request, polls predictions with a finite budget, and verifies downloaded image artifacts. Use when an agent needs text-to-image or image-editing access through the Atlas Cloud API."
category: "Image & Creative Automation"
framework: "Multi-Framework"
verification: listed
source: "https://www.atlascloud.ai/models"
---

# Generate Images with Atlas Cloud

Use this skill when an agent needs to generate or edit images through Atlas Cloud's hosted media API. It provides a provider-neutral operating sequence for shell-capable agents: discover current image models, read the selected model's live schema, preview the exact payload, make one explicitly authorized generation request, poll the returned prediction ID, and validate the downloaded artifact. The workflow is suitable for Codex, Claude Code, Cursor, Gemini, OpenClaw, and custom agents that can run `curl` and `jq`.

Do not use this skill for video, audio, 3D, or OpenAI-compatible chat requests. Do not invent model IDs or request fields from memory; the model catalog and schemas change independently of this skill.

## Installation

### OpenClaw

```bash
clawhub install generate-images-with-atlas-cloud
```

### Direct repo/manual install

Clone the Agent Skill Exchange repository and copy this skill directory into the skill folder used by your agent runtime:

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/generate-images-with-atlas-cloud ~/.agent-skills/generate-images-with-atlas-cloud
```

### Optional Third-Party Installer

The `skills` npm package is maintained by Vercel Labs / third parties, not AgentSkillExchange. If you choose to use it, pin the package version:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill generate-images-with-atlas-cloud
```

## Requirements and authorization

- Bash, `curl`, `jq`, and `file`
- An Atlas Cloud API key exported as `ATLASCLOUD_API_KEY`
- User approval for the selected model, payload, and potentially billable generation request
- A finite prediction-polling budget and an explicit output path

Never print the key, place it in a command-line argument, commit it, or include it in logs. Treat every generation `POST` as potentially billable. A client timeout is ambiguous: the server may have accepted the job even if the client received no prediction ID. Never automatically retry a generation `POST`.

## 1. Discover the current model and schema

Read the live catalog immediately before building a request:

```bash
curl -fsS --max-time 30 \
  https://api.atlascloud.ai/api/v1/models \
  -o /tmp/atlas-models.json

jq -r '
  .data[]
  | select(.type == "Image")
  | [.model, (.tags // [] | join(",")), (.price.actual.base_price // "n/a"), .schema]
  | @tsv
' /tmp/atlas-models.json
```

Choose an exact model whose operation matches the task, such as text-to-image, edit, or reference-to-image. Confirm the catalog entry has `type: "Image"`. Then fetch only the schema URL supplied by that entry:

```bash
MODEL='replace-with-an-exact-live-model-id'
SCHEMA_URL=$(jq -er --arg model "$MODEL" '
  .data
  | map(select(.model == $model and .type == "Image"))
  | if length == 1 then .[0].schema else error("model must match one live Image entry") end
' /tmp/atlas-models.json)

case "$SCHEMA_URL" in
  https://static.atlascloud.ai/*) ;;
  *) echo "Refusing unexpected schema host" >&2; exit 1 ;;
esac

curl -fsS --max-time 30 "$SCHEMA_URL" -o /tmp/atlas-model-schema.json
jq '.components.schemas.Input | {required, properties}' /tmp/atlas-model-schema.json
```

Validate every payload field against `components.schemas.Input`. Required fields must be present, enum values must be exact, and source images must be supplied only when the selected operation requires them. Catalog pricing is volatile; quote the current unit and verification time when cost matters.

## 2. Build and review the payload

Construct JSON with `jq` rather than string interpolation. The following is an example for a model whose current schema accepts `prompt` and `aspect_ratio`; omit or replace fields that are not present in the selected live schema:

```bash
PROMPT='4:5 editorial product photograph of one matte-black travel mug on pale limestone, soft window light from camera left, clean upper-left negative space, no text, no logo, no watermark'

jq -n \
  --arg model "$MODEL" \
  --arg prompt "$PROMPT" \
  --arg aspect_ratio '4:5' \
  '{model: $model, prompt: $prompt, aspect_ratio: $aspect_ratio}' \
  > /tmp/atlas-image-request.json

jq . /tmp/atlas-image-request.json
```

Show the model ID, current price unit, and complete payload to the user before submission when they have not already approved those details. Keep one creative variable per diagnostic iteration so changes remain attributable.

## 3. Submit exactly once

After approval, issue one `POST`. Do not add `curl --retry` and do not wrap this command in a retry loop:

```bash
curl -fsS --max-time 60 \
  -X POST https://api.atlascloud.ai/api/v1/model/generateImage \
  -H "Authorization: Bearer $ATLASCLOUD_API_KEY" \
  -H 'Content-Type: application/json' \
  --data-binary @/tmp/atlas-image-request.json \
  -o /tmp/atlas-image-submission.json

PREDICTION_ID=$(jq -er '
  select((.code | tostring) == "200")
  | .data.id
  | select(type == "string" and length > 0)
' /tmp/atlas-image-submission.json)

printf 'prediction_id=%s\n' "$PREDICTION_ID"
```

If the command times out or returns no prediction ID, stop. Report the ambiguity and reconcile through Atlas Cloud account history or support instead of creating another job.

## 4. Poll with a finite budget

Prediction `GET` requests may be retried because they do not create replacement jobs. Use a bounded loop and stop on every terminal state:

```bash
PREDICTION_URL="https://api.atlascloud.ai/api/v1/model/prediction/$PREDICTION_ID"

for attempt in $(seq 1 20); do
  curl -fsS --max-time 30 \
    -H "Authorization: Bearer $ATLASCLOUD_API_KEY" \
    "$PREDICTION_URL" \
    -o /tmp/atlas-image-prediction.json || true

  STATUS=$(jq -r '.data.status // empty' /tmp/atlas-image-prediction.json 2>/dev/null || true)
  case "$STATUS" in
    completed) break ;;
    failed|timeout|canceled|cancelled)
      jq -r '.data.error // ("prediction ended with status " + (.data.status // "unknown"))' /tmp/atlas-image-prediction.json >&2
      exit 1
      ;;
  esac

  if [[ "$attempt" -eq 20 ]]; then
    echo "Polling budget exhausted; preserve prediction ID $PREDICTION_ID" >&2
    exit 1
  fi
  sleep 3
done

jq -e '.data.status == "completed" and (.data.outputs | type == "array" and length > 0)' \
  /tmp/atlas-image-prediction.json >/dev/null
```

An exhausted poll budget does not mean the job failed or that no charge occurred. Preserve the prediction ID and let the user decide whether to check it later.

## 5. Download and inspect the artifact

Read the first output URL only from a completed response. Require direct HTTPS, do not follow redirects without revalidating each target, cap the file size, and verify that the result is an image:

```bash
OUTPUT_URL=$(jq -er '.data.outputs[0]' /tmp/atlas-image-prediction.json)
case "$OUTPUT_URL" in
  https://*) ;;
  *) echo "Refusing non-HTTPS output URL" >&2; exit 1 ;;
esac

OUTPUT_PATH='./atlas-output.bin'
curl -fsS --max-time 60 \
  --proto '=https' \
  --max-filesize 26214400 \
  "$OUTPUT_URL" \
  -o "$OUTPUT_PATH"

file --mime-type "$OUTPUT_PATH"
```

Open the image before reporting success. Check dimensions, corruption, prompt-critical subject count and geometry, crop safety, hands and faces, reflections, repeated structures, exact text or logos, unintended watermarks, and any consent, likeness, privacy, trademark, or usage-right constraints. API status `completed` proves only that an output was returned; it is not creative approval.

## Prompt and iteration guidance

These are production heuristics, not model guarantees:

- Lead with the deliverable, aspect ratio, subject, and intended placement.
- Specify composition, camera distance, light direction, materials, and required negative space using observable terms.
- Quote required on-image copy exactly, but plan a deterministic typography repair pass and inspect every character.
- Express exclusions concretely: `no logo`, `no watermark`, `no extra objects`.
- For identity consistency, editing, or reference-driven work, select a live model whose schema explicitly accepts the required image inputs.
- Log the exact model ID, redacted payload, prediction ID, artifact path, and visual review result. Never log credentials.

## Official references

- [Atlas Cloud model catalog](https://www.atlascloud.ai/models)
- [Atlas Cloud live model API](https://api.atlascloud.ai/api/v1/models)
- [Atlas Cloud API key console](https://www.atlascloud.ai/console/api-keys)
- The model-specific schema URL returned by each live catalog entry
