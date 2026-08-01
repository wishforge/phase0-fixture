import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_06") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_06.py not implemented")
class Issue06Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_06 import clamp

        self.assertEqual(clamp(5, 0, 10), 5)
        self.assertEqual(clamp(-1, 0, 10), 0)
        self.assertEqual(clamp(11, 0, 10), 10)
        with self.assertRaises(ValueError):
            clamp(1, 10, 0)
