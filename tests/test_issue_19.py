import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_19") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_19.py not implemented")
class Issue19Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_19 import parse_query_string

        self.assertEqual(parse_query_string("a=1&b=hello%20world&a=2"), {"a": "1", "b": "hello world"})
        self.assertEqual(parse_query_string(""), {})
