/* Browser-only, privacy-first CSV structure inspection. No network, storage, or payment. */
(function (root) {
  "use strict";
  const MAX_BYTES = 32 * 1024;

  function parseCsv(source) {
    const input = String(source).replace(/^\uFEFF/, "");
    if (!input.trim()) throw new Error("Paste a CSV with a header row first.");
    const rows = [];
    let row = [], field = "", quoted = false, justClosed = false, dirty = false;
    function endField() {
      row.push(field);
      field = "";
      justClosed = false;
      dirty = false;
    }
    function endRow() {
      endField();
      rows.push(row);
      row = [];
    }
    for (let i = 0; i < input.length; i++) {
      const ch = input[i];
      if (quoted) {
        if (ch === '"') {
          if (input[i + 1] === '"') { field += '"'; i++; }
          else { quoted = false; justClosed = true; }
        } else {
          field += ch;
        }
      } else if (ch === "," || ch === "\r" || ch === "\n") {
        if (ch === "\r" && input[i + 1] === "\n") i++;
        if (ch === ",") endField();
        else endRow();
      } else if (ch === '"') {
        if (dirty || justClosed) throw new Error("Unexpected quote in an unquoted cell.");
        quoted = true;
        dirty = true;
      } else if (justClosed) {
        throw new Error("Unexpected text after a closing CSV quote.");
      } else {
        field += ch;
        dirty = true;
      }
    }
    if (quoted) throw new Error("Unclosed quoted CSV field.");
    if (row.length || field !== "" || justClosed || dirty || !rows.length) endRow();
    return rows;
  }

  function inspectCsv(input) {
    const source = String(input ?? "");
    const bytes = typeof TextEncoder !== "undefined"
      ? new TextEncoder().encode(source).length
      : Buffer.byteLength(source, "utf8");
    if (bytes > MAX_BYTES) return {ok: false, error: "CSV exceeds the 32 KB free local preview limit.", bytes};
    let rows;
    try { rows = parseCsv(source); }
    catch (error) { return {ok: false, error: error.message, bytes}; }
    const headers = rows[0];
    const body = rows.slice(1);
    const distinctHeaders = new Set();
    let duplicateHeaders = 0, blankHeaders = 0;
    for (const header of headers) {
      const normalized = header.trim().toLowerCase();
      if (!normalized) blankHeaders++;
      if (distinctHeaders.has(normalized)) duplicateHeaders++;
      distinctHeaders.add(normalized);
    }
    let raggedRows = 0, missingCells = 0, duplicateRows = 0, formulaWarnings = 0;
    const fingerprints = new Set();
    for (const row of body) {
      if (row.length !== headers.length) raggedRows++;
      missingCells += row.filter(v => !v.trim()).length;
      if (row.length < headers.length) missingCells += headers.length - row.length;
      const fingerprint = JSON.stringify(row);
      if (fingerprints.has(fingerprint)) duplicateRows++;
      fingerprints.add(fingerprint);
      for (const value of row) {
        const trim = value.trimStart();
        if (/^[=+@]/.test(trim) || /^-(?!\d+(?:[.,]\d+)?$)/.test(trim)) formulaWarnings++;
      }
    }
    return {
      ok: true, bytes, columns: headers.length, dataRows: body.length,
      duplicateHeaders, blankHeaders, raggedRows, missingCells,
      duplicateRows, formulaWarnings,
      caveat: "Heuristic structure checks only, not semantic verification or security certification."
    };
  }

  if (typeof module !== "undefined" && module.exports) module.exports = {parseCsv, inspectCsv, MAX_BYTES};

  const doc = root.document;
  if (!doc) return;
  const input = doc.getElementById("csv-preview-input");
  const result = doc.getElementById("csv-preview-results");
  const file = doc.getElementById("csv-preview-file");
  if (!input || !result) return;

  function show(message, state) {
    result.replaceChildren();
    const para = doc.createElement("p");
    para.textContent = message;
    result.appendChild(para);
    result.dataset.state = state;
  }
  doc.getElementById("csv-preview-check").addEventListener("click", function () {
    const report = inspectCsv(input.value);
    if (!report.ok) return show(report.error, "error");
    const pairs = [
      ["Data rows", report.dataRows],
      ["Columns", report.columns],
      ["Uneven-length rows", report.raggedRows],
      ["Missing cells", report.missingCells],
      ["Duplicate rows", report.duplicateRows],
      ["Duplicate header names", report.duplicateHeaders],
      ["Blank header names", report.blankHeaders],
      ["Potential spreadsheet-formula cells", report.formulaWarnings]
    ];
    const summary = doc.createElement("p");
    summary.textContent = `Checked ${report.bytes} bytes locally. This is a heuristic preview, not a certified audit.`;
    const dl = doc.createElement("dl");
    dl.className = "csv-preview-stats";
    for (const [label, count] of pairs) {
      const dt = doc.createElement("dt");
      const dd = doc.createElement("dd");
      dt.textContent = label;
      dd.textContent = String(count);
      dl.append(dt, dd);
    }
    result.replaceChildren(summary, dl);
    result.dataset.state = "checked";
  });
  doc.getElementById("csv-preview-demo").addEventListener("click", function () {
    input.value = 'id,name,amount\n1,Ada,15\n2,,20\n2,,20\n3,"=HYPERLINK(""https://example.invalid"", ""not safe"")",45\n4,Bob\n';
    file.value = "";
    input.focus();
    show("Fictional sample loaded. Select “Check locally”.", "demo");
  });
  doc.getElementById("csv-preview-clear").addEventListener("click", function () {
    input.value = "";
    file.value = "";
    show("CSV cleared from this form. Nothing was uploaded.", "empty");
    input.focus();
  });
  file.addEventListener("change", async function () {
    const chosen = file.files && file.files[0];
    if (!chosen) return;
    if (chosen.size > MAX_BYTES) {
      file.value = "";
      return show("File exceeds 32 KB. Select a smaller non-confidential CSV.", "error");
    }
    try {
      const content = await chosen.text();
      if (typeof TextEncoder !== "undefined" && new TextEncoder().encode(content).length > MAX_BYTES) {
        return show("Decoded content exceeds 32 KB.", "error");
      }
      input.value = content;
      show("CSV read locally from your device; select “Check locally” to inspect its structure.", "ready");
    } catch (_) {
      show("Could not read the selected file locally.", "error");
    }
    file.value = "";
  });
})(typeof window !== "undefined" ? window : globalThis);
