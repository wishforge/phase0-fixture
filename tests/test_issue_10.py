import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_10") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_10.py not implemented")
class Issue10Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_10 import dedupe_stable

        self.assertEqual(dedupe_stable([3, 1, 3, 2, 1]), [3, 1, 2])
        self.assertEqual(dedupe_stable([]), [])
