import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_17") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_17.py not implemented")
class Issue17Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_17 import run_length_encode

        self.assertEqual(run_length_encode("aaabbc"), "a3b2c1")
        self.assertEqual(run_length_encode(""), "")
        self.assertEqual(run_length_encode("a"), "a1")
