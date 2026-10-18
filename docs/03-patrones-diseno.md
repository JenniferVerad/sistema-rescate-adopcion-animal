# 3. Patrones de diseño aplicados

| # | Patrón | Tipo | Clases | Archivo |
|---|---|---|---|---|
| 1 | Singleton | Creacional | `GestorCasos` | `src/rescate/servicio.py` |
| 2 | Factory Method | Creacional | `ExpedienteFactory` y fábricas concretas | `src/rescate/modelo.py` |
| 3 | Observer | Comportamiento | `Sujeto`, `Observador`, `Voluntario` | `src/rescate/notificaciones.py` |
| 4 | MVC | Arquitectónico / Estructural | `ControladorRescate`, `VistaConsola`, `GestorCasos` | `src/rescate/mvc.py` |

## Singleton — instancia central del motor de gestión de casos
**Propósito:** garantizar una única instancia con acceso global.
**Problema que resuelve:** si hubiera varios gestores, cada uno tendría su propia lista de casos y la numeración de expedientes
se duplicaría. **Justificación técnica:** `GestorCasos` es la única fuente de verdad y punto de acceso a datos (RNF-04);
se implementa thread-safe con *double-checked locking*.

## Factory Method — expedientes según la especie
**Propósito:** delegar a subclases la creación del objeto concreto.
**Problema que resuelve:** cada especie requiere un expediente distinto (vacunas y trámites diferentes). Sin el patrón,
`registrar_rescate` tendría una cadena de `if/elif` que habría que modificar por cada especie nueva.
**Justificación técnica:** cumple Abierto/Cerrado (RNF-01); agregar «Aves» implica una subclase y una fábrica.

## Observer — notificación automática a voluntarios
**Propósito:** que varios objetos reaccionen automáticamente a un cambio de otro.
**Problema que resuelve:** al ingresar un rescate, todos los voluntarios suscritos deben enterarse sin que el gestor conozca
quiénes son ni cómo se les avisa. **Justificación técnica:** bajo acoplamiento; se pueden añadir observadores
(correo, SMS, panel) sin tocar `GestorCasos` (RF-05, RNF-01).

## MVC — organización de lógica de negocio e interfaz
**Propósito:** separar modelo, vista y controlador.
**Problema que resuelve:** evitar que la presentación se mezcle con las reglas de negocio.
**Justificación técnica:** `VistaConsola` puede reemplazarse por una web/móvil sin cambiar el modelo (RNF-02, RNF-05).

## Cómo interactúan los patrones
Ver diagrama de secuencia en `02-modelado-uml.md`: el **Controlador** (MVC) invoca al **Singleton**; este usa la
**Factory Method** para crear el expediente y notifica por **Observer** a los voluntarios.
