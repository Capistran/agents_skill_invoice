---
name: mx-cfdi-nota-credito
description: Analiza CFDI mexicanos de egreso y notas de crédito, devoluciones, descuentos, bonificaciones y correcciones relacionadas con facturas.
---

# CFDI de egreso y nota de crédito

Aplica `mx-cfdi-common` antes de este análisis.

## Revisar

- tipo de comprobante de egreso;
- CFDI relacionado, tipo de relación y UUID;
- motivo económico y documental: devolución, descuento, bonificación, ajuste o corrección;
- conceptos, cantidades, impuestos y total de la nota;
- periodo de la operación original y periodo del ajuste;
- correspondencia entre la nota y la factura original;
- cancelaciones, sustituciones y documentos duplicados.

## Resultado específico

Explicar qué documento modifica, por qué importe, qué impuestos potencialmente ajusta, qué evidencia respalda el ajuste y qué validación humana falta. No asumir que una nota de crédito es válida solo porque contiene un UUID relacionado.