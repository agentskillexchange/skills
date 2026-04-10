---
name: "mitmproxy Interactive HTTPS Proxy for Debugging and Security Testing"
description: "mitmproxy is an interactive, SSL/TLS-capable intercepting HTTP proxy for penetration testers and software developers. It supports HTTP/1, HTTP/2, HTTP/3, and WebSockets, offering console, command-line, and web-based interfaces for intercepting, inspecting, modifying, and replaying web traffic."
verification: security_reviewed
source: "https://github.com/mitmproxy/mitmproxy"
category:
  - "Security &amp; Verification"
framework:
  - "Custom Agents"
tool_ecosystem:
  github_repo: "mitmproxy/mitmproxy"
  github_stars: 42881
---

# mitmproxy Interactive HTTPS Proxy for Debugging and Security Testing

mitmproxy is a free, open-source interactive HTTPS proxy that serves as a swiss-army knife for debugging, testing, privacy measurements, and penetration testing. It can intercept, inspect, modify, and replay web traffic including HTTP/1, HTTP/2, HTTP/3, WebSockets, and any other SSL/TLS-protected protocol. The project has been actively developed for over a decade and is one of the most widely-used tools in web security and development.
Three Interfaces
mitmproxy ships with three distinct interfaces. The main mitmproxy tool provides an interactive console interface in the terminal for real-time traffic inspection and modification. mitmdump is the command-line version — think tcpdump for HTTP — ideal for scripted and automated workflows. mitmweb provides a modern web-based interface for those who prefer a GUI. All three interfaces share the same core engine and support the same features.
Core Capabilities
The proxy transparently intercepts HTTPS traffic using dynamically generated certificates. It supports request and response modification on the fly, traffic replay for testing, flow filtering and search, and scripting via a powerful Python addon API. The addon system allows developers to write custom scripts that hook into any point of the proxy lifecycle — from connection setup through request handling and response delivery.
Agent Integration
An AI agent can leverage mitmproxy for API debugging and reverse engineering, automated security testing of web applications, monitoring and logging HTTP traffic for analysis, testing webhook integrations by intercepting and modifying payloads, and privacy auditing by inspecting what data applications send. The Python addon API makes it straightforward to build custom automation that programmatically inspects and modifies traffic flows based on agent decisions.

## Installation

You can install this skill using one of these methods:

1. Install from the Agent Skill Exchange UI
2. Clone or download this repository and copy the skill folder into your skills directory
3. Install with the relevant package manager if the upstream project provides one
4. Add it manually to your local OpenClaw skill collection
5. Use the upstream project install flow documented by the publisher

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/mitmproxy-interactive-https-proxy-debugging-security/)
