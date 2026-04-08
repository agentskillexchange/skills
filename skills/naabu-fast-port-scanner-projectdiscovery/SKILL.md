---
title: Naabu Fast Port Scanner by ProjectDiscovery
description: 'Overview Naabu is a high-performance port scanning tool written in Go,
  developed by ProjectDiscovery — the team behind Nuclei, httpx, subfinder, and other
  widely-used security tools. It is designed for fast, reliable port enumeration during
  bug bounty hunting, penetration testing, and attack surface discovery. Naabu focuses
  on simplicity and composability, producing clean output that pipes directly into
  other ProjectDiscovery tools. How It Works Naabu performs SYN, CONNECT, or UDP probe-based
  scanning against target hosts. It accepts input from STDIN, files, individual hosts,
  CIDR ranges, or ASN identifiers. Results are output in JSON, CSV, or plain text
  format. The tool automatically deduplicates IP addresses resolved from DNS and can
  exclude CDN/WAF ranges from full scans. Key Features Fast SYN/CONNECT/UDP scanning:
  Optimized packet sending with configurable rate limiting (default 1000 packets/sec)
  and parallel workers. Multiple input formats: Accepts hosts, IP addresses, CIDR
  ranges, ASN numbers, and file lists. Nmap integration: Pass discovered open ports
  directly to Nmap for service version detection using the -nmap-cli flag. CDN/WAF
  exclusion: Automatically detect and exclude CDN-protected hosts from full port scans,
  only scanning ports 80 and 443. Passive enumeration: Query Shodan InternetDB API
  for passive port discovery without sending any packets. IPv4 and IPv6: Supports
  both address families with configurable preference. Host discovery: Built-in host
  discovery mode using TCP SYN, TCP ACK, ICMP echo, and ARP probes. Agent Integration
  Security-focused agents can use Naabu as the first step in an automated reconnaissance
  pipeline: enumerate open ports with Naabu, pipe results to httpx for HTTP probing,
  then to Nuclei for vulnerability scanning. The JSON output mode makes it easy to
  parse results programmatically for further automated analysis. Installation # Via
  Go go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest # Via Homebrew
  brew install naabu # Via Docker docker pull projectdiscovery/naabu:latest Example
  Usage # Scan top 100 ports on a host naabu -host example.com # Scan specific ports
  with JSON output naabu -host 192.168.1.0/24 -p 80,443,8080 -json -o results.json
  # Passive port enumeration via Shodan naabu -host example.com -passive # Pipe to
  Nmap for service detection naabu -host example.com -nmap-cli ''nmap -sV -oX nmap-output'''
verification: security_reviewed
source: https://github.com/projectdiscovery/naabu
category:
- Security &amp; Verification
framework:
- Multi-Framework
---

# Naabu Fast Port Scanner by ProjectDiscovery

Overview Naabu is a high-performance port scanning tool written in Go, developed by ProjectDiscovery — the team behind Nuclei, httpx, subfinder, and other widely-used security tools. It is designed for fast, reliable port enumeration during bug bounty hunting, penetration testing, and attack surface discovery. Naabu focuses on simplicity and composability, producing clean output that pipes directly into other ProjectDiscovery tools. How It Works Naabu performs SYN, CONNECT, or UDP probe-based scanning against target hosts. It accepts input from STDIN, files, individual hosts, CIDR ranges, or ASN identifiers. Results are output in JSON, CSV, or plain text format. The tool automatically deduplicates IP addresses resolved from DNS and can exclude CDN/WAF ranges from full scans. Key Features Fast SYN/CONNECT/UDP scanning: Optimized packet sending with configurable rate limiting (default 1000 packets/sec) and parallel workers. Multiple input formats: Accepts hosts, IP addresses, CIDR ranges, ASN numbers, and file lists. Nmap integration: Pass discovered open ports directly to Nmap for service version detection using the -nmap-cli flag. CDN/WAF exclusion: Automatically detect and exclude CDN-protected hosts from full port scans, only scanning ports 80 and 443. Passive enumeration: Query Shodan InternetDB API for passive port discovery without sending any packets. IPv4 and IPv6: Supports both address families with configurable preference. Host discovery: Built-in host discovery mode using TCP SYN, TCP ACK, ICMP echo, and ARP probes. Agent Integration Security-focused agents can use Naabu as the first step in an automated reconnaissance pipeline: enumerate open ports with Naabu, pipe results to httpx for HTTP probing, then to Nuclei for vulnerability scanning. The JSON output mode makes it easy to parse results programmatically for further automated analysis. Installation # Via Go go install -v github.com/projectdiscovery/naabu/v2/cmd/naabu@latest # Via Homebrew brew install naabu # Via Docker docker pull projectdiscovery/naabu:latest Example Usage # Scan top 100 ports on a host naabu -host example.com # Scan specific ports with JSON output naabu -host 192.168.1.0/24 -p 80,443,8080 -json -o results.json # Passive port enumeration via Shodan naabu -host example.com -passive # Pipe to Nmap for service detection naabu -host example.com -nmap-cli 'nmap -sV -oX nmap-output'

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/naabu-fast-port-scanner-projectdiscovery/)
