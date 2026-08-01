import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_20") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_20.py not implemented")
class Issue20Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_20 import to_roman

        self.assertEqual(to_roman(1), "I")
        self.assertEqual(to_roman(1994), "MCMXCIV")
        self.assertEqual(to_roman(2026), "MMXXVI")
        for bad in (0, 4000, -1):
            with self.assertRaises(ValueError):
                to_roman(bad)
