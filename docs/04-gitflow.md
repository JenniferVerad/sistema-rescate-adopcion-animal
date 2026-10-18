# 4. Flujo de trabajo Gitflow

| Rama | Rol |
|---|---|
| `main` | Versiones estables (producción). Solo recibe merges desde `develop` (release) |
| `develop` | Integración continua de las funcionalidades |
| `feature/analisis-requerimientos` | Análisis de actores y requerimientos |
| `feature/modelado-uml` | Diagramas de casos de uso, clases, secuencia y estados |
| `feature/patrones-diseno` | Implementación y documentación de los patrones |

Flujo: `develop` → `feature/*` → Pull Request a `develop` → Pull Request de `develop` a `main`.
Convención de commits: `docs:`, `feat:`, `test:`.
