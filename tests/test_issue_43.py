import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_43") is not None


@unittest.skipUnless(_HAVE, "fixturelib/issue_43.py not implemented")
class Issue43Tests(unittest.TestCase):
    def test_cases(self):
        from fixturelib.issue_43 import verify_webhook_signature

        payload = b"what do ya want for nothing?"
        secret = "Jefe"
        # RFC 4231 test case 2, HMAC-SHA-256.
        sha256_hex = (
            "5bdcc146bf60754e6a042426089575c7"
            "5a003f089d2739839dec58b964ec3843"
        )
        # RFC 2202 test case 2, HMAC-SHA-1.
        sha1_hex = "effcdf6ae5eb2fa2d27416d5f184df9c259a7c79"

        self.assertTrue(verify_webhook_signature(payload, secret, sha256_hex))
        self.assertTrue(
            verify_webhook_signature(payload, secret, "sha256=" + sha256_hex)
        )
        self.assertTrue(
            verify_webhook_signature(payload, secret, sha256_hex.upper())
        )
        self.assertTrue(
            verify_webhook_signature(
                payload, secret, "sha1=" + sha1_hex.upper(), algorithm="sha1"
            )
        )
        # Deterministic: repeated calls agree.
        self.assertEqual(
            verify_webhook_signature(payload, secret, sha256_hex),
            verify_webhook_signature(payload, secret, sha256_hex),
        )

        self.assertFalse(
            verify_webhook_signature(b"tampered payload", secret, sha256_hex)
        )
        self.assertFalse(
            verify_webhook_signature(payload, "wrong-secret", sha256_hex)
        )
        self.assertFalse(
            verify_webhook_signature(payload, secret, sha256_hex[:-2])
        )
        self.assertFalse(verify_webhook_signature(payload, secret, "zz" * 32))
        self.assertFalse(verify_webhook_signature(payload, secret, ""))
        self.assertFalse(verify_webhook_signature(payload, secret, "   "))
        self.assertFalse(
            verify_webhook_signature(payload, secret, "sha1=" + sha1_hex)
        )

        with self.assertRaises(ValueError):
            verify_webhook_signature(payload, "", sha256_hex)
        with self.assertRaises(ValueError):
            verify_webhook_signature(payload, secret, sha256_hex, algorithm="md5")
        with self.assertRaises(TypeError):
            verify_webhook_signature("not-bytes", secret, sha256_hex)
        with self.assertRaises(TypeError):
            verify_webhook_signature(payload, b"Jefe", sha256_hex)


if __name__ == "__main__":
    unittest.main()
