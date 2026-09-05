import sqlite3
import tempfile
import unittest
from pathlib import Path

import reconnect as r


def candidate(slug='alex', **kw):
    return dict(url='https://www.linkedin.com/in/' + slug, name=slug,
                source_ids=[slug], eligibility='review', relationship='not_contacted',
                evidence=[{'source': 'fixture:roster'}], **kw)


class LedgerTests(unittest.TestCase):
    def setUp(self):
        self.tmp = tempfile.TemporaryDirectory()
        self.path = Path(self.tmp.name) / 'ledger.sqlite3'
        self.c = r.connect(self.path)

    def tearDown(self):
        self.c.close()
        self.tmp.cleanup()

    def test_reserved_candidates_not_repeated_and_batch_stable(self):
        r.ingest(self.c, [candidate('a'), candidate('b'), candidate('c')])
        a = r.prepare(self.c, 'one', 2)
        b = r.prepare(self.c, 'two', 2)
        self.assertEqual(a, r.prepare(self.c, 'one', 2))
        self.assertEqual(b['count'], 1)
        self.assertFalse({x['url'] for x in a['candidates']} & {x['url'] for x in b['candidates']})
        with self.assertRaises(ValueError):
            r.prepare(self.c, 'one', 3)

    def test_canonical_duplicates_and_blocking_state_win(self):
        a = candidate()
        b = candidate(); b.update(url=a['url'].upper().replace('HTTPS', 'https').replace('WWW.LINKEDIN.COM', 'www.linkedin.com').replace('/IN/', '/in/') + '/?trk=abc',
                                   source_ids=['other-id'], relationship='do_not_contact')
        r.ingest(self.c, [a, b, a])
        self.assertEqual(self.c.execute('SELECT count(*) FROM candidate').fetchone()[0], 1)
        self.assertEqual(r.prepare(self.c, 'one', 2)['count'], 0)

    def test_failed_import_is_atomic(self):
        with self.assertRaises(ValueError):
            r.ingest(self.c, [candidate(), dict(candidate('b'), evidence=[])])
        self.assertEqual(self.c.execute('SELECT count(*) FROM candidate').fetchone()[0], 0)

    def test_uncertain_cannot_release_until_reconciled(self):
        a = candidate(); r.ingest(self.c, [a]); r.prepare(self.c, 'one', 1)
        r.observe(self.c, 'one', a['url'], 'relationship', 'uncertain', 'Submission in progress')
        with self.assertRaises(ValueError):
            r.release(self.c, 'one', a['url'], 'timeout')
        r.observe(self.c, 'one', a['url'], 'relationship', 'requested', 'Pending readback')
        r.release(self.c, 'one', a['url'], 'reconciled')
        self.assertEqual(r.prepare(self.c, 'two', 1)['count'], 0)

    def test_group_does_not_change_relationship(self):
        a = candidate(); r.ingest(self.c, [a]); r.prepare(self.c, 'one', 1)
        r.observe(self.c, 'one', a['url'], 'group', 'joined', 'Group membership readback')
        r.release(self.c, 'one', a['url'], 'complete')
        self.assertEqual(self.c.execute('SELECT relationship FROM candidate').fetchone()[0], 'not_contacted')
        self.assertEqual(r.prepare(self.c, 'two', 1)['count'], 0)

    def test_reserve_exact_list_and_overlap_rollback(self):
        a, b = candidate('a'), candidate('b')
        r.ingest(self.c, [a, b])
        r.prepare(self.c, 'one', 1, [b['url']])
        with self.assertRaises(sqlite3.IntegrityError):
            r.prepare(self.c, 'two', 2, [a['url'], b['url']])
        self.assertIsNone(self.c.execute("SELECT * FROM batch WHERE id='two'").fetchone())
        self.assertEqual(r.prepare(self.c, 'three', 1)['candidates'][0]['url'], a['url'])

    def test_invalid_urls(self):
        for url in ['https://evil.test/in/alex', 'https://www.linkedin.com/company/x',
                    'https://www.linkedin.com/in/x/extra', 'https://user@www.linkedin.com/in/x']:
            with self.assertRaises(ValueError):
                r.canonical(url)

    def test_new_professional_contact_needs_no_roster(self):
        person = candidate('collaborator')
        person.update(source_ids=['public:conference-speaker-1'], eligibility='eligible',
                      evidence=[{'source': 'https://example.org/speakers',
                                 'claim': 'Works on the same professional research topic'}])
        r.ingest(self.c, [person])
        batch = r.prepare(self.c, 'collaborators', 1)
        self.assertEqual(batch['count'], 1)
        self.assertEqual(batch['candidates'][0]['source_ids'], person['source_ids'])



if __name__ == '__main__':
    unittest.main()
