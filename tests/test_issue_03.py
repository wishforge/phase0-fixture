import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_03") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_03.py not implemented")
class Issue03Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_03 import is_palindrome

        self.assertIs(is_palindrome("Racecar!"), True)
        self.assertIs(is_palindrome("A man, a plan, a canal: Panama"), True)
        self.assertIs(is_palindrome("hello"), False)
