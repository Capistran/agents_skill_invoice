---
name: mx-cfdi-complementos
description: Analiza complementos fiscales mexicanos dentro de un CFDI y determina su versión, propósito, campos obligatorios, relaciones y evidencia adicional.
---

# Complementos CFDI

Aplica `mx-cfdi-common` y luego identifica el complemento concreto. No tratar todos los complementos como equivalentes.

## Familias a reconocer

- pagos;
- nómina;
- comercio exterior;
- carta porte y transporte;
- recepción de donativos;
- instituciones educativas privadas;
- hidrocarburos y otros complementos sectoriales;
- cualquier complemento cuya existencia y versión se confirme en el catálogo oficial vigente.

## Revisar por complemento

1. Namespace y versión exacta.
2. Autoridad, catálogo o estándar oficial aplicable.
3. Campos obligatorios y condicionales.
4. Catálogos referenciados y valores permitidos.
5. Relación con conceptos, impuestos, partes y documentos relacionados.
6. Evidencia externa requerida.
7. Vigencia de la versión al momento de emisión.

Si el complemento no puede identificarse con seguridad, detener la interpretación y solicitar el XML completo o documentación oficial de la versión.