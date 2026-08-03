"""Phase 0 fixture for the end-to-end webhook check.

Provides a single pure function, :func:`verify_webhook`, that verifies a
webhook payload's HMAC signature using only the Python standard library.
The check is fully deterministic and offline-testable: no network access,
no filesystem I/O, no clock reads, and no randomness are involved.
"""

import hashlib
import hmac

__all__ = ["verify_webhook"]


def _to_bytes(value, name):
    """Normalize ``str``/``bytes``/``bytearray`` input to ``bytes``."""
    if isinstance(value, str):
        return value.encode("utf-8")
    if isinstance(value, (bytes, bytearray)):
        return bytes(value)
    raise TypeError(
        "%s must be str, bytes, or bytearray, got %s" % (name, type(value).__name__)
    )


def verify_webhook(payload, signature, secret, *, algorithm="sha256"):
    """Verify an HMAC signature for a webhook payload.

    Args:
        payload: The webhook body as ``str`` (encoded as UTF-8) or
            ``bytes``/``bytearray``.
        signature: Hex digest to verify. May optionally carry an
            ``"<algorithm>="`` prefix (e.g. ``"sha256=ab12..."``); when
            present, the prefix must match ``algorithm``.
        secret: Shared secret as ``str`` (UTF-8) or ``bytes``; must be
            non-empty.
        algorithm: Any member of ``hashlib.algorithms_guaranteed``;
            defaults to ``"sha256"``.

    Returns:
        ``True`` if ``signature`` is a valid HMAC of ``payload`` under
        ``secret`` using ``algorithm``, ``False`` otherwise. Comparison is
        performed in constant time via ``hmac.compare_digest``.

    Raises:
        TypeError: If ``payload``, ``signature``, or ``secret`` is not a
            string or bytes-like value.
        ValueError: If ``secret`` is empty or ``algorithm`` is unsupported.
    """
    if algorithm not in hashlib.algorithms_guaranteed:
        raise ValueError("unsupported algorithm: %r" % (algorithm,))

    payload_bytes = _to_bytes(payload, "payload")
    secret_bytes = _to_bytes(secret, "secret")
    if not secret_bytes:
        raise ValueError("secret must not be empty")
    provided = _to_bytes(signature, "signature").decode("utf-8").lower()

    prefix = algorithm.lower() + "="
    if provided.startswith(prefix):
        provided = provided[len(prefix):]

    expected = hmac.new(secret_bytes, payload_bytes, algorithm).hexdigest()
    return hmac.compare_digest(expected, provided)
