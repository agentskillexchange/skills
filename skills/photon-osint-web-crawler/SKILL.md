---
name: "Photon High-Speed OSINT Web Crawler and Data Extractor"
slug: "photon-osint-web-crawler"
description: "Photon is a blazing-fast Python web crawler purpose-built for OSINT operations. It extracts URLs, emails, social media accounts, files, secret keys, JavaScript endpoints, and subdomains from target websites with multithreaded efficiency."
github_stars: 12795
verification: "security_reviewed"
source: "https://github.com/s0md3v/Photon"
category: "Research & Scraping"
framework: "Multi-Framework"
tool_ecosystem:
  github_repo: "s0md3v/Photon"
  github_stars: 12795
---

# Photon High-Speed OSINT Web Crawler and Data Extractor

Photon is a blazing-fast Python web crawler purpose-built for OSINT operations. It extracts URLs, emails, social media accounts, files, secret keys, JavaScript endpoints, and subdomains from target websites with multithreaded efficiency.

## Installation

Use the upstream install or setup path that matches your environment:
- $ git clone https://github.com/s0md3v/Photon.git
- $ docker build -t photon .
- $ docker run -it --name photon photon:latest -u google.com
- $ docker run -it --name photon -v "$PWD:/Photon/google.com" photon:latest -u google.com

Requirements and caveats from upstream:
- #### Docker
- Photon can be launched using a lightweight Python-Alpine (103 MB) Docker image.
- To view results, you can either head over to the local docker volume, which you can find by running docker inspect photon or by mounting the target loot folder:

Basic usage or getting-started notes:
- <a href="https://github.com/s0md3v/Photon/wiki/Usage">How To Use</a> •
- URLs with parameters (example.com/gallery.php?id=2)
- The extracted information is saved in an organized manner or can be [exported as json](https://github.com/s0md3v/Photon/wiki/Usage#export-formatted-result).

- Source: https://github.com/s0md3v/Photon
- Extracted from upstream docs: https://raw.githubusercontent.com/s0md3v/Photon/HEAD/README.md

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/photon-osint-web-crawler/)
