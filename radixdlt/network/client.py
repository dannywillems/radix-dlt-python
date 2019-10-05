from abc import ABCMeta
import six

from radixdlt.universe.universe import Sunstone, Alphanet

# https://docs.radixdlt.com/node-api/rest
# https://docs.radixdlt.com/node-api/json-rpc


# FIXME: https://docs.radixdlt.com/node-api/#rate-limits Rate limits!
class AbstractClient(six.with_metaclass(ABCMeta)):
    UNIVERSE = None

    def __init__(self, client_ip):
        self.client_ip = client_ip
        self.client_port = self.UNIVERSE.get_port()


class AlphanetClient(AbstractClient):
    UNIVERSE = Alphanet


class SunstoneClient(AbstractClient):
    UNIVERSE = Sunstone
