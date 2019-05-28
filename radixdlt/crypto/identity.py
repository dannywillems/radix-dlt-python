import secp256k1


class Identity:
    def __init__(self, private_key):
        assert isinstance(private_key, secp256k1.PrivateKey)
        self.private_key = private_key

    @classmethod
    def generate(cls):
        return cls(private_key=secp256k1.PrivateKey())

    def public_key(self):
        return self.private_key.pubkey
