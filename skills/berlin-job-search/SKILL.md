---
name: "Berlin Job Search"
slug: "berlin-job-search"
description: "AI job-search coach for Berlin and the rest of Germany. Searches live postings (Bundesagentur für Arbeit API, Arbeitnow, LinkedIn guest jobs, Daily Berlin Jobs for Berlin tech, public Greenhouse/Lever/Ashby/Personio boards), quotes German-language requirements, checks salaries against 2026 EU Blue Card thresholds, writes a German Lebenslauf/Anschreiben or English CV as PDF, runs mock interviews and tracks applications. Use for any job search in Germany."
github_stars: 0
verification: "listed"
source: "https://github.com/umutyesildal/berlin-job-search"
author: "umutyesildal"
category: "Templates & Workflows"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "umutyesildal/berlin-job-search"
---

# Berlin Job Search

Berlin Job Search teaches an AI agent the unwritten rules of job hunting in Germany, and gives it live job data plus deterministic tools for the boring parts.

- **Search:** bilingual queries (for example *Software Engineer* and *Softwareentwickler*) against the Bundesagentur für Arbeit Jobsuche v6 API, Arbeitnow, LinkedIn's logged-out guest job search, Daily Berlin Jobs (Berlin tech roles) and 33 public company ATS boards. Sources are chosen per field, and an optional phrase-based title filter removes off-target results.
- **Check:** whether German is really required (with the quoted sentence), annualised salary against the 2026 EU Blue Card thresholds, agency/Zeitarbeit flags, contract terms, and hidden instruction-shaped text aimed at AI agents.
- **Apply:** a writer pass and an independent reviewer pass that traces every claim back to the user's CV, then a German Lebenslauf/Anschreiben or English CV rendered to PDF with local Chrome and an ATS check. It never invents experience and never submits anything.
- **Interview and track:** mock interviews with scored feedback, an application tracker with follow-up reminders, and an offline HTML dashboard.

The scripts are Python 3.9+ standard library only and need no API keys. User data stays on the user's machine in `job-search/` (or `$GJS_DATA_DIR`). Inside a Git repository, the scripts give that folder its own `.gitignore` before the first write, and the skill runs `tracker.py protect` before saving any personal data; already-tracked files are reported, never changed.

## Installation

No source-backed install or usage instructions could be extracted automatically. Review the upstream project before running this skill in a sensitive workflow.

- Source: https://github.com/umutyesildal/berlin-job-search

## Usage

Ask, for example: "Find English-friendly product manager jobs in Munich from this week and tell me which ones really need German."
