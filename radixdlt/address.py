import binascii
import hashlib
from abc import ABC, abstractmethod
import secp256k1
import base58

from radixdlt.crypto.utils import double_sha256


class InvalidAddressError(Exception):
    pass


class AbstractAddress(ABC):
    UNIVERSE = None

    def __init__(self, public_key):
        assert isinstance(public_key, secp256k1.PublicKey)
        self.public_key = public_key

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

    @classmethod
    def from_string(cls, address):
        assert isinstance(address, bytes)
        if not cls.is_valid(address=address):
            raise InvalidAddressError()
        decoded_address = base58.b58decode(address)
        public_key = decoded_address[:-5]
        public_key = secp256k1.PublicKey(public_key)
        return cls(public_key=public_key)
