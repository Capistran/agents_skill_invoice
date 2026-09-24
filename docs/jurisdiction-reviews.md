# Revisión inicial de jurisdicciones

Fecha de revisión: 2026-09-22

Este documento registra una revisión arquitectónica y de alcance, no una validación fiscal definitiva. Los nombres de autoridades, documentos, formatos, proveedores, tasas y obligaciones deben confirmarse con fuentes primarias antes de crear reglas.

## Resultado común

La siguiente capacidad puede reutilizarse como método en todos los países:

- revisión de documentos y fuentes;
- reglas versionadas y auditables;
- catálogos con vigencia;
- validación estructural mediante el esquema oficial disponible;
- factores críticos de cálculo;
- integración con aplicaciones;
- auditoría, seguridad y revisión humana;
- fixtures, casos negativos y pruebas de cambio de versión.

La implementación mexicana no debe copiarse literalmente. Los skills `mx-*` contienen terminología y reglas específicas de México. Los nuevos skills de estos cinco países son esqueletos operativos condicionados a fuentes primarias, no una certificación de cumplimiento.

## Matriz por país

| País | Código | Estado | Documento o sistema a confirmar | Riesgo de reutilización |
| --- | --- | --- | --- | --- |
| México | `mx` | implementado inicialmente | CFDI, SAT, PAC y complementos | Es la base actual, no un modelo universal |
| El Salvador | `sv` | diferido; skills de análisis disponibles | comprobante electrónico, autoridad y proveedor o servicio autorizado | No asumir CFDI, XML, PAC ni campos mexicanos |
| Guatemala | `gt` | diferido; skills de análisis disponibles | FEL, SAT de Guatemala, certificador y documentos aplicables | No asumir que FEL es CFDI con otro nombre |
| Panamá | `pa` | diferido; skills de análisis disponibles | factura electrónica, DGI y modalidades autorizadas | Confirmar formato, ciclo y proveedor antes de nombrar skills |
| Colombia | `co` | diferido; skills de análisis disponibles | DIAN, factura electrónica, documentos equivalentes y proveedor tecnológico | No llamar PAC al proveedor sin evidencia |
| Brasil | `br` | diferido; skills de análisis disponibles | NF-e, NFS-e, CT-e y autoridades federal, estatal y municipal | Requiere portugués técnico y separación por ámbito |
| Argentina | `ar` | diferido; skills de análisis disponibles | comprobantes A/B/C/E/T, CAE, notas y transporte | No asumir que CAE o COT equivalen a modelos mexicanos |
| Perú | `pe` | diferido; skills de análisis disponibles | CPE, UBL 2.1, notas, retenciones, GRE, PSE/OSE | No asumir que CDR, PSE u OSE equivalen a PAC |
| Chile | `cl` | diferido; skills de análisis disponibles | DTE, XML, CAF, notas, guías y exportación | No asumir que CAF o SII equivalen a PAC/CFDI |

## Skills comunes que requieren adaptación

Para cada país se pueden generar, después de confirmar las fuentes:

```text
<pais>-common
<pais>-document-review
<pais>-rules
<pais>-catalogs
<pais>-schemas
<pais>-source-monitoring
<pais>-calculation-risks
<pais>-app-integration
```

Solo crear `<pais>-pac-integration` si existe una figura equivalente confirmada. El nombre debe reflejar la figura local cuando no sea un PAC.

Los documentos específicos deben generarse desde la taxonomía oficial de cada país. No crear automáticamente `factura`, `nota-credito`, `pagos`, `nomina`, `traslado` o `complementos` solo porque existen en México.

## Preguntas mínimas pendientes por país

### El Salvador (`sv`)

- ¿Cuál es la autoridad competente y qué documentos tributarios electrónicos reconoce?
- ¿Existe formato, esquema, catálogo, firma, sello o servicio oficial que deba validarse?
- ¿Existe proveedor, certificador o intermediario autorizado y qué alcance tiene?
- ¿Cómo funcionan emisión, recepción, anulación, sustitución, consulta y contingencia?

### Guatemala (`gt`)

- ¿Cuál es el alcance vigente de FEL y su taxonomía documental?
- ¿Qué autoridad publica normas, especificaciones, catálogos y versiones?
- ¿Qué papel tiene el certificador y qué valida frente a la responsabilidad del contribuyente?
- ¿Qué documentos, relaciones, anulaciones, formatos y esquemas son oficiales?

### Panamá (`pa`)

- ¿Qué autoridad y modalidades de factura electrónica aplican al alcance?
- ¿Qué documentos, formatos, esquemas, catálogos y estados deben soportarse?
- ¿Existe proveedor, certificador, intermediario o servicio estatal autorizado?
- ¿Cuáles son las reglas de emisión, validación, contingencia, anulación y conservación?

### Colombia (`co`)

- ¿Qué documentos y versiones están definidos por la DIAN para el alcance?
- ¿Qué anexos técnicos, XML, esquemas, catálogos, eventos y servicios oficiales aplican?
- ¿Qué responsabilidades y servicios corresponden al proveedor tecnológico?
- ¿Cómo se modelan notas, documentos equivalentes, documentos soporte, nómina y contingencia?

### Brasil (`br`)

- ¿Qué documentos entran en alcance: NF-e, NFS-e, CT-e u otros?
- ¿Qué autoridad corresponde a cada documento y ámbito federal, estadual o municipal?
- ¿Qué formatos, schemas, catálogos, eventos, cancelaciones y contingencias aplican?
- ¿Qué impuestos, bases, retenciones y reglas de cálculo corresponden a mercancías y servicios?
- ¿Qué documentación técnica debe consultarse en portugués?

## Criterio para crear un paquete de país

No se debe pasar de `revisión inicial` a `implementado` hasta contar, como mínimo, con:

1. autoridad y fuentes primarias identificadas;
2. taxonomía documental confirmada;
3. formatos y versiones registrados;
4. catálogo o esquema oficial, si aplica;
5. ciclo de vida y servicio externo documentados;
6. matriz de validaciones adaptativas;
7. riesgos de cálculo y datos faltantes;
8. fixtures y pruebas iniciales;
9. límites de interpretación y revisión humana.