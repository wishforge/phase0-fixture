import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_13") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_13.py not implemented")
class Issue13Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_13 import to_camel_case

        self.assertEqual(to_camel_case("user_id"), "userId")
        self.assertEqual(to_camel_case("already_camel_case"), "alreadyCamelCase")
