"""Deterministic webhook signature verification (issue 43 / e2e webhook check).

Exposes a single pure helper, :func:`verify_webhook_signature`, which checks
an HMAC digest of a payload against a supplied signature hex string. The
implementation uses only the standard library, performs no I/O or network
access, uses no randomness, and always returns the same result for the same
inputs.
"""

import hashlib
import hmac

__all__ = ["verify_webhook_signature"]

_SUPPORTED_ALGORITHMS = {
    "sha1": hashlib.sha1,
    "sha256": hashlib.sha256,
    "sha512": hashlib.sha512,
}


def verify_webhook_signature(
    payload: bytes,
    secret: str,
    signature_hex: str,
    *,
    algorithm: str = "sha256",
) -> bool:
    """Return ``True`` when ``signature_hex`` matches the HMAC of ``payload``.

    The comparison is constant-time (``hmac.compare_digest``). The candidate
    signature is normalized before comparison: surrounding whitespace is
    stripped, an optional ``"<algorithm>="`` prefix is accepted, and
    upper-case hex digits are lower-cased. Malformed candidates (invalid hex,
    wrong length, empty) simply return ``False`` instead of raising.

    Raises:
        TypeError: if ``payload`` is not ``bytes`` or ``secret`` /
            ``signature_hex`` is not ``str``.
        ValueError: if ``secret`` is empty or ``algorithm`` is unsupported.
    """
    if not isinstance(payload, bytes):
        raise TypeError("payload must be bytes")
    if not isinstance(secret, str):
        raise TypeError("secret must be str")
    if not isinstance(signature_hex, str):
        raise TypeError("signature_hex must be str")
    if not secret:
        raise ValueError("secret must not be empty")

    digestmod = _SUPPORTED_ALGORITHMS.get(algorithm)
    if digestmod is None:
        raise ValueError(
            "unsupported algorithm %r; expected one of %s"
            % (algorithm, sorted(_SUPPORTED_ALGORITHMS))
        )

    candidate = signature_hex.strip().lower()
    prefix = "%s=" % algorithm
    if candidate.startswith(prefix):
        candidate = candidate[len(prefix):]

    expected = hmac.new(secret.encode("utf-8"), payload, digestmod).hexdigest()
    if len(candidate) != len(expected):
        return False
    try:
        bytes.fromhex(candidate)
    except ValueError:
        return False
    return hmac.compare_digest(expected, candidate)
