import hmac
import importlib.util
import unittest

_HAVE = importlib.util.find_spec("fixturelib.issue_23") is not None

PAYLOAD = b'{"event":"push","id":23}'
SECRET = "s3cr3t"
KNOWN_SIGNATURE = "7eaaa0f7acc42e17377f61b4265f9d08ad687ab493f0795bff9319bde1bb15f5"
EMPTY_PAYLOAD_SIGNATURE = "3c81cc9496e1c25250f6ccb85f697c1bb623e3480d6538ad8cb6a6648142777d"


@unittest.skipUnless(_HAVE, "fixturelib/issue_23.py not implemented")
class Issue23Tests(unittest.TestCase):
    def test_known_answer(self):
        from fixturelib.issue_23 import verify_webhook

        self.assertIs(verify_webhook(PAYLOAD, KNOWN_SIGNATURE, SECRET), True)
        self.assertIs(
            verify_webhook(PAYLOAD, KNOWN_SIGNATURE.upper(), SECRET), True
        )
        self.assertIs(
            verify_webhook(PAYLOAD, "sha256=" + KNOWN_SIGNATURE, SECRET), True
        )

    def test_round_trip(self):
        from fixturelib.issue_23 import verify_webhook

        signature = hmac.new(b"s3cr3t", PAYLOAD, "sha256").hexdigest()
        self.assertIs(verify_webhook(PAYLOAD, signature, SECRET), True)
        self.assertIs(
            verify_webhook(PAYLOAD, "sha256=" + signature, SECRET), True
        )
        sha512_signature = hmac.new(b"s3cr3t", PAYLOAD, "sha512").hexdigest()
        self.assertIs(
            verify_webhook(
                PAYLOAD, sha512_signature, SECRET, algorithm="sha512"
            ),
            True,
        )

    def test_negative_cases(self):
        from fixturelib.issue_23 import verify_webhook

        tampered = b'{"event":"push","id":24}'
        self.assertIs(verify_webhook(tampered, KNOWN_SIGNATURE, SECRET), False)
        self.assertIs(
            verify_webhook(PAYLOAD, KNOWN_SIGNATURE, "wrong-secret"), False
        )
        self.assertIs(verify_webhook(PAYLOAD, KNOWN_SIGNATURE[:-8], SECRET), False)
        self.assertIs(verify_webhook(PAYLOAD, "0" * 64, SECRET), False)
        self.assertIs(
            verify_webhook(PAYLOAD, "sha512=" + KNOWN_SIGNATURE, SECRET), False
        )

    def test_input_handling(self):
        from fixturelib.issue_23 import verify_webhook

        text_payload = '{"event":"push","id":23}'
        self.assertIs(verify_webhook(text_payload, KNOWN_SIGNATURE, SECRET), True)
        self.assertIs(
            verify_webhook(bytearray(PAYLOAD), KNOWN_SIGNATURE, SECRET), True
        )
        self.assertIs(
            verify_webhook(b"", EMPTY_PAYLOAD_SIGNATURE, SECRET), True
        )
        self.assertIs(
            verify_webhook(b"", EMPTY_PAYLOAD_SIGNATURE, b"s3cr3t"), True
        )

    def test_error_cases(self):
        from fixturelib.issue_23 import verify_webhook

        with self.assertRaises(ValueError):
            verify_webhook(PAYLOAD, KNOWN_SIGNATURE, "")
        with self.assertRaises(ValueError):
            verify_webhook(PAYLOAD, KNOWN_SIGNATURE, b"")
        with self.assertRaises(ValueError):
            verify_webhook(PAYLOAD, KNOWN_SIGNATURE, SECRET, algorithm="md4")
        with self.assertRaises(TypeError):
            verify_webhook(12345, KNOWN_SIGNATURE, SECRET)
        with self.assertRaises(TypeError):
            verify_webhook(None, KNOWN_SIGNATURE, SECRET)
        with self.assertRaises(TypeError):
            verify_webhook(PAYLOAD, 1234, SECRET)


if __name__ == "__main__":
    unittest.main()
