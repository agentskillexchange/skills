---
name: "Call or Text Your Phone from an Agent with /call-me"
slug: "call-me"
description: "Lets an agent call or text the user's own phone (iPhone or Android) through the /call-me remote MCP server, Claude Code plugin or REST API. The phone rings with a native call screen, the agent's text is read aloud, and the user's spoken answer comes back as a transcript. Use it when an unattended run reaches a decision it cannot make alone, when the user asks to be called or texted, or when a spoken status update or summary is wanted."
verification: "listed"
source: "https://github.com/radres/call-me"
publisher_type: "vendor"
category: "Integrations & Connectors"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "radres/call-me"
---

# Call or Text Your Phone from an Agent with /call-me

/call-me is a phone app for iPhone and Android that gives the user a private 10-digit number. With that number an agent can ring the user's actual phone: the phone shows an incoming call, the agent's text is read aloud word for word, the user answers out loud, and the transcript of the answer goes back to the agent. The agent can also send one-way texts and receive the user's text replies. The text of one call can be up to 2000 characters, about two minutes of speech, and it does not have to be a question: a status update or a summary of the day ahead works too.

The hosted remote MCP server speaks Streamable HTTP at `https://callmemcp.com/mcp` and is listed in the official MCP Registry as `com.callmemcp/call-me`. It needs no OAuth and no API key: the user's 10-digit number, shown under My Number in the app, is the only credential. Its tools are `call`, `say`, `hang_up`, `poll_result`, `text`, `wait_for_reply`, `set_thread_title` and `setup`. `call` takes the text to read aloud as `question`, rings the phone and waits about 30 seconds. If the user is still listening or has not picked up, `poll_result` with the returned `call_id` follows the call. By default the line stays open after the first answer, so `say` speaks the next line and `hang_up` ends the call. The Claude Code plugin adds channel delivery of the user's later texts into the session, a `wait_for_answer` tool that gives the user a window to answer at the keyboard before the phone rings, and a Stop hook that wakes the agent to reach out when a turn ends on an unanswered question.

## Installation

### Claude Code (plugin: skill plus MCP channel)

```bash
claude plugin marketplace add radres/call-me
claude plugin install call-me@call-me
claude plugin enable call-me@call-me
```

`install` leaves the plugin disabled, so the `enable` line is required. Then restart Claude Code.

### Any MCP client

Point the client at `https://callmemcp.com/mcp` (Streamable HTTP). For Claude Code without the plugin:

```bash
claude mcp add --transport http call-me https://callmemcp.com/mcp
```

Pass the user's number as `to` in `call` and `text`.

### Direct repo/manual install

```bash
git clone --depth 1 https://github.com/radres/call-me /tmp/call-me
mkdir -p ~/.claude/skills && cp -R /tmp/call-me/skill ~/.claude/skills/call-me
```

- Source: https://github.com/radres/call-me

## Usage

1. Find the user's number before anything else. On a local host read `user_number` from `~/.aiphone/config.json`. If there is none, call `setup`, show its download links ([App Store](https://apps.apple.com/app/call-me/id6789575165) for iPhone, [Google Play](https://play.google.com/store/apps/details?id=com.serdaroztetik.callmeai) for Android) and ask the user to read back the 10 digits under My Number. Never guess or invent a number, never reuse a number from an example or from another user, and save a number the user gives you to `~/.aiphone/config.json` with owner-only permissions (directory 700, file 600).
2. Text first, call second. A call interrupts the user's day and a text does not. Send the question with `text`, keep working on anything that does not depend on the answer, and escalate to `call` only when a few minutes pass without a reply, the answer is blocking and time-sensitive, or the user asked to be called.
3. Never end a turn with an open question in the final message, because the session is asleep after that and cannot reach anyone. Reach out first, or on Claude Code arm `wait_for_answer` and end the turn.
4. Make a call self-contained. Include the options, because the user hears it once. Put digits the user must read back (an IBAN, a code, a long URL) in a `text` first and point to it in the call, since speech transcription mangles them.
5. Follow a call with `poll_result` until it settles. `status` is `completed` with the transcript, `missed` after about a minute of ringing, or `declined`. After a missed call, send a text and wait with `wait_for_reply`. If a call is declined, do not retry the call: send a text.
6. Use only the user's own number. The `from` in every result is the agent's identity: never call or text it. Five numbers in an hour that are not /call-me numbers get the caller blocked for an hour.
7. Pass `language` (for example `tr`) on `call` and `say` when speaking a language other than English, and always `hang_up` when the conversation is done.

Where the MCP tools are not available, the same service has a REST route that needs no plugin or registration. The 10-digit number is the credential and the request blocks until the spoken answer returns:

```sh
CALLME_TO=$(jq -r .user_number ~/.aiphone/config.json)
curl -sS https://callmemcp.com/ring \
  -H 'content-type: application/json' \
  -d "$(jq -nc --arg to "$CALLME_TO" --arg text "Should I deploy to prod?" \
    --arg from "Codex" '{to:$to,text:$text,from:$from}')"
```

`POST /text` with `body` in place of `text` sends a non-blocking notification.

## Licensing

The plugin, skill and client code in `radres/call-me` are MIT licensed. The calling service at `callmemcp.com` is a hosted, closed-source commercial service. Using it needs the paid /call-me app subscription: weekly at $4.99 with a 3-day free trial, or yearly at $84.99. There is no free plan beyond the trial.

## Documentation

- Site and privacy policy: https://callmemcp.com and https://callmemcp.com/privacy
- Plugin and MCP setup: https://github.com/radres/call-me#readme
- Official MCP Registry entry: `com.callmemcp/call-me`
