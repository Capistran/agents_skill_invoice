---
name: mx-cfdi-catalogs
description: Lee, normaliza y versiona catálogos oficiales del CFDI mexicano, incluyendo claves, descripciones, restricciones, relaciones y vigencia.
---

# Catálogos CFDI

## Revisar

- nombre oficial, identificador y versión del catálogo;
- código, descripción y estado de cada valor;
- fechas de inicio y fin de vigencia;
- restricciones por régimen, impuesto, entidad, moneda, complemento o tipo de comprobante;
- cambios de descripción, altas, bajas y sustituciones;
- fuente oficial y hash del archivo consultado.

## Reglas de implementación

- No usar descripciones como claves cuando exista un código oficial.
- No sobrescribir valores históricos; conservar versiones por vigencia.
- Diferenciar valor desconocido, valor obsoleto y valor inválido.
- Reportar conflictos entre catálogo, XSD y documentación normativa.
- Probar fechas frontera y valores que cambian de vigencia.