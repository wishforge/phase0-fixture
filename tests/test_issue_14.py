import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_14") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_14.py not implemented")
class Issue14Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_14 import human_bytes

        self.assertEqual(human_bytes(0), "0 B")
        self.assertEqual(human_bytes(1024), "1 KiB")
        self.assertEqual(human_bytes(1536), "1.5 KiB")
        self.assertEqual(human_bytes(1048576), "1 MiB")
