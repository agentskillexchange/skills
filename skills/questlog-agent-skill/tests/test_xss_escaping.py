#!/usr/bin/env python3
"""Synthetic XSS regression checks. Requires Node for escaper behavior tests."""

import io
import json
import os
import re
import shutil
import subprocess
import unittest
from html.parser import HTMLParser

UI = os.path.join(os.path.dirname(os.path.dirname(os.path.abspath(__file__))), "ui")
FILES = ["bar.html", "index.html", "quickadd.html"]

ESCAPERS = ("esc(", "esc2(", "escAttr(", "escAttr2(")

# Interpolations that carry no markup. Each entry needs a reason, not just a pattern.
SAFE_EXPR = [
    # --- arithmetic and counts: cannot contain '<' ---
    (r"^Math\.", "arithmetic"),
    (r"\.length\b", "array length, an integer"),
    (r"^i$|^idx$|^n$(?![\w(])", "loop counter"),
    (r"^\d+$", "literal number"),
    (r"days_waiting|overdue_by|chase_days|depth\b", "parser-produced integers"),
    # --- composites already escaped where they were built ---
    (r"^(meta|wmeta|dmeta|notes|journal|tags|dues|badge|label|st|tip|key)$",
     "composite assembled from already-escaped parts, or itself escaped at construction"),
    # `cls` was in the list above with that same justification. It was FALSE — cls is
    # d.kind, not a composite. A verifier forced a payload through it and built a live
    # onmouseover. Removed rather than re-justified: the site is now escaped. This is
    # what the maintenance note at the top of this file is warning about.
    # NOTE: there are deliberately NO entries here for "starts with a paren" or "is a
    # ternary". Earlier versions had `^\(` and `^\w[\w.]*\s*(&&|\?)`, and a verifier
    # demonstrated the consequence:
    #
    #     ${w.goal}           -> caught      ${(w.goal||"")}      -> MISSED
    #     ${w.goal||""}       -> caught      ${w.goal?w.goal:""}  -> MISSED
    #                                        ${w.goal&&w.goal}    -> MISSED
    #
    # i.e. one pair of parentheses away from the sink that had been live an hour
    # earlier, and the suite stayed green. Those patterns allowlisted a SYNTACTIC
    # SHAPE rather than a set of values, on the assumption that such expressions are
    # plumbing — when they may carry data. Ternaries and parens are now RESOLVED by
    # _is_safe() instead, which recurses into the branches that actually get emitted.
    (r"^glow$", "const glow = overdue(w)?' glow':'' — a ternary of two static strings"),
    (r"^acts$", "composite built in this file from static markup plus escAttr'd data-subj"),
    (r"^dueBadge\(", "returns markup built only from d.date (pinned to a date by DUE_RE) "
                     "and d.kind (an enum); its title attribute is escAttr'd at the sink"),
    (r"^r\.(grp|ic|t|sub|tag)$", "quickadd row fields: grp and ic are literals set in this "
                                 "file, t and sub are composites already esc()'d where they "
                                 "are built, tag is the state enum"),
    # --- values pinned by a server-side regex. NOTE: this safety is a property of
    #     WS_RE / DUE_RE in ui/server.py, i.e. of a different file. Escaped at the
    #     sink anyway wherever practical; listed here for the sites where the value
    #     is used as a CSS class name and escaping would change the class. ---
    (r"^w\.state$|^w\.domain$|^d\.kind$", "enum pinned by WS_RE/DUE_RE in server.py"),
    (r"^slug$|^w\.slug$", "slug pinned to [a-z0-9][a-z0-9._-]* by WS_RE in server.py"),
    # --- template plumbing, not data ---
    (r"^t\.done|^t\.depth", "boolean/int from the subtask parser"),
    (r"^f\.(label|key)$", "static filter definition in this file"),
    (r"^(STATE|SEARCH|s)\.[\w.]*\.length", "count"),
    (r"^cron$|^s\.unpushed$", "server-side integer"),
]

INTERP = re.compile(r"\$\{([^{}]*(?:\{[^{}]*\}[^{}]*)*)\}")


def _script_of(path):
    src = io.open(path, encoding="utf-8").read()
    blocks = re.findall(r"<script>(.*?)</script>", src, re.S)
    if not blocks:
        return ""
    return max(blocks, key=len)


def _template_literals(js):
    """Backtick-delimited strings. Crude but sufficient: the UI builds all its markup
    with template literals, and a false positive here costs one allowlist entry while
    a false negative costs an XSS."""
    return re.findall(r"`([^`]*)`", js, re.S)


# A single-quoted literal may contain double quotes and vice versa — which is exactly
# how static markup is written here, e.g. '<span class="k">↵</span>'. An earlier
# version excluded BOTH quote characters from the body and so failed to recognise its
# own UI's literals as literals.
STRING_LIT = re.compile(r"""^(?:'(?:[^'\\]|\\.)*'|"(?:[^"\\]|\\.)*")$""")
NUMERIC = re.compile(r"^[\d\s.+*/()%-]+$")


def _split_top(expr, ops):
    """Split on an operator at paren/quote depth zero. Returns None if absent."""
    depth = 0
    quote = None
    i = 0
    while i < len(expr):
        c = expr[i]
        if quote:
            if c == "\\":
                i += 2
                continue
            if c == quote:
                quote = None
        elif c in "'\"`":
            quote = c
        elif c in "([{":
            depth += 1
        elif c in ")]}":
            depth -= 1
        elif depth == 0:
            for op in ops:
                if expr.startswith(op, i):
                    return expr[:i], op, expr[i + len(op):]
        i += 1
    return None


def _is_safe(expr, depth=0):
    """Resolve what the expression EMITS, rather than pattern-matching its prefix.

    An earlier version allowlisted anything beginning with '(' and anything shaped
    like a ternary. That allowlisted a syntactic shape rather than a set of values,
    and `${(w.goal||'')}` — one paren away from a sink that was live — passed.
    """
    e = expr.strip()
    if depth > 6:
        return False                      # pathological nesting: refuse, do not assume
    if any(x in e for x in ESCAPERS):
        return True
    if STRING_LIT.match(e) or NUMERIC.match(e) or e == "":
        return True

    # (X) -> whatever X emits
    if e.startswith("(") and e.endswith(")") and _split_top(e[1:-1], (")",)) is None:
        return _is_safe(e[1:-1], depth + 1)

    # cond ? A : B -> the CONDITION is never emitted; A and B are.
    tern = _split_top(e, ("?",))
    if tern:
        _cond, _, rest = tern
        arms = _split_top(rest, (":",))
        if arms:
            return _is_safe(arms[0], depth + 1) and _is_safe(arms[2], depth + 1)

    # A && B -> only B is emitted when truthy.  A || B -> either may be emitted.
    andor = _split_top(e, ("&&",))
    if andor:
        return _is_safe(andor[2], depth + 1)
    orop = _split_top(e, ("||",))
    if orop:
        return _is_safe(orop[0], depth + 1) and _is_safe(orop[2], depth + 1)

    for pat, _reason in SAFE_EXPR:
        if re.search(pat, e):
            return True
    return False


class NoRawInterpolation(unittest.TestCase):
    """Every interpolation into markup is escaped or explicitly allowlisted."""

    def test_every_interpolation_is_escaped_or_allowlisted(self):
        problems = []
        for name in FILES:
            path = os.path.join(UI, name)
            if not os.path.exists(path):
                continue
            js = _script_of(path)
            self.assertTrue(js, f"{name}: no <script> block found — parser assumption broke")
            for lit in _template_literals(js):
                if "<" not in lit:          # not markup; a URL or a plain message
                    continue
                for expr in INTERP.findall(lit):
                    if not _is_safe(expr):
                        problems.append(f"{name}: unescaped ${{{expr.strip()[:90]}}}")
        self.assertEqual([], problems, "\n  " + "\n  ".join(problems) if problems else "")

    def test_the_escapers_are_defined_in_each_file_that_uses_them(self):
        for name in FILES:
            path = os.path.join(UI, name)
            if not os.path.exists(path):
                continue
            js = _script_of(path)
            for fn in ("esc", "esc2", "escAttr", "escAttr2"):
                if re.search(r"[^\w]" + fn + r"\(", js) and fn + "(" not in "".join(ESCAPERS[:0]):
                    defined = re.search(r"(function\s+%s\s*\(|const\s+%s\s*=)" % (fn, fn), js)
                    if re.search(r"[^\w.]%s\(" % fn, js):
                        self.assertTrue(defined, f"{name}: uses {fn}() but never defines it")

    # REMOVED: test_attribute_escapers_escape_both_quote_styles.
    #
    # It asserted that an escaper's SOURCE contained the literal "&quot;" and "&#39;".
    # A verifier showed it was inverted in BOTH directions:
    #
    #     a CORRECT escaper spelling the entity &#34;   -> the test said RED
    #     a BROKEN escaper with &quot; in a dead branch -> the test said GREEN
    #
    # &#34; and &quot; are the same character. It never checked that a quote gets
    # neutralised; it checked that someone spelled the entity as its author expected.
    # So it failed correct code and passed an attribute-breakout hole. A first attempt
    # to repair it — resolving one level of delegation, since escAttr2 hands the double
    # quote to esc2 — removed the symptom and left the cause: it still grepped a
    # literal. Superseded by EscaperBehaviour, which executes the escapers.
    #
    # Deleted rather than skipped. It was left skipped for one commit, and a verifier
    # pointed out that by this file's own standard — a green run must mean something
    # ran — a test that can never run is worse than no test, since it inflates the
    # count while asserting nothing. The lesson lives here instead.

def _node():
    for c in ("node", "/opt/homebrew/bin/node", "/usr/local/bin/node"):
        if shutil.which(c) or os.path.exists(c):
            return shutil.which(c) or c
    return None


def _run_escaper(js_src, fn, payloads):
    """Execute an escaper for real and return its outputs.

    Everything else in this file is a syntactic check, which is the right shape for
    "is an escaper called at this sink". Whether an escaper actually neutralises a
    quote is a BEHAVIOURAL property, and the only honest way to test it is to run it.
    """
    node = _node()
    if node is None:
        raise unittest.SkipTest("node not available")
    # Evaluate the REAL page script, then call the real escaper out of it. The page's
    # top level touches document/window, so it runs against a Proxy global that
    # absorbs any property access or call and returns itself.
    #
    # Two earlier attempts sliced the function out with a regex instead. Both failed,
    # and instructively: one terminated at the ';' inside '&amp;' (HTML entities end
    # in semicolons), and the escapers contain regex literals like /[&<>"]/g whose
    # quote characters defeat a naive string tracker. Writing a JS parser to test a JS
    # function is the wrong trade — node already has one.
    stub = (
        "const sink = new Proxy(function(){}, {get:()=>sink, apply:()=>sink, "
        "set:()=>true, has:()=>true});\n"
        "globalThis.document = sink; globalThis.window = globalThis;\n"
        "globalThis.location = {href:'', search:''};\n"
        "globalThis.addEventListener = ()=>{}; globalThis.setInterval = ()=>0;\n"
        "globalThis.setTimeout = ()=>0; globalThis.requestAnimationFrame = ()=>0;\n"
        "globalThis.fetch = ()=>Promise.resolve({ok:true, json:()=>({}), text:()=>''});\n"
        "globalThis.EventSource = function(){ return sink; };\n"
    )
    # No try-wrapper: `const` declarations inside a block are block-scoped and
    # would not be visible to the invocation appended below. The stub is good enough
    # that the page scripts evaluate cleanly at top level (verified).
    prog = (stub + js_src + "\n" +
            "const out = %s.map(p => %s(p));\n" % (json.dumps(payloads), fn) +
            "process.stdout.write(JSON.stringify(out));\n")
    r = subprocess.run([node, "-e", prog], capture_output=True, text=True, timeout=30)
    if r.returncode != 0:
        raise AssertionError(f"{fn} failed to execute: {r.stderr.strip()[:300]}")
    return json.loads(r.stdout)


class _AttrSpy(HTMLParser):
    """Parse the rendered fragment and record what the parser actually built."""

    def __init__(self):
        super().__init__(convert_charrefs=True)
        self.tags = []
        self.attrs = []

    def handle_starttag(self, tag, attrs):
        self.tags.append(tag)
        self.attrs.extend(a for a, _v in attrs)

    def attr_value(self, name):
        return None


class EscaperBehaviour(unittest.TestCase):
    """Run the escapers and parse their output. Replaces a spelling check that was
    inverted in both directions — it failed a correct escaper that spelled the entity
    `&#34;` and passed a broken one that merely contained `&quot;` in a dead branch.

    node is required. If it is missing this FAILS rather than skipping, for the same
    reason the API suite now fails without a server: a green run must mean something
    ran.
    """

    DQ = 'a" onmouseover="alert(1)'
    SQ = "a' onfocus='alert(1)"
    TAG = "<img src=x onerror=alert(1)>"

    def setUp(self):
        self.assertIsNotNone(_node(), "node is required to execute the escapers; "
                                      "a spelling check is not an acceptable substitute")
        self.bar = _script_of(os.path.join(UI, "bar.html"))
        self.idx = _script_of(os.path.join(UI, "index.html"))

    def _defs(self, js, *names):
        """Whole-script source; the escapers are top-level so defining the script and
        calling one of its functions is enough. Cheaper and far more robust than
        slicing a definition out with a regex — an earlier attempt did that and
        terminated at the ';' inside '&amp;'."""
        return js

    def _assert_neutralised(self, js, fn, payload, quote, fname):
        out = _run_escaper(self._defs(js, fn), fn, [payload])[0]
        # Behavioural assertion: embed the result in an attribute of that quote style
        # and confirm the PARSER built no extra attribute. This is the property that
        # matters, and it is independent of which entity spelling was used.
        frag = f"<button data-x={quote}{out}{quote}>t</button>"
        spy = _AttrSpy()
        spy.feed(frag)
        self.assertEqual(["button"], spy.tags, f"{fname}: {fn} let a tag through: {frag[:120]}")
        self.assertEqual(["data-x"], spy.attrs,
                         f"{fname}: {fn}({payload!r}) broke out of a {quote}-quoted "
                         f"attribute — parser built {spy.attrs}")

    # Which escapers can be tested behaviourally, and why not all of them:
    #
    #   esc2, escAttr, escAttr2  are PURE string functions -> executed below.
    #   esc (index.html)         is the DOM idiom: createElement / textContent /
    #                            innerHTML. It has no behaviour without a document,
    #                            and shimming one would only test the shim's
    #                            serialisation rules — spelling again, one remove
    #                            further out. Its invariant is enforced statically
    #                            instead, by test_esc_is_never_used_in_an_attribute,
    #                            which is the property that actually matters for it:
    #                            esc does NOT escape quotes, by design.

    PURE = (("bar.html", "esc2"), ("bar.html", "escAttr2"), ("index.html", "escAttr"))

    def _js(self, fname):
        return self.bar if fname == "bar.html" else self.idx

    def test_attribute_escapers_neutralise_double_quotes(self):
        self._assert_neutralised(self.bar, "escAttr2", self.DQ, '"', "bar.html")
        self._assert_neutralised(self.idx, "escAttr", self.DQ, '"', "index.html")

    def test_attribute_escapers_neutralise_single_quotes(self):
        self._assert_neutralised(self.bar, "escAttr2", self.SQ, "'", "bar.html")
        self._assert_neutralised(self.idx, "escAttr", self.SQ, "'", "index.html")

    def test_content_escaper_neutralises_tags(self):
        out = _run_escaper(self.bar, "esc2", [self.TAG])[0]
        spy = _AttrSpy()
        spy.feed(f"<div>{out}</div>")
        self.assertEqual(["div"], spy.tags,
                         f"bar.html: esc2 let an element through — parser built {spy.tags}")

    def test_escapers_do_not_corrupt_ordinary_text(self):
        """Round-trip fidelity. Over-escaping is a real bug too: data-subj and data-t
        are read back and POSTed, so a doubled entity would corrupt the ledger."""
        plain = 'Tom & Jerry <3 100% "quoted" it\'s'
        for fname, fn in self.PURE:
            out = _run_escaper(self._js(fname), fn, [plain])[0]
            self.assertNotIn("&amp;amp;", out, f"{fname}: {fn} double-escaped")

    def test_esc_is_never_used_in_an_attribute(self):
        """esc() is the textContent idiom and does NOT escape quotes — correct for
        element content, a live hole inside an attribute. This is the invariant that
        matters for it, and it is checkable statically where its behaviour is not.
        """
        bad = []
        for name in ("index.html", "quickadd.html"):
            path = os.path.join(UI, name)
            if not os.path.exists(path):
                continue
            for lit in _template_literals(_script_of(path)):
                # any ${...} sitting inside a quoted attribute value
                for m in re.finditer(r"""=\s*(["'])([^"']*?\$\{[^}]*\}[^"']*?)\1""", lit):
                    expr = m.group(2)
                    if re.search(r"[^\w.]esc\(", expr) or expr.strip().startswith("${esc("):
                        bad.append(f"{name}: esc() inside an attribute -> {m.group(0)[:80]}")
        self.assertEqual([], bad, "\n  " + "\n  ".join(bad) if bad else "")

    def test_a_deliberately_broken_escaper_is_CAUGHT(self):
        """Prove this suite can fail. The old spelling check passed this exact shape:
        it contains the literal '&quot;' but never applies it to the input."""
        broken = ("function escBroken(x){ if (false) { return String(x)"
                  ".replace(/\"/g,'&quot;').replace(/'/g,'&#39;'); } return String(x); }")
        out = _run_escaper(broken, "escBroken", [self.DQ])[0]
        spy = _AttrSpy()
        spy.feed(f'<button data-x="{out}">t</button>')
        self.assertIn("onmouseover", spy.attrs,
                      "the canary escaper should have broken out — if it did not, this "
                      "test can no longer detect a broken escaper")


class KnownSinksStayEscaped(unittest.TestCase):
    """Named regressions. Each of these was live at some point; a rename or refactor
    that drops the escaper here must fail loudly rather than quietly."""

    def setUp(self):
        self.bar = _script_of(os.path.join(UI, "bar.html"))
        self.idx = _script_of(os.path.join(UI, "index.html"))

    def test_open_detail_panel_sinks(self):
        # Seven sinks; six had JavaScript executed through them in a live browser.
        for frag in ("esc2(x.who)", "esc2(x.what)", "esc2(d.what)", "esc2(n)", "esc2(l)"):
            self.assertIn(frag, self.bar, f"openDetail sink regressed: {frag}")
        self.assertGreaterEqual(self.bar.count("esc2(w.goal"), 2, "goal escaped on both card and panel")
        self.assertGreaterEqual(self.bar.count("esc2(w.next"), 2, "next escaped on both card and panel")

    def test_queue_renderers(self):
        self.assertIn("esc2(a.text)", self.bar)
        self.assertIn("esc2(a.result)", self.bar)
        self.assertIn("esc2(a.slug)", self.bar)

    def test_index_data_subj_uses_the_attribute_escaper(self):
        # The exploitable one: key contains the parser's unconstrained `who` field.
        self.assertIn("escAttr(key)", self.idx,
                      "data-subj must use the ATTRIBUTE escaper — esc() does not "
                      "escape quotes and would not close the breakout")
        self.assertNotIn('data-subj="${key}"', self.idx)


if __name__ == "__main__":
    unittest.main(verbosity=2)
