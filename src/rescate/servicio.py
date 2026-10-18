"""Singleton: motor central de gestión de casos y conexión a datos."""
import threading

from .modelo import Estado, fabrica_para
from .notificaciones import Sujeto


class GestorCasos(Sujeto):
    """Instancia única del motor de gestión de casos (Singleton thread-safe)
    que además actúa como Sujeto del patrón Observer."""

    _instancia = None
    _lock = threading.Lock()

    def __new__(cls):
        if cls._instancia is None:
            with cls._lock:
                if cls._instancia is None:
                    inst = super().__new__(cls)
                    Sujeto.__init__(inst)
                    inst._casos = {}
                    inst._siguiente_id = 1
                    cls._instancia = inst
        return cls._instancia

    @classmethod
    def reiniciar(cls):
        """Solo para pruebas."""
        cls._instancia = None

    def registrar_rescate(self, especie, nombre, ubicacion):
        expediente = fabrica_para(especie).crear_expediente(
            self._siguiente_id, nombre, ubicacion
        )
        self._casos[expediente.id_caso] = expediente
        self._siguiente_id += 1
        self.notificar(expediente)
        return expediente

    def asignar_voluntario(self, id_caso, voluntario):
        self._casos[id_caso].voluntario = voluntario

    def cambiar_estado(self, id_caso, estado: Estado):
        self._casos[id_caso].cambiar_estado(estado)

    def listar(self, estado=None):
        return [c for c in self._casos.values() if estado is None or c.estado == estado]
