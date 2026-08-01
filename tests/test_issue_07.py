import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_07") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_07.py not implemented")
class Issue07Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_07 import chunked

        self.assertEqual(chunked([1, 2, 3, 4, 5], 2), [[1, 2], [3, 4], [5]])
        self.assertEqual(chunked([1, 2, 3], 1), [[1], [2], [3]])
        with self.assertRaises(ValueError):
            chunked([1, 2], 0)
