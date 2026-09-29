---
name: mx-cfdi-calculation-risks
description: Identifica factores críticos que pueden alterar cálculos fiscales mexicanos derivados de CFDI y reglas de negocio. Úsalo antes de implementar impuestos, retenciones, saldos, pagos, nómina o conciliaciones.
---

# Riesgos críticos de cálculo fiscal mexicano

## Propósito

Detectar condiciones que pueden cambiar el resultado de un cálculo y hacerlas visibles antes de convertirlas en código o automatización. Este skill es de análisis de riesgos, no sustituye una opinión fiscal ni decide por sí solo la obligación aplicable.

## Factores obligatorios a revisar

### 1. Base y alcance de la operación

- qué operación real respalda el CFDI;
- si el importe es precio, descuento, anticipo, devolución, bonificación, gasto, pago o saldo;
- conceptos gravados, exentos, no objeto o sujetos a tratamiento especial;
- relación entre importe por concepto y total del comprobante;
- si el cálculo corresponde a emisión, recepción, pago, declaración, contabilidad o conciliación.

### 2. Vigencia y contexto fiscal

- fecha de operación, emisión, timbrado, pago y cancelación;
- disposición vigente en cada fecha;
- régimen fiscal, tipo de contribuyente y obligaciones de las partes;
- ámbito federal, estatal o municipal;
- reglas transitorias, facilidades, excepciones y cambios de versión.

### 3. Impuestos, tasas y retenciones

- impuesto aplicable por concepto;
- tasa, cuota, factor o combinación de tasas;
- traslado frente a retención;
- base usada para cada impuesto;
- impuestos incluidos o no incluidos en el precio;
- topes, mínimos, exenciones, estímulos o condiciones sectoriales;
- diferencias entre el impuesto declarado en el XML y el impuesto calculado por la aplicación.

### 4. Precisión, redondeo y moneda

- precisión guardada por concepto, impuesto y total;
- momento y método de redondeo;
- tolerancia autorizada y diferencias acumuladas;
- moneda, tipo de cambio y fecha del tipo de cambio;
- conversión antes o después de calcular el impuesto;
- pagos parciales y diferencias cambiarias.

### 5. Relaciones y estado documental

- UUID, tipo de relación y documento relacionado;
- sustitución, cancelación, aceptación o rechazo;
- nota de crédito, devolución o descuento posterior;
- complemento de pagos y número de parcialidad;
- duplicidad, documentos huérfanos o documentos relacionados más de una vez.

### 6. Datos externos y evidencia

- catálogo oficial y versión usada;
- XSD y versión del documento;
- respuesta de PAC o servicio oficial;
- contrato, orden de compra, comprobante bancario o evidencia logística;
- datos contables, de nómina o de inventario;
- fuente primaria y fecha de consulta.

## Clasificación del resultado

Cada factor debe clasificarse como:

- `confirmed`: respaldado por fuente y datos suficientes;
- `inferred`: derivado, pero requiere confirmar el supuesto;
- `missing`: falta información para calcular;
- `conflict`: existen datos o fuentes contradictorias;
- `requires_human_review`: no debe automatizarse sin decisión fiscal.

## Contrato de un cálculo

Antes de implementar una regla, documentar:

```text
calculation_id:
jurisdiction: MX
operation:
taxes:
inputs:
source_documents:
effective_dates:
assumptions:
precision_and_rounding:
formula_or_rule:
expected_result:
tolerance:
exceptions:
classification:
human_reviewer:
test_cases:
```

## Controles de implementación

- No calcular una tasa o retención solo por leer un atributo del CFDI.
- No reemplazar el importe del XML con el cálculo de la aplicación sin conservar ambos valores.
- Mantener el resultado histórico junto con la versión de reglas que lo produjo.
- Hacer explícitas las diferencias de redondeo y no ocultarlas con tolerancias arbitrarias.
- No reutilizar una regla entre regímenes, periodos o tipos de operación sin validar su alcance.
- Detener el cálculo cuando falten fecha, moneda, base, régimen, catálogo o relación documental relevante.
- Registrar advertencias aunque el total coincida; una coincidencia numérica no prueba el tratamiento fiscal correcto.

## Salida mínima

1. Cálculos observados en el documento.
2. Cálculos reconstruidos por la aplicación, si procede.
3. Diferencias y tolerancias.
4. Factores críticos encontrados.
5. Datos faltantes y supuestos.
6. Reglas que no deben automatizarse todavía.
7. Casos de prueba requeridos.
8. Revisión fiscal necesaria.