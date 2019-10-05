import binascii
from abc import ABCMeta

import secp256k1
import base58
import six

from radixdlt.crypto.utils import double_sha256
from radixdlt.utils.compat import convert_to_bytes, unicode


class InvalidAddressError(Exception):
    pass


class AbstractAddress(six.with_metaclass(ABCMeta)):
    UNIVERSE = None

    def __init__(self, public_key):
        assert self.UNIVERSE is not None
        assert isinstance(public_key, secp256k1.PublicKey)
        self.public_key = public_key

    @classmethod
    def _convert_to_bytes(cls, address):
        if isinstance(address, str) or isinstance(address, unicode):
            address = convert_to_bytes(address)
            return address
        elif isinstance(address, bytes):
            return address
        else:
            raise InvalidAddressError("The address must be given as a 'str', a 'unicode' or a 'bytes' type, %s "
                                      "given" % type(address))

    @classmethod
    def is_valid(cls, address):
        try:
            address = cls._convert_to_bytes(address)
            decoded_address = base58.b58decode(address)
            double_hashed = binascii.hexlify(double_sha256(decoded_address[:-4]))
            checksum = binascii.hexlify(decoded_address)
            return double_hashed[0:8] == checksum[len(checksum) - 8:]
        except Exception:
            return False

    @classmethod
    def from_string(cls, address):
        try:
            address = cls._convert_to_bytes(address)
            if not cls.is_valid(address=address):
                raise InvalidAddressError()
            decoded_address = base58.b58decode(address)
            public_key = decoded_address[:-5]
            public_key = secp256k1.PublicKey(public_key)
            return cls(public_key=public_key)
        except Exception:
            raise InvalidAddressError
