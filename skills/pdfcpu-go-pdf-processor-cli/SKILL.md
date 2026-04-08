---
title: pdfcpu Go PDF Processor and Manipulation CLI
description: 'pdfcpu is a comprehensive PDF processing library written in Go that
  provides both a command-line interface and a Go API for manipulating PDF files.
  It supports PDF specification versions up to 2.0 and handles the full range of PDF
  operations that developers and document automation workflows require. Core Operations
  The CLI covers essential PDF tasks: pdfcpu merge combines multiple PDFs into one,
  pdfcpu split breaks a PDF into individual pages or page ranges, pdfcpu trim removes
  pages, and pdfcpu rotate adjusts page orientation. For document assembly, pdfcpu
  booklet and pdfcpu nup arrange multiple pages onto single sheets for printing. Validation
  and Optimization Use pdfcpu validate to check PDF conformance against the spec.
  The pdfcpu optimize command reduces file size by removing redundant objects, linearizing
  the file for fast web viewing, and compressing streams. This is particularly useful
  in document pipelines where PDFs pass through multiple processing stages and accumulate
  overhead. Watermarks and Stamps pdfcpu supports text, image, and PDF watermarks
  with full control over position, rotation, opacity, and scaling. Use pdfcpu stamp
  to add stamps on top of content or pdfcpu watermark to place them behind content.
  Multi-page stamp PDFs allow different stamps per page. Encryption and Security The
  tool supports AES-128, AES-256, and RC4 encryption. Use pdfcpu encrypt to set user
  and owner passwords, and pdfcpu permissions to control printing, copying, and modification
  rights. pdfcpu decrypt removes encryption when the password is known. Form Filling
  pdfcpu can fill PDF forms programmatically via JSON input with pdfcpu form fill
  . Export form field data with pdfcpu form export . This enables automated document
  generation from templates in billing, contracts, and compliance workflows. Installation
  Install via Go with go install github.com/pdfcpu/pdfcpu/cmd/pdfcpu@latest , via
  Homebrew with brew install pdfcpu , or download pre-built binaries from the GitHub
  releases page. Docker images are also available.'
verification: security_reviewed
source: https://github.com/pdfcpu/pdfcpu
category:
- Developer Tools
framework:
- Custom Agents
tool_ecosystem:
  github_repo: pdfcpu/pdfcpu
  github_stars: 8550
---

# pdfcpu Go PDF Processor and Manipulation CLI

pdfcpu is a comprehensive PDF processing library written in Go that provides both a command-line interface and a Go API for manipulating PDF files. It supports PDF specification versions up to 2.0 and handles the full range of PDF operations that developers and document automation workflows require. Core Operations The CLI covers essential PDF tasks: pdfcpu merge combines multiple PDFs into one, pdfcpu split breaks a PDF into individual pages or page ranges, pdfcpu trim removes pages, and pdfcpu rotate adjusts page orientation. For document assembly, pdfcpu booklet and pdfcpu nup arrange multiple pages onto single sheets for printing. Validation and Optimization Use pdfcpu validate to check PDF conformance against the spec. The pdfcpu optimize command reduces file size by removing redundant objects, linearizing the file for fast web viewing, and compressing streams. This is particularly useful in document pipelines where PDFs pass through multiple processing stages and accumulate overhead. Watermarks and Stamps pdfcpu supports text, image, and PDF watermarks with full control over position, rotation, opacity, and scaling. Use pdfcpu stamp to add stamps on top of content or pdfcpu watermark to place them behind content. Multi-page stamp PDFs allow different stamps per page. Encryption and Security The tool supports AES-128, AES-256, and RC4 encryption. Use pdfcpu encrypt to set user and owner passwords, and pdfcpu permissions to control printing, copying, and modification rights. pdfcpu decrypt removes encryption when the password is known. Form Filling pdfcpu can fill PDF forms programmatically via JSON input with pdfcpu form fill . Export form field data with pdfcpu form export . This enables automated document generation from templates in billing, contracts, and compliance workflows. Installation Install via Go with go install github.com/pdfcpu/pdfcpu/cmd/pdfcpu@latest , via Homebrew with brew install pdfcpu , or download pre-built binaries from the GitHub releases page. Docker images are also available.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/pdfcpu-go-pdf-processor-cli/)
