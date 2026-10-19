#!/usr/bin/env python3
"""Local CLI sharing Questlog's lock and atomic writer."""
import argparse
import json
from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1] / "ui"))
import server

def main():
    parser = argparse.ArgumentParser(description=__doc__)
    sub = parser.add_subparsers(dest="command", required=True)
    sub.add_parser("init").add_argument("--git", action="store_true", help="explicitly initialize local ledger history")
    sub.add_parser("show")
    for name in ("capture", "new", "now"):
        sub.add_parser(name).add_argument("text")
    replace = sub.add_parser("replace")
    replace.add_argument("--file", required=True)
    replace.add_argument("--base", required=True)
    args = parser.parse_args()
    if args.command == "init":
        server.initialize()
        if args.git:
            err = server.initialize_git()
            if err:
                parser.error(err)
        print(str(server.LEDGER))
        return
    if not server.LEDGER.exists():
        parser.error("ledger missing; run init first with an explicit QUESTLOG_ROOT")
    if args.command == "show":
        print(json.dumps(server.full_state(), indent=2))
        return
    if args.command == "capture":
        err = server.do_capture(args.text)
    elif args.command == "new":
        err = server.do_new(args.text)
    elif args.command == "now":
        err = server.do_mutate("", "now", args.text)
    else:
        content = Path(args.file).read_text(encoding="utf-8")
        if "\n## NOW\n" not in content or "\n## INBOX\n" not in content:
            parser.error("replacement must preserve NOW and INBOX sections")
        server.REQUEST.base = args.base
        err = server.cas_commit(lambda _: (content, None), "replace ledger")
    if err:
        print(err, file=sys.stderr)
        raise SystemExit(1)
    print(json.dumps({"ok": True, "head": server.full_state()["head"]}))

if __name__ == "__main__":
    main()
