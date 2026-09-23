---
name: mx-cfdi-rules
description: Convierte disposiciones fiscales y especificaciones oficiales mexicanas en reglas versionadas, auditables y testeables para validar CFDI.
---

# Reglas fiscales implementables

## Tipos de regla

- estructural: presencia, formato, tipo y cardinalidad;
- catálogo: valor permitido y vigencia;
- relación: consistencia entre nodos, UUID o documentos;
- aritmética: sumas, redondeos, impuestos y totales;
- temporal: fechas de emisión, pago, vigencia y plazos;
- contextual: régimen, operación, complemento o tipo de contribuyente;
- servicio: validación externa realizada por SAT o PAC.

## Contrato de una regla

Cada regla debe registrar:

- `rule_id` estable;
- descripción fiscal en español;
- condición de aplicación;
- entrada y salida esperada;
- severidad: error, advertencia o revisión;
- fuente primaria;
- fecha de vigencia y fecha de consulta;
- versión de CFDI, XSD o catálogo;
- casos positivos, negativos y casos límite;
- responsable de revisión.

No convertir una explicación ambigua en una regla automática. Marcarla como `requires_human_review` hasta resolverla.