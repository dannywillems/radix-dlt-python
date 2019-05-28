from abc import ABC, abstractmethod

from radixdlt.core.particle_group import AbstractParticleGroup
from radixdlt.crypto.signature import AbstractSignature
from radixdlt.universe.universe import Sunstone, Alphanet


class AbstractAtom(ABC):
    UNIVERSE = None

    def __init__(self, timestamp, particle_groups, metadata, signatures):
        assert self.UNIVERSE is not None, "Define in which universe the atom lives in"
        # FIXME: what's the size of the timestamp? Milliseconds? Microseconds? Nanoseconds?
        assert isinstance(int, timestamp)
        assert timestamp > self.UNIVERSE.get_big_bang_timestamp()
        self.timestamp = timestamp
        assert isinstance(particle_groups, list)
        assert all((isinstance(particle_group, AbstractParticleGroup) for particle_group in particle_groups))
        self.particle_groups = particle_groups
        self.metadata = metadata
        assert isinstance(signatures, list)
        assert all((isinstance(signature, AbstractSignature) for signature in signatures))
        self.signatures = signatures

    @abstractmethod
    def verify(self):
        pass


class AlphanetAtom(AbstractAtom):
    UNIVERSE = Alphanet


class SunstoneAtom(AbstractAtom):
    UNIVERSE = Sunstone
