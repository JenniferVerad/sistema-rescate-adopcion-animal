# 1. Análisis del problema

## 1.1 Escenario
Un refugio animal necesita un sistema para **reportar ingresos de animales rescatados** (perros, gatos y fauna
silvestre), **asignar voluntarios o veterinarios** encargados y **gestionar los estados del proceso**
(Rescatado → En Tratamiento → Adopción → Adoptado).

## 1.2 Actores

| Actor | Descripción | Interacciones principales |
|---|---|---|
| Ciudadano / Reportante | Persona que encuentra un animal y lo reporta | Reportar rescate, consultar el estado de su caso |
| Voluntario | Persona que atiende y da seguimiento al caso | Recibir notificaciones, actualizar estado, consultar casos |
| Veterinario | Profesional que evalúa y trata al animal | Registrar tratamiento, actualizar estado médico |
| Administrador del Refugio | Responsable de la operación | Asignar voluntarios, gestionar adopciones, generar reportes |

## 1.3 Requerimientos funcionales

| ID | Requerimiento |
|---|---|
| RF-01 | Crear un caso de rescate con especie, nombre/descripción y ubicación |
| RF-02 | Categorizar automáticamente la especie (perro, gato, fauna silvestre) y generar su expediente específico |
| RF-03 | Asignar un voluntario o veterinario a un caso |
| RF-04 | Cambiar y registrar el historial de estados (Rescatado, En Tratamiento, Adopción, Adoptado) |
| RF-05 | Notificar automáticamente a los voluntarios cuando ingresa un nuevo rescate |
| RF-06 | Registrar tratamientos veterinarios y requisitos especiales por especie |
| RF-07 | Gestionar el proceso de adopción de un animal |
| RF-08 | Consultar y filtrar casos por estado |
| RF-09 | Generar reportes para el administrador |

## 1.4 Requerimientos no funcionales

| ID | Requerimiento | Cómo se atiende |
|---|---|---|
| RNF-01 | Escalabilidad: soportar nuevas especies y nuevos canales de notificación | Factory Method y Observer (abiertos a extensión) |
| RNF-02 | Mantenibilidad: bajo acoplamiento y alta cohesión | MVC, principios SOLID |
| RNF-03 | Trazabilidad de versiones del diseño y del código | Gitflow en GitHub |
| RNF-04 | Consistencia de datos: una sola fuente de verdad | Singleton del gestor de casos |
| RNF-05 | Usabilidad: interfaz clara para ciudadanos y voluntarios | Vista desacoplada del modelo (MVC) |
| RNF-06 | Seguridad: roles diferenciados por actor | Separación de responsabilidades por actor |
