# Sistema de Control de Rescate y Adopción Animal

Diseño de la arquitectura lógica de un sistema para gestionar rescates y adopciones de animales
(perros, gatos y fauna silvestre), aplicando **UML**, **patrones de diseño** y el flujo de trabajo **Gitflow**.

- **Autora:** Jennifer Anahi Vera Centeno
- **Asignatura:** Desarrollo de Sistemas Informáticos – Universidad Técnica de Manabí (UTM Online)
- **Actividad #1:** Estudio de caso – Unidad 1: Desarrollo de software, Introducción y Paradigmas de diseño

## Contenido

| Documento | Descripción |
|---|---|
| [docs/01-analisis-requerimientos.md](docs/01-analisis-requerimientos.md) | Actores, requerimientos funcionales y no funcionales |
| [docs/02-modelado-uml.md](docs/02-modelado-uml.md) | Casos de uso, clases (SOLID), secuencia y estados |
| [docs/03-patrones-diseno.md](docs/03-patrones-diseno.md) | Singleton, Observer, Factory Method y MVC justificados |
| [docs/04-gitflow.md](docs/04-gitflow.md) | Estrategia de ramas utilizada |
| `src/` y `tests/` | Implementación de referencia en Python de los patrones |

## Ejecución

```bash
python3 tests/test_patrones.py     # pruebas unitarias
cd src && python3 main.py          # demostración por consola
```

## Gitflow

Ramas: `main` (producción), `develop` (integración) y `feature/*` (avances). Ver [docs/04-gitflow.md](docs/04-gitflow.md).
