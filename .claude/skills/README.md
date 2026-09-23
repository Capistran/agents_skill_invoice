# Skills por jurisdicción

Los skills fiscales usan el prefijo ISO o código corto de jurisdicción para evitar mezclar reglas entre países.

## México

Los skills actuales usan el prefijo `mx-`:

- `mx-cfdi-*`: CFDI, catálogos, XSD y reglas mexicanas.
- `mx-pac-integration`: integración con PAC para México.

## Futuros países

Cuando se incorpore otra jurisdicción, usar el mismo patrón:

```text
.claude/skills/<pais>-<dominio>/SKILL.md
```

Ejemplos de nombres futuros: `co-facturacion-electronica`, `ar-comprobantes`, `cl-reglas-tributarias`.

Los skills compartidos entre países deben mantenerse separados de los skills jurisdiccionales y no contener tasas, catálogos o reglas locales.

Todos los skills de este repositorio son de análisis y planificación. Pueden proponer reglas, contratos, riesgos, pruebas, fuentes y fases de implementación, pero no construyen software productivo ni automatizan decisiones fiscales.

El comando `/start-country` es el punto de entrada general; `/analyze-cfdi` es el punto de entrada especializado para CFDI.

Skills transversales de integración y datos:

- `integration-discovery`: endpoints sandbox y servicios externos;
- `erp-integration-discovery`: procesos, APIs y datos de ERP;
- `data-source-assessment`: bases SQL, NoSQL, archivos, APIs, colas y SaaS.

`document-validation` es un skill transversal para revisar JSON y XML recibidos en una conversación. Los skills `mx-*`, `co-*`, `br-*`, `gt-*`, `pa-*` y `sv-*` aportan el contexto fiscal local cuando corresponda.

También se incorporan los namespaces `ar-*`, `pe-*` y `cl-*` como alcance de referencia EDICOM: Argentina, Perú y Chile.

## Estado de paquetes iniciales

Se implementaron skills de flujo para `sv`, `gt`, `pa`, `co` y `br`. Estos paquetes contienen descubrimiento, revisión documental, riesgos de cálculo e integración, y solo incluyen taxonomías documentales identificadas durante la revisión inicial.

No deben considerarse paquetes fiscales completos hasta verificar fuentes primarias, vigencias, catálogos, esquemas, reglas y servicios oficiales. El estado detallado está en [docs/jurisdiction-reviews.md](../../docs/jurisdiction-reviews.md).