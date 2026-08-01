import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_12") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_12.py not implemented")
class Issue12Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_12 import find_first_duplicate

        self.assertEqual(find_first_duplicate([1, 2, 3, 2, 1]), 2)
        self.assertIsNone(find_first_duplicate([1, 2, 3]))
        self.assertIsNone(find_first_duplicate([]))
