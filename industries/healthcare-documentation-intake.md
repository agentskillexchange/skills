# 🩺 Healthcare Documentation & Intake

Documentation intake, OCR, transcription, structured extraction, and biomedical literature support for paperwork-heavy workflows.

- Live page: https://agentskillexchange.com/industry-skills/#healthcare-documentation-intake
- Homepage access: Curated Collections on https://agentskillexchange.com/

## Who this is for

- Healthcare operations, intake, research, and documentation teams handling paperwork-heavy non-clinical workflows.
- Teams that need PHI-aware extraction and literature support with explicit human review boundaries.

## Jobs covered

- Extract text and tables from intake forms and scanned records.
- Transcribe documentation audio into reviewable text.
- Query literature and FHIR resources for documentation support.
- Redact sensitive fields before downstream sharing.

## Workflow Stacks

- **Non-clinical intake packet:** OCR forms → extract structured fields → redact sensitive data → route for human review
- **Literature support:** Search PubMed → collect citations → summarize findings → preserve source links
- **Mixed-document intake extraction:** Ingest mixed files → OCR scanned layouts → extract tables and metadata → redact sensitive data → route for human review

## Recommended Picks

| Skill | What it does here | Persona | Install | Stars |
|---|---|---|---|---:|
| [PubMed Literature Mining Agent](../skills/pubmed-literature-mining-agent/) | Adds literature lookup for documentation and research support without making clinical recommendations. | Research coordinator / medical writer | Medium | — |
| [LangExtract LLM-Powered Structured Text Extraction](../skills/langextract-llm-structured-text-extraction/) | Extracts structured fields from intake notes, letters, and forms for human-reviewed documentation. | Documentation analyst / intake ops | Medium | 35k |
| [OCRmyPDF Searchable PDF OCR Pipeline](../skills/ocrmypdf-searchable-pdf-ocr-pipeline/) | Makes scanned forms and records searchable before routing or summarization. | Intake coordinator / records ops | Medium | 33.2k |
| [WhisperX Speech Recognition with Word-Level Timestamps and Diarization](../skills/whisperx-speech-recognition-timestamps-diarization/) | Transcribes documentation audio with speaker and word timing for reviewable notes. | Transcription ops / documentation lead | High | 21k |
| [DocuSeal Open Source Document Signing and PDF Form Platform](../skills/docuseal-document-signing-pdf-forms/) | Supports consent, intake, and administrative forms that need signatures and structured PDF fields. | Clinic admin / forms coordinator | Medium | 11.7k |
| [pdfplumber Python PDF Text and Table Extraction Library](../skills/pdfplumber-python-pdf-text-table-extraction/) | Extracts tables and structured text from lab-style PDFs, referrals, and administrative packets. | Data coordinator / intake analyst | Medium | 10.1k |
| [Expose FHIR healthcare data resources to MCP agents with review boundaries](../skills/expose-fhir-healthcare-data-resources-to-mcp-agents-with-review-boundaries/) | Lets agents inspect FHIR resources with explicit PHI and clinical-use boundaries. | Health IT engineer / integration lead | High | 80 |
| [Apache Tika Document Extractor](../skills/apache-tika-document-extractor/) | Extracts text from mixed intake files, office documents, and uploaded paperwork. | Health records ops / integration engineer | High | 3.7k |
| [Apache Tika Document Parser](../skills/apache-tika-document-parser/) | Adds metadata and embedded-object parsing for mixed healthcare document packets. | Health data engineer / archive specialist | High | 3.7k |
| [Parse local PDFs into agent-ready text, JSON, and screenshots with LiteParse](../skills/parse-local-pdfs-into-agent-ready-text-json-and-screenshots-with-liteparse/) | Keeps local PDF extraction inspectable with text, JSON, and screenshots before PHI-sensitive review. | AI ops / documentation QA | Medium | 5.1k |
| [Redact PII from text before sharing or indexing with scrubadub](../skills/redact-pii-from-text-before-sharing-or-indexing-with-scrubadub/) | Removes obvious identifiers before documentation text is shared, indexed, or sent downstream. | Privacy reviewer / documentation ops | Low | 421 |
| [Surya Document OCR with Layout Analysis and Table Recognition](../skills/surya-document-ocr-layout-analysis-table-recognition/) | Adds layout-aware OCR and table recognition for scanned forms, records, and intake packets. | Health records ops / documentation analyst | High | 19.5k |
| [Extract structured text, metadata, tables, and images from mixed documents through an MCP server with Kreuzberg](../skills/extract-structured-text-metadata-tables-and-images-from-mixed-documents-through-an-mcp-server-with-kreuzberg/) | Gives agents one MCP-accessible extraction layer for PDFs, Office files, images, HTML, and other mixed healthcare intake inputs. | Health data engineer / AI documentation ops | High | 7.6k |

## Editorial Notes

- This collection is explicitly not diagnosis, treatment, or medical decision support.
- Prefer documentation, intake, transcription, extraction, and review workflows with audit-friendly outputs.
- Keep the framing explicitly non-clinical. This is for documentation, intake, extraction, transcription, and literature support — not diagnosis or medical decision support.

## Adjacent Collections

- [Legal Ops & Compliance](legal-ops-compliance.md)
- [Media & Publishing Systems](media-publishing-systems.md)

---

[← Back to industry collections](README.md)
