import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_11") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_11.py not implemented")
class Issue11Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_11 import capitalize_sentences

        self.assertEqual(capitalize_sentences("hello. world! bye"), "Hello. World! Bye")
        self.assertEqual(capitalize_sentences("what? yes. no"), "What? Yes. No")
