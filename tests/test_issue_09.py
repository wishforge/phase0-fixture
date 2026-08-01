import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_09") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_09.py not implemented")
class Issue09Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_09 import parse_semver

        self.assertEqual(parse_semver("1.2.3"), (1, 2, 3))
        self.assertEqual(parse_semver("0.0.0"), (0, 0, 0))
        for bad in ("1.2", "a.2.3", "1.2.x"):
            with self.assertRaises(ValueError):
                parse_semver(bad)
