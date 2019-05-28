import binascii
import hashlib
from abc import ABC, abstractmethod

import base58

from radixdlt.crypto.utils import double_sha256


class AbstractAddress(ABC):
    UNIVERSE = None

    def __init__(self, public_key, check_sum):
        self.public_key = public_key
        self.check_sum = check_sum

    @classmethod
    def is_valid(cls, address):
        assert isinstance(address, bytes)
        try:
            decoded_address = base58.b58decode(address)
            double_hashed = binascii.hexlify(double_sha256(decoded_address[:-4]))
            checksum = binascii.hexlify(decoded_address)
            return double_hashed[0:8] == checksum[len(checksum) - 8:]
        except Exception:
            return False

    def from_string(self, address):
        assert isinstance(address, bytes)

