import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_18") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_18.py not implemented")
class Issue18Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_18 import most_common_words

        self.assertEqual(most_common_words("a b a c a b", 2), [("a", 3), ("b", 2)])
        self.assertEqual(most_common_words("x y", 5), [("x", 1), ("y", 1)])
