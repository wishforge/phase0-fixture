import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_15") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_15.py not implemented")
class Issue15Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_15 import is_valid_email

        self.assertIs(is_valid_email("a@b.co"), True)
        self.assertIs(is_valid_email("a@b"), False)
        self.assertIs(is_valid_email("a b@c.co"), False)
        self.assertIs(is_valid_email("@b.co"), False)
