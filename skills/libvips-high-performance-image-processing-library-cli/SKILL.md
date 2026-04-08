---
title: libvips High-Performance Image Processing Library and CLI
description: libvips is a high-performance image processing library written in C that
  uses a demand-driven, horizontally threaded pipeline architecture. This design means
  it processes images in small tiles that flow through the operation pipeline on demand,
  keeping memory usage low while fully utilizing multi-core CPUs. Benchmarks consistently
  show libvips running faster and using significantly less memory than comparable
  libraries like ImageMagick and GraphicsMagick. Operations and Format Support libvips
  provides approximately 300 image processing operations covering arithmetic, histograms,
  convolution, morphological operations, frequency filtering, colour management (ICC
  profiles via liblcms), resampling, and statistics. It handles numeric types from
  8-bit integer to 128-bit complex, with images supporting any number of bands. Format
  support includes JPEG, JPEG 2000, JPEG XL, TIFF, PNG, WebP, HEIC, AVIF, FITS, PDF,
  SVG, HDR, GIF, OpenEXR, DeepZoom, NIfTI, and OpenSlide, with fallback to ImageMagick
  for additional formats like DICOM. Command-Line Interface libvips includes a CLI
  tool called vips that exposes all operations as subcommands. Common tasks like thumbnail
  generation, format conversion, and batch resizing can be performed directly from
  the terminal. The CLI supports piping and shell scripting, making it straightforward
  to integrate into automated image processing pipelines. Language Bindings Beyond
  the native C and C++ APIs, libvips has bindings for Python (pyvips), Ruby (ruby-vips),
  PHP (php-vips), C#/.NET (NetVips), Go (vips-gen), Lua, Crystal, Elixir (vix), Java
  (vips-ffm), and Nim. The Node.js Sharp library, one of the most popular image processing
  packages on npm, uses libvips as its processing engine. Real-World Usage libvips
  powers image processing in Mastodon (social media), Sharp (Node.js), imgproxy (image
  CDN proxy), Ruby on Rails Active Storage, CarrierWave, and MediaWiki. Its low memory
  footprint and high throughput make it the preferred choice for server-side image
  processing at scale. Installation libvips is available through most Linux package
  managers ( apt install libvips-tools ), Homebrew on macOS ( brew install vips ),
  and pre-built Windows binaries from GitHub releases. Building from source uses the
  Meson build system. The library is licensed under LGPL-2.1-or-later.
verification: security_reviewed
source: https://github.com/libvips/libvips
category:
- Image &amp; Creative Automation
framework:
- Multi-Framework
tool_ecosystem:
  github_repo: libvips/libvips
  github_stars: 11197
---

# libvips High-Performance Image Processing Library and CLI

libvips is a high-performance image processing library written in C that uses a demand-driven, horizontally threaded pipeline architecture. This design means it processes images in small tiles that flow through the operation pipeline on demand, keeping memory usage low while fully utilizing multi-core CPUs. Benchmarks consistently show libvips running faster and using significantly less memory than comparable libraries like ImageMagick and GraphicsMagick. Operations and Format Support libvips provides approximately 300 image processing operations covering arithmetic, histograms, convolution, morphological operations, frequency filtering, colour management (ICC profiles via liblcms), resampling, and statistics. It handles numeric types from 8-bit integer to 128-bit complex, with images supporting any number of bands. Format support includes JPEG, JPEG 2000, JPEG XL, TIFF, PNG, WebP, HEIC, AVIF, FITS, PDF, SVG, HDR, GIF, OpenEXR, DeepZoom, NIfTI, and OpenSlide, with fallback to ImageMagick for additional formats like DICOM. Command-Line Interface libvips includes a CLI tool called vips that exposes all operations as subcommands. Common tasks like thumbnail generation, format conversion, and batch resizing can be performed directly from the terminal. The CLI supports piping and shell scripting, making it straightforward to integrate into automated image processing pipelines. Language Bindings Beyond the native C and C++ APIs, libvips has bindings for Python (pyvips), Ruby (ruby-vips), PHP (php-vips), C#/.NET (NetVips), Go (vips-gen), Lua, Crystal, Elixir (vix), Java (vips-ffm), and Nim. The Node.js Sharp library, one of the most popular image processing packages on npm, uses libvips as its processing engine. Real-World Usage libvips powers image processing in Mastodon (social media), Sharp (Node.js), imgproxy (image CDN proxy), Ruby on Rails Active Storage, CarrierWave, and MediaWiki. Its low memory footprint and high throughput make it the preferred choice for server-side image processing at scale. Installation libvips is available through most Linux package managers ( apt install libvips-tools ), Homebrew on macOS ( brew install vips ), and pre-built Windows binaries from GitHub releases. Building from source uses the Meson build system. The library is licensed under LGPL-2.1-or-later.

## Installation

Choose the method that fits your setup:

1. Install from the Agent Skill Exchange UI
2. Clone or copy the skill into your local skills directory
3. Install with a compatible skill manager or CLI
4. Add it to your agent workspace manually
5. Fork and customize it for your own environment

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/libvips-high-performance-image-processing-library-cli/)
