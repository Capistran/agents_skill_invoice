---
name: mx-cfdi-nomina
description: Analiza CFDI de nómina mexicanos y su complemento, separando percepciones, deducciones, otros pagos, subsidios, retenciones y datos sensibles de trabajadores.
---

# CFDI de nómina

Aplica `mx-cfdi-common` y la especialización de nómina solo cuando el complemento esté identificado.

## Revisar

- emisor, receptor trabajador y periodo de pago;
- tipo de nómina, fecha inicial, final y de pago;
- percepciones gravadas y exentas;
- deducciones, retenciones y otros pagos;
- subsidios, incapacidades, horas extra, separación e indemnización cuando correspondan;
- consistencia entre totales del complemento y el CFDI;
- datos personales y reglas de minimización de acceso.

## Reglas

- No exponer RFC, CURP, salario, cuenta o datos personales en reportes innecesarios.
- No concluir retención correcta sin revisar periodo, régimen, tablas y normativa vigente.
- Marcar diferencias para revisión de nómina y fiscal, no corregirlas silenciosamente.