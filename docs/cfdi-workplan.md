# Plan inicial de análisis y planificación CFDI

## Objetivo

Definir un análisis trazable para CFDI mexicanos que clasifique el documento, identifique datos verificables, detecte inconsistencias y prepare requisitos o un plan para una posible implementación posterior.

## Skills iniciales

| Skill | Alcance | Prioridad |
| --- | --- | --- |
| `mx-cfdi-common` | lectura, identificación y controles comunes | P0 |
| `mx-cfdi-factura` | ingreso y factura | P0 |
| `mx-cfdi-nota-credito` | egreso y ajustes | P0 |
| `mx-cfdi-pagos` | recepción de pagos y conciliación | P0 |
| `mx-cfdi-complementos` | clasificación de complementos | P0 |
| `mx-cfdi-cancelacion` | estados y sustitución | P1 |
| `mx-cfdi-nomina` | nómina y datos sensibles | P1 |
| `mx-cfdi-traslado` | traslado, transporte y comercio exterior | P1 |
| `mx-cfdi-document-review` | documentos, comunicados y cambios normativos | P0 |
| `mx-cfdi-rules` | reglas versionadas y testeables | P0 |
| `mx-cfdi-calculation-risks` | factores críticos de cálculos y reglas de negocio | P0 |
| `mx-cfdi-catalogs` | catálogos y vigencias | P0 |
| `mx-cfdi-xsd` | esquemas y validación estructural | P0 |
| `mx-pac-integration` | timbrado, consulta y cancelación con PAC | P1 |
| `mx-cfdi-app-integration` | integración con ERP, contabilidad o facturación | P1 |

## Tareas de análisis y planificación

1. Definir el modelo neutral propuesto para CFDI, conceptos, impuestos, relaciones y complementos.
2. Especificar el parser XML, namespaces y validación estructural requeridos.
3. Diseñar fixtures anonimizados por tipo de CFDI y versión soportada.
4. Definir casos de prueba para documentos válidos, incompletos, duplicados y maliciosos.
5. Inventariar catálogos y reglas versionadas con fecha de vigencia y fuente oficial.
6. Especificar la consulta de estado de cancelación y la evidencia que debería conservarse.
7. Diseñar reportes de diferencias entre XML, complementos y datos contables externos.
8. Pasar cada conclusión por revisión fiscal antes de recomendar una automatización.
9. Documentar reglas, catálogos o esquemas propuestos, sin implementarlos.
10. Evaluar opciones de PAC, ambientes, idempotencia, auditoría y manejo de errores.
11. Definir el contrato de integración con una aplicación consumidora y una política de aprobación humana.
12. Aplicar `mx-cfdi-calculation-risks` antes de recomendar cualquier cálculo, tasa, retención, saldo o conciliación.

Ninguna tarea de este plan autoriza por sí misma la implementación de código productivo.

## Criterio de terminado

Un análisis no está terminado si solo parsea XML. Debe indicar versión, tipo, UUID, fecha de consulta, fuente normativa, campos faltantes, riesgos, nivel de confianza y revisión requerida.