# Alcance activo: México

Fecha de enfoque: 2026-09-23

## Decisión

El proyecto mantiene conocimiento multi-jurisdicción, pero el alcance activo para análisis y planificación de implementaciones es México. Los demás países permanecen como referencia y no deben considerarse listos para una implementación sin una activación explícita y revisión de fuentes primarias.

## Objetivo de implementación futura

Preparar a una fábrica de software para integrar CFDI mexicano con un PAC, ERP o aplicación empresarial, manteniendo separación entre:

- norma fiscal y fuente primaria;
- documento CFDI;
- reglas de validación;
- cálculo y riesgos;
- proveedor PAC;
- aplicación consumidora;
- datos y auditoría;
- revisión fiscal y seguridad.

## Agents activos

| Agent | Entrega para México |
| --- | --- |
| `architect` | arquitectura, límites, contratos y decisiones |
| `tax-domain` | interpretación fiscal y alcance por régimen/documento |
| `source-analyst` | fuentes SAT/DOF/SHCP, vigencia y evidencia |
| `dba-data` | modelo canónico, mapeos, retención e integridad |
| `backend` | diseño de APIs, estados, errores e idempotencia |
| `devops` | sandbox, observabilidad, reintentos y recuperación |
| `devsecops` | secretos, certificados, permisos, privacidad y amenazas |
| `qa` | criterios de aceptación, fixtures y regresión fiscal |
| `compliance-reviewer` | revisión final de hechos, vigencia, impacto y lenguaje |

## Skills activos por fase

### Descubrimiento fiscal

- `mx-cfdi-common`
- `mx-cfdi-document-review`
- `mx-cfdi-rules`
- `mx-cfdi-catalogs`
- `mx-cfdi-xsd`
- `mx-cfdi-calculation-risks`
- `document-validation`

### Documentos CFDI

- `mx-cfdi-factura`
- `mx-cfdi-nota-credito`
- `mx-cfdi-pagos`
- `mx-cfdi-complementos`
- `mx-cfdi-nomina`
- `mx-cfdi-traslado`
- `mx-cfdi-cancelacion`

### Integración futura

- `integration-discovery`
- `erp-integration-discovery`
- `data-source-assessment`
- `mx-pac-integration`
- `mx-cfdi-app-integration`

## Entregable mínimo de una implementación planificada

1. Alcance y tipo de CFDI.
2. Fuentes SAT/DOF y vigencia.
3. Versión, XSD, catálogos y reglas aplicables.
4. Modelo de datos y mapa ERP-origen/destino.
5. Contrato PAC: operaciones, estados, errores, certificados y acuses.
6. Contrato de aplicación: API, eventos, permisos e idempotencia.
7. Riesgos de cálculo, seguridad, privacidad y operación.
8. Fixtures y criterios de aceptación.
9. Plan de sandbox, pruebas, salida gradual y revisión humana.

## Países diferidos

`sv`, `gt`, `pa`, `co`, `br`, `ar`, `pe` y `cl` conservan sus perfiles y skills de análisis, pero quedan fuera del alcance activo hasta que el usuario solicite explícitamente su activación.