import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_08") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_08.py not implemented")
class Issue08Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_08 import slugify

        self.assertEqual(slugify("Hello, World!"), "hello-world")
        self.assertEqual(slugify("a--b c"), "a-b-c")
        self.assertEqual(slugify("  spaced  out  "), "spaced-out")
