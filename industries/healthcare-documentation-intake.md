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
| [Parse multilingual documents for agent ingestion with dots.ocr](../skills/parse-multilingual-documents-for-agent-ingestion-with-dots-ocr/) | Adds multilingual layout parsing for intake forms, referrals, and mixed-language documentation queues before human review. | Healthcare intake ops / document automation engineer | High | 8.9k |
| [Expose FHIR healthcare data resources to MCP agents with review boundaries](../skills/expose-fhir-healthcare-data-resources-to-mcp-agents-with-review-boundaries/) | Lets agents inspect FHIR resources with explicit PHI and clinical-use boundaries. | Health IT engineer / integration lead | High | 80 |
| [Unstructured Document ETL for LLM Pipelines](../skills/unstructured-document-etl-for-llm-pipelines/) | Chunks and normalizes intake packets into structured elements before PHI-aware retrieval or abstraction workflows. | Healthcare data ops / retrieval engineer | High | 14.4k |
| [Beautiful Soup Academic Paper Parser](../skills/beautifulsoup-academic-paper-parser/) | Parses PubMed and scholarly HTML metadata so literature-support packets keep citations, authors, and source links intact. | Research coordinator / evidence reviewer | Medium | — |
| [Surya Document OCR with Layout Analysis and Table Recognition](../skills/surya-document-ocr-layout-analysis-table-recognition/) | Adds layout-aware OCR and table recognition for scanned forms, records, and intake packets. | Health records ops / documentation analyst | High | 19.5k |
| [PaddleOCR Multilingual Document OCR and Structured Data Toolkit](../skills/paddleocr-multilingual-document-ocr-toolkit/) | Adds multilingual OCR and structured extraction for scanned intake forms, referral packets, and mixed-language documentation queues. | Healthcare intake ops / document automation engineer | High | 73.7k |
| [Whisper.cpp Local Transcription Engine](../skills/whisper-cpp-local-transcription-engine/) | Provides a local transcription option for documentation audio when teams want reviewable text artifacts without sending recordings through a hosted service. | Clinical documentation ops / transcription engineer | Medium | 51.7k |
| [Extract structured text, metadata, tables, and images from mixed documents through an MCP server with Kreuzberg](../skills/extract-structured-text-metadata-tables-and-images-from-mixed-documents-through-an-mcp-server-with-kreuzberg/) | Gives agents one MCP-accessible extraction layer for PDFs, Office files, images, HTML, and other mixed healthcare intake inputs. | Health data engineer / AI documentation ops | High | 7.6k |
| [Tesseract OCR Document Extractor](../skills/tesseract-ocr-document-extractor/) | Adds a proven OCR path for scanned intake forms, referral packets, and legacy paperwork before human review. | Healthcare intake ops / document automation engineer | Medium | 73.6k |
| [Build OCR and layout-analysis preprocessing pipelines with deepdoctection](../skills/build-ocr-and-layout-analysis-preprocessing-pipelines-with-deepdoctection/) | Adds layout-aware preprocessing for forms, tables, and multi-section medical paperwork before human review. | Healthcare data ops engineer | High | 3.2k |

## Editorial Notes

- This collection is explicitly not diagnosis, treatment, or medical decision support.
- Prefer documentation, intake, transcription, extraction, and review workflows with audit-friendly outputs.
- Generic parser alternatives are intentionally limited in favor of non-clinical healthcare intake, documentation, transcription, FHIR, literature, and human-review workflows.
- Keep the framing explicitly non-clinical. This is for documentation, intake, extraction, transcription, and literature support — not diagnosis or medical decision support.

## Adjacent Collections

- [Legal Ops & Compliance](legal-ops-compliance.md)
- [Media & Publishing Systems](media-publishing-systems.md)

---

[← Back to industry collections](README.md)
