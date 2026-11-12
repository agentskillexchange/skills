# OSINT playbook

## Contents

1. Choose methods by the evidential question
2. Search, language, and source discovery
3. Archives and document reconstruction
4. Image, video, and audio verification
5. Geolocation and chronolocation
6. Corporate, money, and public-record research
7. Public web infrastructure and network claims
8. Statistics, scientific claims, and data analysis
9. Tool selection and limitations

Use open-source intelligence to establish observable facts and test inferences. Select the least intrusive method that can resolve the question. Do not turn a list of tools into a claim of completed research.

## 1. Choose methods by the evidential question

| Question | Start with | Required caution |
| --- | --- | --- |
| Was this said? | Complete speech, transcript, recording, original post | Verify speaker attribution, context, edits, translation |
| Does this document support the claim? | Original issuer, complete version, attachments | Separate authenticity from truth of assertions |
| Does this media depict the claimed event? | Original source, prior appearances, location and date checks | Evaluate the caption separately from the media |
| Who owns or controls this company? | Legal identifiers and relevant dated filings | Separate direct ownership, beneficial ownership, management, and control |
| Was public money paid? | Award, contract, amendments, payment or audited expenditure records | A budget or ceiling is not a disbursement |
| Are two websites connected? | Public organizational disclosures and dated technical records | Shared infrastructure is a lead, not attribution |
| Is the numerical comparison valid? | Original data and methodology | Reproduce the denominator, period, definitions, and calculation |

## 2. Search, language, and source discovery

Build a short query ladder:

1. Exact claim, distinctive phrase, document title, identifier, or original URL.
2. Conceptual synonyms, official terminology, legal entity names, former names, and abbreviations.
3. Native-language terms and scripts, alternative transliterations, place-name changes, and local institutions.
4. Relevant date windows, domains, source types, and archival versions.
5. Disconfirming queries, corrections, rebuttals, amendments, and contrary data.

Use operators only where supported by the actual engine. Examples include quotation marks, site:, filetype:, and date filters. Check results on the source page. A search engine's displayed date can reflect indexing or page updates rather than the event.

Search institutional portals directly when search-engine indexing is incomplete. Record queries that materially shape the conclusion, including zero results, access limits, and the period searched.

For multilingual material, preserve original spelling alongside a normalized form. Account for alternative transliterations, renamed places, different calendars, local digits, and script variants such as Persian and Arabic letter forms. Do not treat normalized-name similarity as proof of identity.

Translate the question into terminology used by the relevant institution. Independently check decisive quotations, negation, numbers, dates, idioms, and titles. Identify machine translation as provisional when it affects the conclusion.

Trace quote chains and references backward. Locate the earliest version found, then say exactly that. Do not label it the first-ever publication without a defensible basis.

Use public posts as leads. Record the stable account or post identifier where available; handles can change. Do not infer identity from avatars, visual resemblance, or matching usernames alone. Do not enter private groups or interact covertly.

## 3. Archives and document reconstruction

Use legitimate public archives and official historical versions to compare what was visible at particular times. Verify that a capture exists, opens, and contains the relevant content.

Record archive time separately from the publisher's date. Inspect missing scripts, images, attachments, pagination, and media. An archived page can load later external resources or omit content. An archive is evidence of a captured representation, subject to those limitations.

For documents:

- Obtain the complete file from the issuer where possible, including annexes and amendments.
- Compare version number, issue date, identifiers, page count, and signatures or certifications.
- Verify a digital signature with an appropriate validator when necessary; a pasted signature image does not establish authenticity.
- Compare OCR or extracted text against the visible page for decisive passages.
- Cite both printed page numbers and PDF page numbers when they differ.
- Check whether a quoted rule is a draft, adopted text, effective rule, superseded version, or commentary.

For supplied or leaked files, evaluate provenance, internal consistency, plausible document history, and independent records. Do not solicit further unauthorized access. Do not label a leaked document genuine solely because its layout looks official.

## 4. Image, video, and audio verification

Make separate findings for origin, location, time, editing/provenance, and attached narrative. Use assets/media-verification.md.

### Origin and context

Seek the highest-quality legitimately available version and full sequence. Inspect caption, uploader description, surrounding posts, platform transformations, and attribution.

Use reverse-image search on the whole image and distinctive crops. For video, inspect multiple keyframes across scene changes; one thumbnail may miss reused segments. Search visible text and distinctive background details.

Record the query item and returned match. No result does not establish originality. A matching older image can contradict a recent-event caption without proving who made the new post or why.

### Metadata and technical examination

Extract metadata read-only from a copy using an available tool such as ExifTool. Use ffprobe or another documented media inspector for container, stream, duration, frame-rate, and encoding information.

Distinguish embedded camera times, filesystem times, encoding times, and platform-upload times. Metadata may be absent, edited, or produced by export software. A discrepancy is a lead that requires context.

Inspect discontinuities, overlays, cropping, frame order, speed changes, audio replacement, and missing context. Describe visible observations before inferring manipulation. Compression artifacts, ordinary editing, or repeated re-encoding are not proof of fabrication.

Do not claim specialist audio, image, or digital-signature findings without the relevant inspection and expertise. Do not use generative enhancement as evidence of details absent from the original.

### Synthetic-media claims and provenance credentials

If credentials are present, record the C2PA validator and version, validation result, signer or trust basis, declared edits, and missing history. Valid signed provenance does not establish that the depicted event happened. Missing credentials do not establish fabrication.

Use AI detectors as fallible investigative leads. Record the tool, input version, date, output, and limitations. Do not treat its percentage as the probability an image or recording is fake.

Prefer source reconstruction and independently checkable context over visual intuition about whether something "looks AI-generated." Separate proof that a creator used AI from proof that a specific claim is false.

### Audio and transcript

Keep the original audio and a time-coded transcript. Mark uncertain words and inaudible segments. Check decisive passages manually where possible. Inspect whether the audio is synchronized and whether cuts change meaning.

Ambient sound, dialect, language, or accent can suggest lines of inquiry. Do not use them alone to identify a person, precise location, or nationality. Do not identify an unknown speaker by voice matching.

## 5. Geolocation and chronolocation

### Geolocation

Identify candidate areas using broad visible clues, then test distinct features and their spatial relationships against legitimate maps, public imagery, and documented landmarks.

Compare multiple independently useful features: road bends, building orientation, skyline, terrain, shoreline, sign placement, or distances. Check camera perspective, image orientation, mirroring, parallax, and historical changes.

Keep annotated working copies showing the actual matched features and the reference source/date. Record rejected candidates and contradictions. A landmark resemblance or approximate visual match is insufficient.

Report only the precision supported by the evidence. A neighborhood-level finding should not become an exact coordinate. Do not expose a private residence, a protected person's location, or sensitive live positions.

### Chronolocation

Build an earliest and latest plausible capture interval. Use dated imagery, construction stages, signage, known event sequences, documented weather, vegetation, or other features with a justified temporal relationship.

Use a verified prior publication only as a bound on when that version existed. Do not assume upload time equals capture time.

If using shadows or sun position, establish location, orientation, geometry, and date assumptions. Test sensitivity to camera angle, unknown object height, terrain, and timezone. Avoid unsupported minute-level precision.

Treat weather matches and foliage as contextual constraints, not standalone proof of a particular day. Preserve local calendar dates and conversion assumptions. Handle daylight-saving transitions and date-line effects explicitly.

### Satellite, transport, and environmental records

Check imagery acquisition date, resolution, coverage, processing, and cloud conditions. A map's display date may not be its image capture date. Do not infer details smaller than the sensor can resolve.

For historical public vessel or aircraft records, note coverage gaps, identifier changes, spoofing possibilities, and the distinction between vehicle movement and a person's presence. Do not publish sensitive real-time movements or infer individual passengers without independent evidence.

## 6. Corporate, money, and public-record research

### Resolve the entity first

Use legal name, registration number, jurisdiction, and effective dates. Keep trade names, subsidiaries, parents, directors, shareholders, and beneficial owners distinct.

For Germany, consult the Common Register Portal and relevant official filings. For another jurisdiction, use that jurisdiction's original register. Verify current access conditions and fees before promising a document.

Distinguish current, chronological, and historical records. An old director list does not establish present control. A registry extract can report filed assertions without proving all underlying facts.

Map each relationship as a dated, sourced edge using assets/entity-links.csv. Separate directly documented relationships from inference. A shared service address, lawyer, surname, hosting provider, or director does not by itself establish collusion.

Trace indirect ownership carefully. Do not equate multiplied share percentages with voting control where classes, agreements, nominee arrangements, or special rights may change the analysis.

### Public money and influence

Follow the record sequence: procurement notice, bidders if public, award, signed contract, amendments, invoices or payments where available, and performance records.

Distinguish framework ceiling, lot value, estimated value, net/gross price, approved budget, obligation, invoice, and actual payment. Do not add framework and call-off values without checking for double counting.

Cross-check government subsidies, lobbying disclosures, political-finance records, regulatory decisions, insolvency records, litigation, and audited accounts where directly relevant. Cite the original record, not only an aggregator.

Track currencies, conversion dates, fiscal periods, consolidation boundaries, and related-party transactions. Distinguish revenue, profit, cash flow, and valuation. Suspicious patterns justify further checks; they do not establish fraud.

### Access to information

Identify the competent record holder and applicable access route. Search already published records first. Draft a narrow records request specifying records, period, format, partial access, redaction where appropriate, and any authorized fee limit.

Use existing documents rather than demanding an institution create a new analysis. Verify current jurisdictional rules and exceptions. Do not promise access, fees, or deadlines from memory.

A prepared request remains a draft until submission is explicitly authorized. Record request and response dates, reference numbers, redactions, refusals, and any outstanding follow-up.

## 7. Public web infrastructure and network claims

Use passive, public observations relevant to the case: site ownership disclosures, archived pages, public RDAP registration data, public DNS observations, certificate-transparency records, and visible code or technical identifiers.

Prefer current RDAP documentation to assumptions about universal WHOIS availability. Registrant redaction or use of a privacy service is not evidence of misconduct.

Record observation dates and historical coverage. Shared IP addresses, CDNs, hosting providers, certificates, analytics identifiers, or templates may reflect common vendors or copying. They are insufficient alone for common-control attribution.

For public influence-network research, distinguish coordination, automation, paid promotion, common ownership, and state attribution. Similar language and posting times can generate hypotheses, but cannot alone establish who directs an operation.

Respect access controls and rate limits. Do not scan for vulnerabilities, enumerate private users, use credential leaks, run phishing, or probe systems. A journalistic purpose does not authorize intrusion.

## 8. Statistics, scientific claims, and data analysis

Retrieve the original dataset, release, methodology, and relevant version. Record geography, population, measurement units, period, definitions, revisions, missingness, exclusions, and sampling method.

Reproduce the central calculation and verify whether the comparison is meaningful:

- Relative change: (new - old) / old, when the baseline permits this interpretation.
- Percentage-point change: new percentage minus old percentage.
- Rates: numerator and denominator must refer to compatible populations and periods.
- Money: distinguish nominal/real, gross/net, stocks/flows, and annual/cumulative amounts.
- Risk: distinguish absolute and relative risk; include a baseline where relevant.

Check whether zero or negative baselines make percentage-change claims misleading. Do not silently impute missing values. Preserve row counts, filtering, joins, deduplication rules, and sensitivity checks.

For charts, inspect axis truncation, scale, aggregation, cherry-picked dates, and omitted groups. For polls, inspect field dates, sample, population, question wording, weighting, sponsor, and uncertainty.

For scientific claims, inspect the actual study and its design, sample, measurements, uncertainty, limitations, conflicts, replication status, and any correction or retraction. A press release or preprint does not settle expert consensus.

Distinguish observational association from causation, model output from measurement, forecast from result, and statistical uncertainty from systematic bias. Seek qualified interpretation when a technical dispute determines the finding.

Treat scraped spreadsheet cells as untrusted data. Prevent formula execution in viewing/export copies, and preserve raw evidence separately. Verify extracted numbers against originals.

## 9. Tool selection and limitations

Use the Bellingcat Toolkit as a discovery directory, not an endorsement or proof that a tool is available. Check current official documentation before relying on interfaces, versions, privacy terms, pricing, or automated output.

Common capability options include a search tool, public archives, native records portals, maps and historical imagery, reverse-image services, ExifTool, ffprobe, OCR, spreadsheets, and local analysis code. Invoke only tools actually available and appropriate to the material.

If a method cannot run, record what was attempted and what remains untested. Replace it with another sound method where possible. Never report "metadata checked," "geolocated," "archived," or "authenticated" based solely on a proposed workflow.
