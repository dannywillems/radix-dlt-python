import six


def convert_to_bytes(string):
    if six.PY2:
        return bytes(string)
    else:
        return bytes(string, encoding="utf8")
