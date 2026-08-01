import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_16") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_16.py not implemented")
class Issue16Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_16 import deep_merge

        a = {"x": 1, "nested": {"a": 1, "b": 2}}
        b = {"y": 2, "nested": {"b": 3, "c": 4}}
        self.assertEqual(deep_merge(a, b), {"x": 1, "y": 2, "nested": {"a": 1, "b": 3, "c": 4}})
        self.assertEqual(a, {"x": 1, "nested": {"a": 1, "b": 2}})
        self.assertEqual(b, {"y": 2, "nested": {"b": 3, "c": 4}})
