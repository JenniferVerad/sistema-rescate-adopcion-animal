"""Observer: notificación automática a voluntarios ante nuevos rescates."""
from abc import ABC, abstractmethod


class Observador(ABC):
    @abstractmethod
    def actualizar(self, expediente):
        ...


class Voluntario(Observador):
    def __init__(self, nombre, es_veterinario=False):
        self.nombre = nombre
        self.es_veterinario = es_veterinario
        self.bandeja = []

    def actualizar(self, expediente):
        self.bandeja.append(
            f"Nuevo rescate #{expediente.id_caso}: {expediente.especie} "
            f"'{expediente.nombre}' en {expediente.ubicacion}"
        )


class Sujeto:
    def __init__(self):
        self._observadores = []

    def suscribir(self, obs):
        if obs not in self._observadores:
            self._observadores.append(obs)

    def desuscribir(self, obs):
        self._observadores.remove(obs)

    def notificar(self, expediente):
        for obs in list(self._observadores):
            obs.actualizar(expediente)
