import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_05") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_05.py not implemented")
class Issue05Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_05 import word_count

        self.assertEqual(word_count("Hello, world! hello"), {"hello": 2, "world": 1})
        self.assertEqual(word_count(""), {})
