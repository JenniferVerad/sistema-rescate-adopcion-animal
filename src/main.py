from rescate.modelo import Estado
from rescate.mvc import ControladorRescate
from rescate.notificaciones import Voluntario

ctrl = ControladorRescate()
ana, luis = Voluntario("Ana"), Voluntario("Luis", es_veterinario=True)
ctrl.gestor.suscribir(ana)
ctrl.gestor.suscribir(luis)

print(ctrl.reportar("Perro", "Rocky", "Pedernales"))
print(ctrl.reportar("Fauna Silvestre", "Mono aullador", "Cojimíes"))
ctrl.asignar(1, luis)
ctrl.avanzar(1, Estado.EN_TRATAMIENTO)
print(ctrl.reporte())
print(ana.bandeja)
