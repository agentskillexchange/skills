#!/usr/bin/env python3
"""Private offline reservations and evidence. No network or invitation sending."""
import argparse
import json
import math
import os
from pathlib import Path
import re
import sqlite3
from datetime import datetime, timezone
from urllib.parse import urlsplit, unquote


REL = ('not_contacted', 'requested', 'pending', 'connected', 'uncertain', 'withheld', 'do_not_contact')
ELIG = ('eligible', 'review', 'excluded')
GROUP = ('unknown', 'invited', 'joined')


def now():
    return datetime.now(timezone.utc).isoformat()


def canonical(url):
    p = urlsplit(url.strip())
    slug = unquote(p.path).strip('/').split('/')
    if (p.scheme not in ('http', 'https') or p.hostname not in
            ('linkedin.com', 'www.linkedin.com') or p.username or p.password or
            p.port or len(slug) != 2 or slug[0] != 'in' or
            not re.fullmatch(r'[\w%-]+', slug[1])):
        raise ValueError('Expected a LinkedIn /in/ person-profile URL')
    return 'https://www.linkedin.com/in/' + slug[1].lower()


def connect(path):
    path = Path(path).expanduser()
    if not path.parent.is_dir():
        raise ValueError('Create the private project directory first')
    if not path.exists():
        fd = os.open(path, os.O_CREAT | os.O_EXCL | os.O_WRONLY, 0o600)
        os.close(fd)
    c = sqlite3.connect(path)
    c.row_factory = sqlite3.Row
    c.execute('PRAGMA foreign_keys=ON')
    c.executescript('''
      CREATE TABLE IF NOT EXISTS candidate(
        url TEXT PRIMARY KEY, name TEXT NOT NULL, source_ids TEXT NOT NULL,
        eligibility TEXT NOT NULL, relationship TEXT NOT NULL,
        priority REAL NOT NULL, evidence TEXT NOT NULL, group_state TEXT NOT NULL DEFAULT 'unknown');
      CREATE TABLE IF NOT EXISTS batch(
        id TEXT PRIMARY KEY, requested_size INTEGER NOT NULL, created_at TEXT NOT NULL,
        authorization TEXT);
      CREATE TABLE IF NOT EXISTS reservation(
        batch_id TEXT REFERENCES batch(id), url TEXT REFERENCES candidate(url),
        ordinal INTEGER NOT NULL, active INTEGER NOT NULL DEFAULT 1,
        PRIMARY KEY(batch_id,url));
      CREATE UNIQUE INDEX IF NOT EXISTS reserved_once ON reservation(url) WHERE active=1;
      CREATE TABLE IF NOT EXISTS event(
        id INTEGER PRIMARY KEY, at TEXT NOT NULL, batch_id TEXT,
        url TEXT, kind TEXT NOT NULL, value TEXT NOT NULL, evidence TEXT NOT NULL);
    ''')
    return c


def event(c, batch, url, kind, value, evidence):
    c.execute('INSERT INTO event(at,batch_id,url,kind,value,evidence) VALUES(?,?,?,?,?,?)',
              (now(), batch, url, kind, value, evidence))


def merged_list(a, b):
    return list(dict.fromkeys(a + b))


def ingest(c, rows):
    if not isinstance(rows, list):
        raise ValueError('Import must be a JSON array')
    with c:
        for r in rows:
            url = canonical(r['url'])
            rel, elig = r['relationship'], r['eligibility']
            ids, evidence = r['source_ids'], r['evidence']
            if (rel not in REL or elig not in ELIG or not r['name'].strip() or
                    not isinstance(ids, list) or not ids or
                    not all(isinstance(x, str) and x for x in ids) or
                    not isinstance(evidence, list) or not evidence or
                    not all(isinstance(e, dict) and e.get('source') for e in evidence)):
                raise ValueError('Invalid state, identity, or missing evidence source')
            old = c.execute('SELECT * FROM candidate WHERE url=?', (url,)).fetchone()
            priority = float(r.get('priority', 0))
            group = r.get('group_state', 'unknown')
            if not math.isfinite(priority) or group not in GROUP:
                raise ValueError('Finite priority and valid group state required')
            if old:
                rel = max((old['relationship'], rel), key=REL.index)
                elig = max((old['eligibility'], elig), key=ELIG.index)
                ids = merged_list(json.loads(old['source_ids']), ids)
                evidence = json.loads(old['evidence']) + evidence
                priority = max(priority, old['priority'])
                group = max((old['group_state'], group), key=GROUP.index)
            evidence = [json.loads(x) for x in dict.fromkeys(
                json.dumps(e, sort_keys=True) for e in evidence)]
            c.execute('''INSERT INTO candidate(url,name,source_ids,eligibility,relationship,priority,evidence,group_state)
                VALUES(?,?,?,?,?,?,?,?) ON CONFLICT(url) DO UPDATE SET
                name=excluded.name, source_ids=excluded.source_ids, eligibility=excluded.eligibility,
                relationship=excluded.relationship, priority=excluded.priority, evidence=excluded.evidence,
                group_state=excluded.group_state''',
                (url, r['name'], json.dumps(ids), elig, rel, priority, json.dumps(evidence), group))
        event(c, None, None, 'import', str(len(rows)), 'Source candidate refresh')
    return {'imported_rows': len(rows)}


def batch_view(c, name):
    b = c.execute('SELECT * FROM batch WHERE id=?', (name,)).fetchone()
    if b is None:
        raise ValueError('Unknown batch')
    rows = [dict(r) for r in c.execute('''SELECT r.ordinal,r.active,c.* FROM reservation r
        JOIN candidate c USING(url) WHERE batch_id=? ORDER BY ordinal''', (name,))]
    for r in rows:
        for key in ('source_ids', 'evidence'):
            r[key] = json.loads(r[key])
    return {**dict(b), 'count': len(rows), 'candidates': rows}


def prepare(c, name, size, exact_urls=None):
    if size < 1 or not name.strip():
        raise ValueError('Positive size and nonempty batch ID required')
    with c:
        c.execute('BEGIN IMMEDIATE')
        b = c.execute('SELECT * FROM batch WHERE id=?', (name,)).fetchone()
        if b:
            if b['requested_size'] != size:
                raise ValueError('Existing batch size differs; use a new ID')
            if exact_urls is not None:
                existing = [r[0] for r in c.execute('SELECT url FROM reservation WHERE batch_id=? ORDER BY ordinal', (name,))]
                if existing != exact_urls:
                    raise ValueError('Existing batch has different recipients')
        else:
            c.execute('INSERT INTO batch(id,requested_size,created_at) VALUES(?,?,?)', (name, size, now()))
            if exact_urls is not None:
                if len(set(exact_urls)) != size:
                    raise ValueError('Exact batch contains duplicate destinations')
                rows = []
                for url in exact_urls:
                    row = c.execute('SELECT url FROM candidate WHERE url=?', (url,)).fetchone()
                    if row is None:
                        raise ValueError('Import every exact-batch candidate first')
                    rows.append(row)
            else:
                rows = c.execute('''SELECT url FROM candidate c WHERE relationship='not_contacted'
                AND eligibility!='excluded' AND group_state='unknown'
                AND NOT EXISTS(SELECT 1 FROM reservation r WHERE r.url=c.url AND r.active=1)
                    ORDER BY CASE eligibility WHEN 'eligible' THEN 0 ELSE 1 END,
                    priority DESC,name COLLATE NOCASE,url LIMIT ?''', (size,)).fetchall()
            c.executemany('INSERT INTO reservation(batch_id,url,ordinal) VALUES(?,?,?)',
                          [(name, r['url'], i) for i, r in enumerate(rows, 1)])
            event(c, name, None, 'prepare', str(len(rows)), 'Offline reservation; no invitations sent')
    return batch_view(c, name)


def observe(c, batch, url, kind, value, evidence):
    url = canonical(url)
    choices = {'relationship': REL, 'eligibility': ELIG, 'group': GROUP}
    if kind not in choices or value not in choices[kind] or not evidence.strip():
        raise ValueError('Valid observation and nonempty evidence required')
    with c:
        if not c.execute('SELECT 1 FROM reservation WHERE batch_id=? AND url=?', (batch, url)).fetchone():
            raise ValueError('Destination is not in that batch')
        col = {'relationship': 'relationship', 'eligibility': 'eligibility', 'group': 'group_state'}[kind]
        c.execute(f'UPDATE candidate SET {col}=? WHERE url=?', (value, url))
        event(c, batch, url, kind, value, evidence)
    return {'recorded': True, 'url': url, 'kind': kind, 'value': value}


def release(c, batch, url, reason):
    url = canonical(url)
    if not reason.strip():
        raise ValueError('Release reason required')
    with c:
        row = c.execute('''SELECT c.relationship FROM candidate c JOIN reservation r USING(url)
            WHERE r.batch_id=? AND r.url=?''', (batch, url)).fetchone()
        if row is None or row['relationship'] == 'uncertain':
            raise ValueError('Unknown reservation or unresolved attempt; reconcile first')
        c.execute('UPDATE reservation SET active=0 WHERE batch_id=? AND url=?', (batch, url))
        event(c, batch, url, 'release', 'released', reason)
    return {'released': url}


def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument('--db', required=True, help='Private project ledger path')
    sub = p.add_subparsers(dest='command', required=True)
    sub.add_parser('import').add_argument('--input', required=True)
    q = sub.add_parser('prepare'); q.add_argument('--batch', required=True); q.add_argument('--size', type=int, required=True)
    q = sub.add_parser('reserve'); q.add_argument('--batch', required=True); q.add_argument('--input', required=True)
    sub.add_parser('batch').add_argument('--batch', required=True)
    q = sub.add_parser('authorize'); q.add_argument('--batch', required=True); q.add_argument('--reference', required=True)
    q = sub.add_parser('observe')
    for key in ('batch', 'url', 'kind', 'value', 'evidence'):
        q.add_argument('--' + key, required=True)
    q = sub.add_parser('release')
    for key in ('batch', 'url', 'reason'):
        q.add_argument('--' + key, required=True)
    sub.add_parser('status')
    a = p.parse_args()
    c = None
    try:
        c = connect(a.db)
        if a.command == 'import':
            result = ingest(c, json.loads(Path(a.input).read_text()))
        elif a.command == 'prepare':
            result = prepare(c, a.batch, a.size)
        elif a.command == 'reserve':
            urls = json.loads(Path(a.input).read_text())
            if not isinstance(urls, list) or not all(isinstance(u, str) for u in urls):
                raise ValueError('Exact reservation input must be a JSON array of URLs')
            urls = [canonical(u) for u in urls]
            result = prepare(c, a.batch, len(urls), urls)
        elif a.command == 'batch':
            result = batch_view(c, a.batch)
        elif a.command == 'authorize':
            batch_view(c, a.batch)
            if not a.reference.strip():
                raise ValueError('Approval reference cannot be empty')
            with c:
                c.execute('UPDATE batch SET authorization=? WHERE id=?', (a.reference, a.batch))
                event(c, a.batch, None, 'authorization', 'recorded', a.reference)
            result = {'recorded': True, 'batch': a.batch, 'external_actions': 0}
        elif a.command == 'observe':
            result = observe(c, a.batch, a.url, a.kind, a.value, a.evidence)
        elif a.command == 'release':
            result = release(c, a.batch, a.url, a.reason)
        else:
            result = {'relationships': [dict(r) for r in c.execute(
                'SELECT relationship,count(*) AS count FROM candidate GROUP BY relationship')],
                'batches': [dict(r) for r in c.execute('SELECT * FROM batch')],
                'active_reservations': c.execute('SELECT count(*) FROM reservation WHERE active=1').fetchone()[0]}
        print(json.dumps(result, ensure_ascii=False, indent=2))
    except (ValueError, KeyError, TypeError, OSError, sqlite3.Error) as e:
        p.exit(1, f'reconnect: {e}\n')
    finally:
        if c is not None:
            c.close()


if __name__ == '__main__':
    main()
