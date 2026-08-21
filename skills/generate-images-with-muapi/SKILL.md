---
name: "Generate Images with MuAPI"
slug: "generate-images-with-muapi"
description: "Discovers current MuAPI image models, builds a model-specific request, and validates asynchronous image artifacts. Use when an agent needs hosted image generation through one MUAPI_API_KEY, bounded prediction polling, and a credential-free HTTPS download."
verification: "listed"
source: "https://muapi.ai/docs/api-reference"
category: "Image & Creative Automation"
framework: "Multi-Framework"
---

# Generate Images with MuAPI

Use this skill when an agent needs hosted image generation through MuAPI's unified API. First
inspect the live catalog and select an exact image model suited to the task; the catalog includes
multiple FLUX, Nano Banana, Seedream, GPT Image, Midjourney, Qwen, and other model families. The
workflow then makes one explicitly authorized generation request, polls the returned prediction,
and downloads the completed image without forwarding the API key to the output host. Do not
assume that a model name or payload is permanent: read the current model schema before adding
model-specific fields. This skill is for image workflows, not video, audio, 3D, or chat requests.

## Installation

### Manual installation

```bash
git clone https://github.com/agentskillexchange/skills.git
cp -R skills/skills/generate-images-with-muapi ~/.agent-skills/generate-images-with-muapi
```

### Optional third-party installer

The `skills` npm package is maintained by Vercel Labs / third parties. If you use it, pin the
package version:

```bash
npm exec --package=skills@1.5.7 -- skills add agentskillexchange/skills --skill generate-images-with-muapi
```

## Requirements and authorization

- Bash, `curl`, `jq`, and `file`
- A MuAPI key exported as `MUAPI_API_KEY`
- An explicit user-approved prompt, output path, and potentially billable request
- A finite polling budget

Never print or commit the key, put it in a command argument, or enable shell tracing. Treat a
generation `POST` as accepted if its outcome is ambiguous; do not retry it automatically.

## 1. Discover the current model and request contract

Read the live catalog immediately before building a request. The catalog response currently uses
top-level `models` and `total` fields. Each model entry includes fields such as `name`, `category`,
and an already-versioned `endpoint` path. Choose an exact text-to-image or image-to-image model;
do not assume the catalog has a `.data[]` array, a `.type` field, or an inline `.schema` URL:

```bash
curl -fsS --max-time 30 \
  https://api.muapi.ai/api/v1/models \
  -o /tmp/muapi-models.json

jq -r '
  .models[]
  | select((.category // "" | ascii_downcase) | test("^(text to image|image to image)$"))
  | [.name, (.category // ""), (.endpoint // "")] | @tsv
' /tmp/muapi-models.json
```

Use the `endpoint` returned by the catalog, not a remembered alias. Payload fields differ by
model; the minimal prompt payload below is only a starting point. Add size, reference-image, or
quality fields only when the selected model's current model documentation or request contract
supports them.

## 2. Build and review the request

Construct JSON with `jq` so prompt text is escaped. Replace `MODEL_ENDPOINT` and add only fields
validated against that model's current request contract:

```bash
API_ORIGIN='https://api.muapi.ai'
MODEL_ENDPOINT='/api/v1/replace-with-the-exact-endpoint-from-the-catalog'
PROMPT='a small red fox reading a book beneath a lantern, storybook illustration'
case "$MODEL_ENDPOINT" in
  /api/v1/*) ;;
  *) echo "Refusing an endpoint that is not an /api/v1 catalog path" >&2; exit 1 ;;
esac
SUBMIT_URL="${API_ORIGIN}${MODEL_ENDPOINT}"
jq -n --arg prompt "$PROMPT" \
  '{prompt: $prompt}' \
  > /tmp/muapi-image-request.json
jq . /tmp/muapi-image-request.json
```

## 3. Submit exactly once

Use the documented model endpoint and do not add `curl --retry` or a POST retry loop:

```bash
curl -fsS --max-time 60 \
  -X POST "$SUBMIT_URL" \
  -H "x-api-key: $MUAPI_API_KEY" \
  -H 'Content-Type: application/json' \
  -H 'Accept: application/json' \
  --data-binary @/tmp/muapi-image-request.json \
  -o /tmp/muapi-image-submission.json

REQUEST_ID=$(jq -er '.request_id // .data.request_id // .id // .data.id' \
  /tmp/muapi-image-submission.json)
printf 'request_id=%s\n' "$REQUEST_ID"
```

Stop if the request times out or returns no request ID. Reconcile an ambiguous request through
the MuAPI account or support rather than creating a second generation job.

## 4. Poll with a finite budget

Prediction GET requests may be retried because they do not create replacement jobs. Poll at most
60 times, stop on terminal failure, and preserve the request ID if the budget is exhausted:

```bash
PREDICTION_URL="https://api.muapi.ai/api/v1/predictions/$REQUEST_ID/result"
for attempt in $(seq 1 60); do
  curl -fsS --max-time 30 \
    -H "x-api-key: $MUAPI_API_KEY" \
    -H 'Accept: application/json' \
    "$PREDICTION_URL" -o /tmp/muapi-image-result.json || true

  STATUS=$(jq -r '.status // .data.status // empty' /tmp/muapi-image-result.json 2>/dev/null || true)
  case "$STATUS" in
    completed) break ;;
    failed|timeout|canceled|cancelled)
      jq -r '.error // .data.error // ("prediction ended with status " + (.status // .data.status // "unknown"))' \
        /tmp/muapi-image-result.json >&2
      exit 1
      ;;
  esac

  if [[ "$attempt" -eq 60 ]]; then
    echo "Polling budget exhausted; preserve request ID $REQUEST_ID" >&2
    exit 1
  fi
  sleep 2
done
```

## 5. Download and inspect the artifact

Read the first output URL only after completion. Require HTTPS and do not send `MUAPI_API_KEY`
to the returned CDN URL:

```bash
OUTPUT_URL=$(jq -er '.outputs[0] // .data.outputs[0]' /tmp/muapi-image-result.json)
case "$OUTPUT_URL" in
  https://*) ;;
  *) echo "Refusing non-HTTPS output URL" >&2; exit 1 ;;
esac

OUTPUT_PATH='./muapi-output.png'
curl -fsS --max-time 60 --proto '=https' --max-filesize 26214400 \
  "$OUTPUT_URL" -o "$OUTPUT_PATH"
file --mime-type "$OUTPUT_PATH"
```

Open or otherwise inspect the file before reporting success. Check that it is a valid image and
meets the prompt, composition, safety, privacy, likeness, trademark, and usage-rights constraints.

## Official references

- [MuAPI model catalog](https://muapi.ai/docs/models)
- [MuAPI API reference](https://muapi.ai/docs/api-reference)
- [MuAPI image models](https://muapi.ai/playground/group/image)
- [MuAPI access keys](https://muapi.ai/access-keys)
