from abc import ABC

from radixdlt.core.particle import AbstractParticleType


class AbstractParticleGroup(ABC):
    def __init__(self, particles):
        assert isinstance(particles, list)
        assert all((isinstance(particle, AbstractParticleType) for particle in particles))
        self.particles = particles
