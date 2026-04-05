---
name: "ExifTool Metadata Reader and Writer for Images and Files"
description: "ExifTool by Phil Harvey is a comprehensive Perl-based CLI tool for reading, writing, and editing metadata in over 400 file types. It extracts EXIF, IPTC, XMP, GPS, and maker note data from images, videos, audio, PDFs, and documents, making it the industry standard for metadata forensics and batch processing."
category: "Data Extraction &amp; Transformation"
framework: "Multi-Framework"
verification: security_reviewed
source: "https://github.com/exiftool/exiftool"
tool_ecosystem:
  github_repo: "exiftool/exiftool"
  github_stars: 4560
---
# ExifTool Metadata Reader and Writer for Images and Files

ExifTool by Phil Harvey is a comprehensive Perl-based CLI tool for reading, writing, and editing metadata in over 400 file types. It extracts EXIF, IPTC, XMP, GPS, and maker note data from images, videos, audio, PDFs, and documents, making it the industry standard for metadata forensics and batch processing.

ExifTool is a platform-independent Perl library and command-line application created and maintained by Phil Harvey for reading, writing, and manipulating meta information in a wide variety of file formats. It supports over 400 file types and recognizes thousands of metadata tags, making it the most comprehensive metadata tool available.

Supported Formats and Tags ExifTool handles EXIF, GPS, IPTC, XMP, JFIF, GeoTIFF, ICC Profile, Photoshop IRB, FlashPix, AFCP, ID3, and maker note metadata formats. It reads metadata from virtually every image format (JPEG, PNG, TIFF, RAW variants from Canon, Nikon, Sony, and dozens of other manufacturers), video formats (MP4, MOV, AVI, MKV), audio files (MP3, FLAC, WAV), documents (PDF, DOCX, XLSX), and more. Writing capabilities cover most major formats.

CLI Usage The command-line interface is powerful yet accessible: exiftool photo.jpg displays all metadata, exiftool -GPSLatitude -GPSLongitude *.jpg extracts specific tags in batch, and exiftool -Artist="Name" -Copyright="2026" photo.jpg writes metadata. Advanced features include conditional tag operations, structured output in JSON/XML/CSV, recursive directory processing, and filename-based date renaming (exiftool "-FileName<DateTimeOriginal" -d "%Y%m%d_%H%M%S.%%e" dir/).

Agent Skill Applications As an agent skill, ExifTool enables automated metadata extraction for digital asset management, GPS coordinate harvesting from photo collections for mapping, copyright and attribution stamping across image libraries, metadata stripping for privacy before publication, and forensic analysis of image authenticity. Agents can use its JSON output mode (-json) for structured data pipelines and integrate with image processing workflows for automated cataloging.

Distribution and Licensing ExifTool is distributed under the Perl Artistic License and GPL. It runs on any platform with Perl (macOS, Linux, Windows) and is available via package managers (apt, brew, choco) or from the official GitHub repository and exiftool.org. The project has been actively maintained since 2003 with frequent releases adding support for new camera models and file formats.

## Installation

### Any Agent

```bash
npx skills add agentskillexchange/skills --skill exiftool-metadata-reader-writer-images-files
```

### Claude Code

```bash
npx skills add agentskillexchange/skills --skill exiftool-metadata-reader-writer-images-files -a claude-code
```

### Cursor

```bash
npx skills add agentskillexchange/skills --skill exiftool-metadata-reader-writer-images-files -a cursor
```

### Codex

```bash
npx skills add agentskillexchange/skills --skill exiftool-metadata-reader-writer-images-files -a codex
```

### OpenClaw

```bash
clawhub install exiftool-metadata-reader-writer-images-files
```

## Source

- [Agent Skill Exchange](https://agentskillexchange.com/skills/exiftool-metadata-reader-writer-images-files/)
