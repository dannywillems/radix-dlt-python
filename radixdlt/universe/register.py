import logging

from radixdlt.universe.universe import AbstractUniverse, Alphanet, Sunstone

LOGGER = logging.getLogger(__file__)


class UniverseRegister:
    _classes = {}

    def register(self, universe):
        assert isinstance(universe, AbstractUniverse)
        LOGGER.debug("Registering universe %s with name %s", universe, universe.NAME)
        self._classes[universe.NAME] = universe

    def get(self, name):
        return self._classes.get(name)

    def get_universes(self):
        return self._classes


REGISTER = UniverseRegister()
REGISTER.register(Alphanet)
REGISTER.register(Sunstone)
