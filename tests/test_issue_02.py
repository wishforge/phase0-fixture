import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_02") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_02.py not implemented")
class Issue02Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_02 import parse_csv_line

        self.assertEqual(parse_csv_line("a,b,c"), ["a", "b", "c"])
        self.assertEqual(parse_csv_line('"x,y",z'), ["x,y", "z"])
        self.assertEqual(parse_csv_line('"a""b"'), ['a"b'])
        self.assertEqual(parse_csv_line("a,"), ["a", ""])
