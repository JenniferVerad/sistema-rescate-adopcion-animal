"""MVC: Controlador y Vista de consola sobre el modelo/servicio."""
from .modelo import Estado
from .servicio import GestorCasos


class VistaConsola:
    def mostrar_caso(self, e):
        v = e.voluntario.nombre if e.voluntario else "sin asignar"
        return f"[#{e.id_caso}] {e.especie} {e.nombre} | {e.estado.value} | voluntario: {v}"

    def mostrar_lista(self, casos):
        return "\n".join(self.mostrar_caso(c) for c in casos) or "(sin casos)"


class ControladorRescate:
    def __init__(self, vista=None):
        self.gestor = GestorCasos()
        self.vista = vista or VistaConsola()

    def reportar(self, especie, nombre, ubicacion):
        return self.vista.mostrar_caso(self.gestor.registrar_rescate(especie, nombre, ubicacion))

    def asignar(self, id_caso, voluntario):
        self.gestor.asignar_voluntario(id_caso, voluntario)

    def avanzar(self, id_caso, estado: Estado):
        self.gestor.cambiar_estado(id_caso, estado)

    def reporte(self, estado=None):
        return self.vista.mostrar_lista(self.gestor.listar(estado))
