---
name: mx-cfdi-xsd
description: Analiza XSD, namespaces y esquemas oficiales del CFDI mexicano para validar estructura, tipos, cardinalidad y compatibilidad de versiones.
---

# XSD y validación estructural

## Revisar

- namespace raíz y versión;
- imports, includes y dependencias del esquema;
- elementos obligatorios, opcionales y repetibles;
- tipos, restricciones, enumeraciones, patrones y longitudes;
- extensiones de complementos;
- cambios entre versiones y compatibilidad hacia atrás;
- fecha, fuente y hash del XSD.

## Límites

La validación XSD solo prueba estructura y tipos definidos por el esquema. No prueba por sí sola vigencia fiscal, coherencia de negocio, estado de cancelación, pago real, deducibilidad ni acreditamiento.

## Entrega

Generar un inventario de elementos y reglas estructurales, diferencias de versión, errores reproducibles y reglas que deben implementarse fuera del XSD.