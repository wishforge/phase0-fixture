import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.smoke_probe") is not None


@unittest.skipUnless(_HAVE, "fixturelib/smoke_probe.py not implemented")
class SmokeProbeTests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.smoke_probe import echo

        self.assertEqual(echo("hello"), "hello")  # normal input
        self.assertEqual(echo(""), "")            # empty-string input
