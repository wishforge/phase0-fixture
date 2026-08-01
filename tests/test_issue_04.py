import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_04") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_04.py not implemented")
class Issue04Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_04 import flatten

        self.assertEqual(flatten([1, [2, [3, 4]], 5]), [1, 2, 3, 4, 5])
        self.assertEqual(flatten([]), [])
        self.assertEqual(flatten([[1], 2, [3, [4]]]), [1, 2, 3, 4])
