---
name: mx-cfdi-factura
description: Analiza CFDI mexicanos de ingreso o factura, incluyendo conceptos, impuestos, pagos, relaciones y efectos fiscales. Úsalo para facturas de venta, servicios, arrendamiento o anticipos.
---

# CFDI de ingreso y factura

Aplica primero `mx-cfdi-common` y después esta especialización.

## Revisar

- tipo de comprobante de ingreso y versión;
- emisor, receptor, régimen y uso CFDI;
- conceptos, claves, unidad, cantidad, valor unitario, descuento y objeto de impuesto;
- impuestos por concepto y totales globales;
- método de pago, forma de pago, moneda, tipo de cambio y exportación;
- relación con sustituciones, anticipos, devoluciones o notas de crédito;
- complemento presente y su impacto.

## Preguntas fiscales

- ¿La operación está correctamente caracterizada como venta, servicio, arrendamiento, anticipo u otra operación?
- ¿El tratamiento de IVA, retenciones y otros impuestos corresponde a la operación y al régimen de las partes?
- ¿La factura es de pago en una sola exhibición o requiere seguimiento de saldo y complemento de pago?
- ¿Existen condiciones para sustitución, cancelación o relación con otro CFDI?

No determinar deducibilidad o acreditamiento sin revisar operación real, documentación adicional y reglas vigentes.