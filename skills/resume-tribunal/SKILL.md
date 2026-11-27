---
name: "Resume Tribunal"
slug: "resume-tribunal"
description: "Tailors a resume or CV to one job posting using only the user's own facts, then has an AI from a different company review the draft blind, with a script that flags numbers and names it cannot find in the user's words. Use when someone wants a resume or CV rewritten or reviewed for a specific job."
github_stars: 1
verification: "listed"
source: "https://github.com/mohiddin7/resume-tribunal"
author: "Mohiddin"
category: "Templates & Workflows"
framework: "Claude Code"
tool_ecosystem:
  github_repo: "mohiddin7/resume-tribunal"
  github_stars: 1
---

# Resume Tribunal

Resume Tribunal is an Agent Skill (a SKILL.md, MIT licensed) that tailors one resume to one job posting. The user supplies the job link and a resume as pasted text, .docx, .pdf or Markdown. One assistant rewrites the resume using only facts the user gave it. A second assistant from a different company then reviews the draft without being told who wrote it, looking for anything exaggerated or made up. An optional Python 3 checker flags numbers and names it cannot find in the user's own words, checks layout and AI-sounding phrases, and can produce a PDF. The user approves each changed line before getting the file.

The result is a resume the user can send, a list of what the job asks for that the resume does not show yet, and the interview questions its claims are likely to prompt. It works in chat-only assistants such as ChatGPT, Gemini and Claude, where it hands the user a block of text to paste into a second app, and in coding agents such as Claude Code, Codex, Gemini CLI, Cursor, GitHub Copilot and OpenCode, where it can run the second assistants automatically on accounts already signed in. Use it when someone wants a resume or CV tailored, rewritten, fixed or reviewed for a role. It has no server and asks for no sign-up.

## Installation

Install or set up from the source-backed instructions:

npx skills add mohiddin7/resume-tribunal

- Source: https://github.com/mohiddin7/resume-tribunal

