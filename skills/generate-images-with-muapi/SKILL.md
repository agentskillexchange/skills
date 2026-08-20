---
name: "Generate Images with MuAPI"
slug: "generate-images-with-muapi"
description: "Generates and validates Flux Dev images through MuAPI's asynchronous API. Use when an agent needs hosted text-to-image generation with a single MUAPI_API_KEY, bounded prediction polling, and a credential-free HTTPS artifact download."
verification: "listed"
source: "https://muapi.ai/docs/api-reference"
category: "Image & Creative Automation"
framework: "Multi-Framework"
---

# Generate Images with MuAPI

Use this skill when an agent needs hosted image generation through MuAPI's Flux Dev endpoint.
The workflow makes one explicitly authorized generation request, polls the returned prediction,
and downloads the completed image without forwarding the API key to the output host. MuAPI's
image contract can change, so verify the current API reference before relying on model-specific
fields. This skill is for image generation; do not use it for video, audio, 3D, or chat requests.

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

## 1. Build and review the request

Flux Dev accepts a `WIDTH*HEIGHT` size with each side from 512 through 1536 pixels. Build the
payload with `jq` so prompt text is JSON-escaped:

```bash
PROMPT='a small red fox reading a book beneath a lantern, storybook illustration'
jq -n --arg prompt "$PROMPT" \
  '{prompt: $prompt, image: "", size: "1024*1024", num_inference_steps: 28,
    seed: -1, guidance_scale: 3.5, num_images: 1,
    enable_base64_output: false, enable_safety_checker: true}' \
  > /tmp/muapi-image-request.json
jq . /tmp/muapi-image-request.json
```

## 2. Submit exactly once

Use the documented Flux Dev endpoint and do not add `curl --retry` or a POST retry loop:

```bash
curl -fsS --max-time 60 \
  -X POST https://api.muapi.ai/api/v1/flux-dev-image \
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

## 3. Poll with a finite budget

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

## 4. Download and inspect the artifact

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

- [MuAPI API reference](https://muapi.ai/docs/api-reference)
- [MuAPI Flux Dev](https://muapi.ai/docs/flux-dev)
- [MuAPI access keys](https://muapi.ai/access-keys)
