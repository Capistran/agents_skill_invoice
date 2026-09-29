---
name: mx-cfdi-pagos
description: Analiza CFDI de recepción de pagos y complementos de pago mexicanos, incluyendo parcialidades, saldos, documentos relacionados, impuestos y diferencias cambiarias.
---

# CFDI de pago

Aplica `mx-cfdi-common` antes de este análisis.

## Revisar

- tipo de comprobante de pago y versión del complemento;
- fecha, forma de pago, moneda y tipo de cambio;
- documentos relacionados y UUID de cada factura;
- número de parcialidad, saldo anterior, importe pagado y saldo insoluto;
- impuestos trasladados y retenidos asociados al pago;
- pagos en moneda distinta, operaciones bancarias y diferencias;
- consistencia entre el pago recibido y las facturas relacionadas.

## Resultado específico

Generar una conciliación por UUID y parcialidad, marcar saldos imposibles o duplicados y distinguir datos del XML de confirmaciones bancarias o contables externas. No concluir que una factura está pagada sin evidencia suficiente.