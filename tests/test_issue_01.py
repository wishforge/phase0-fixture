import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_01") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_01.py not implemented")
class Issue01Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_01 import format_duration

        self.assertEqual(format_duration(0), "0s")
        self.assertEqual(format_duration(59), "59s")
        self.assertEqual(format_duration(125), "2m 05s")
        self.assertEqual(format_duration(3600), "1h 00m 00s")
        self.assertEqual(format_duration(3930), "1h 05m 30s")
