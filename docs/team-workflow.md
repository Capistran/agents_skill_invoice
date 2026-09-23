# Trabajo paralelo por roles fiscales

Todos los roles son especialistas fiscales de la jurisdicción activa además de su función técnica. Los agents son globales; el contexto local se carga desde `jurisdictions/<pais>/`, `sources/<pais>/` y los skills `<pais>-*`. La diferencia entre roles está en el tipo de riesgo que controlan, no en si conocen o no el dominio fiscal.

## Selección de contexto

1. Recibir el país o código de jurisdicción.
2. Cargar el `CLAUDE.md` y el perfil de `jurisdictions/<pais>/`.
3. Cargar fuentes y skills con el prefijo correspondiente.
4. Rechazar referencias de otra jurisdicción salvo que se documenten como comparación.

No duplicar agents por país. Crear un agent adicional solo cuando exista una responsabilidad que no pueda expresarse como contexto jurisdiccional, por ejemplo una revisión especializada por ámbito administrativo en Brasil.

## Roles

| Rol | Resultado fiscal principal | Puede bloquear a |
| --- | --- | --- |
| `architect` | diseño, contratos y decisiones | todos |
| `tax-domain` | interpretación fiscal y alcance | backend, compliance |
| `source-analyst` | fuentes y evidencia | tax-domain, dba-data |
| `dba-data` | modelo y persistencia | backend, devops |
| `backend` | diseño de servicios y APIs posibles | qa, devops |
| `devops` | ejecución y operación | release |
| `devsecops` | controles y amenazas | release |
| `qa` | pruebas y criterios de aceptación | release |
| `compliance-reviewer` | aprobación de resultados | comunicación |

## Secuencia recomendada

1. `architect` define el contrato y el alcance.
2. `source-analyst` y `tax-domain` trabajan en paralelo sobre fuentes y criterios fiscales.
3. `dba-data` define persistencia mientras `devsecops` revisa amenazas.
4. `backend` documenta el diseño posible contra contratos aprobados.
5. `qa` y `devops` validan en paralelo pruebas y operación.
6. `compliance-reviewer` revisa el resultado antes de producir acciones para usuarios.

Cada rol debe devolver decisiones, supuestos, archivos modificados y bloqueos. Ningún agente debe presentar una interpretación fiscal como hecho confirmado sin evidencia primaria.