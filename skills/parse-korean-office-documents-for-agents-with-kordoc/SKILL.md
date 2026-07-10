---
name: "Parse Korean office documents for agents with kordoc"
slug: "parse-korean-office-documents-for-agents-with-kordoc"
description: "Use kordoc when an agent needs to parse HWP, HWPX, PDF, Excel, or DOCX files into Markdown, fill forms, compare documents, or expose document tools through MCP."
github_stars: 1364
verification: "security_reviewed"
source: "https://github.com/chrisryugj/kordoc"
author: "chrisryugj"
publisher_type: "individual"
category: "Data Extraction & Transformation"
framework: "MCP"
tool_ecosystem:
  github_repo: "chrisryugj/kordoc"
  github_stars: 1364
  npm_package: "kordoc"
  npm_weekly_downloads: 34493
---

# Parse Korean office documents for agents with kordoc

Use kordoc when an agent needs to parse HWP, HWPX, PDF, Excel, or DOCX files into Markdown, fill forms, compare documents, or expose document tools through MCP.

## Prerequisites

Node.js 18+, npx or npm, kordoc CLI or MCP server, supported AI client such as Claude Desktop, Cursor, Claude Code, Windsurf, VS Code, Gemini CLI, Zed, or Antigravity

## Installation

Requirements and caveats from upstream:
- **CJS 빌드 수정** — require("kordoc") 시 import.meta SyntaxError 나던 버그 수정.
- **CI**: Node 18 ESM __dirname 미정의로 테스트 매트릭스가 실패하던 문제 수정
- 중첩표 구조 보존(IRCell.blocks), 한컴 PUA 매핑, HWP5 이미지 추출(0→90건), 자동번호 카운터, 머리말/각주 정밀 처리 등. 채점기·코퍼스 수집기·게이트는 bench/에 포함 — node bench/score.mjs로 재현 가능.

Basic usage or getting-started notes:
- **🐛 HWPX 양식 채우기 빈 셀 버그픽스** (#29, #30) — 한컴오피스에서 HWP→HWPX 로 변환한 양식의 빈 값 셀(<hp:run> 이 <hp:t> 자식 없이 self-closing)에 값이 삽입되지 않으면서 결과에는 성공으로 보고되던 false-positive 수정. setRunText 가 <hp:t> 없는 run 에 새로 생성해 텍스트 삽입. 기여: @amnotyoung
- **📄 대형 HWPX 정부문서 파싱** — <p>><run>><tbl> 구조의 중첩 테이블 파싱 누락 수정.

- Source: https://github.com/chrisryugj/kordoc
- Extracted from upstream docs: https://raw.githubusercontent.com/chrisryugj/kordoc/HEAD/README.md

## Documentation

- https://www.npmjs.com/package/kordoc

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/parse-korean-office-documents-for-agents-with-kordoc/)
