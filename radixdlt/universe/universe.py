from abc import ABC

import requests

from radixdlt.universe import alphanet_raw, sunstone_raw


class AbstractUniverse(ABC):
    NAME = None
    RAW_DATA = None
    NODE_FINDER = None

    def get_description(self):
        return self.RAW_DATA["description"]

    def get_name(self):
        return self.RAW_DATA["name"]

    def get_magic(self):
        return self.RAW_DATA["magic"]

    def get_big_bang_timestamp(self):
        return self.RAW_DATA["timestamp"]

    def get_port(self):
        return self.RAW_DATA["port"]

    def get_node_using_finder(self):
        return requests.get("%s:%d" % (self.NODE_FINDER[0], self.NODE_FINDER[1]))


class Alphanet(AbstractUniverse):
    NAME = "alphanet"
    RAW_DATA = alphanet_raw.RAW
    NODE_FINDER = alphanet_raw.NODE_FINDER


class Sunstone(AbstractUniverse):
    NAME = "sunstone"
    RAW_DATA = sunstone_raw.RAW
    NODE_FINDER = sunstone_raw.NODE_FINDER
