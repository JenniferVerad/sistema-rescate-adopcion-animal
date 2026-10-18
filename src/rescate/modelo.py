"""Modelo: entidades del dominio y Factory Method para expedientes."""
from abc import ABC, abstractmethod
from datetime import date
from enum import Enum


class Estado(Enum):
    RESCATADO = "Rescatado"
    EN_TRATAMIENTO = "En Tratamiento"
    ADOPCION = "Adopción"
    ADOPTADO = "Adoptado"


class Expediente(ABC):
    """Producto abstracto del Factory Method."""

    def __init__(self, id_caso, nombre, ubicacion):
        self.id_caso = id_caso
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.estado = Estado.RESCATADO
        self.fecha_ingreso = date.today()
        self.voluntario = None
        self.historial = [(self.fecha_ingreso, Estado.RESCATADO)]

    @property
    @abstractmethod
    def especie(self):
        ...

    @abstractmethod
    def requisitos_especiales(self):
        ...

    def cambiar_estado(self, nuevo):
        self.estado = nuevo
        self.historial.append((date.today(), nuevo))


class ExpedientePerro(Expediente):
    especie = "Perro"

    def requisitos_especiales(self):
        return ["Vacuna antirrábica", "Desparasitación", "Registro de raza/tamaño"]


class ExpedienteGato(Expediente):
    especie = "Gato"

    def requisitos_especiales(self):
        return ["Vacuna triple felina", "Test FIV/FeLV", "Esterilización"]


class ExpedienteFaunaSilvestre(Expediente):
    especie = "Fauna Silvestre"

    def requisitos_especiales(self):
        return ["Aviso a la autoridad ambiental", "Cuarentena", "Plan de liberación"]


class ExpedienteFactory(ABC):
    """Creador abstracto (Factory Method)."""

    @abstractmethod
    def crear_expediente(self, id_caso, nombre, ubicacion) -> Expediente:
        ...


class PerroFactory(ExpedienteFactory):
    def crear_expediente(self, id_caso, nombre, ubicacion):
        return ExpedientePerro(id_caso, nombre, ubicacion)


class GatoFactory(ExpedienteFactory):
    def crear_expediente(self, id_caso, nombre, ubicacion):
        return ExpedienteGato(id_caso, nombre, ubicacion)


class FaunaSilvestreFactory(ExpedienteFactory):
    def crear_expediente(self, id_caso, nombre, ubicacion):
        return ExpedienteFaunaSilvestre(id_caso, nombre, ubicacion)


FABRICAS = {
    "perro": PerroFactory(),
    "gato": GatoFactory(),
    "fauna silvestre": FaunaSilvestreFactory(),
}


def fabrica_para(especie: str) -> ExpedienteFactory:
    try:
        return FABRICAS[especie.strip().lower()]
    except KeyError:
        raise ValueError(f"Especie no soportada: {especie}")
