import hashlib


def double_sha256(bytestr):
    return hashlib.sha256(hashlib.sha256(bytestr).digest()).digest()
