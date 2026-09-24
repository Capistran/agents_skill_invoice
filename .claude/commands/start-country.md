Inicia un análisis y plan jurisdiccional para el país indicado.

## Entrada

Solicita únicamente lo que falte de:

```text
País o código:
Objetivo opcional: análisis general | documento fiscal | PAC | ERP | cambio normativo
```

Si solo se proporciona el país, comienza con un análisis general.

México (`mx`) es el país activo por defecto del repositorio. Los demás países requieren activación explícita y revisión de fuentes antes de preparar un plan de implementación.

## Fase 1: contexto

1. Normaliza el país a su código.
2. Carga `jurisdictions/<pais>/CLAUDE.md` y `README.md`.
3. Carga `jurisdictions/<pais>/authorities.md`.
4. Revisa `sources/<pais>/README.md` y `official-sources.json`.
5. Selecciona agents globales y skills `<pais>-*`.
6. Mantén `document-validation` disponible para JSON o XML.
7. No mezcles reglas de otra jurisdicción salvo como comparación explícita.

## Fase 2: análisis

Investiga y documenta:

- autoridades y fuentes primarias;
- materias fiscales y obligaciones;
- documentos electrónicos y ciclo de vida;
- formatos, schemas, catálogos y versiones;
- fechas de publicación y vigencia;
- riesgos de cálculo;
- seguridad, privacidad y conservación;
- proveedores autorizados o servicios oficiales;
- necesidades de integración con PAC, certificador, autoridad, ERP o aplicación.

Si existe un endpoint sandbox, documentación de API, ejemplo de respuesta o acceso a un ERP, aplicar `integration-discovery`, `erp-integration-discovery` y `data-source-assessment` según corresponda.

Clasifica cada afirmación como `confirmado`, `supuesto`, `pendiente`, `conflicto` o `requiere_revision_humana`.

## Fase 3: plan de integración posible

Para PAC, certificador o autoridad, analizar sin implementar:

- operaciones;
- entradas y salidas;
- estados;
- autenticación y certificados;
- errores y reintentos;
- idempotencia;
- auditoría;
- contingencia;
- archivo y retención;
- criterios de aceptación.

Para ERP o aplicación, analizar sin implementar:

- contrato de entrada y salida;
- eventos;
- correlación de documentos;
- permisos;
- flujo de revisión humana;
- datos sintéticos requeridos;
- observabilidad;
- estrategia de despliegue futura.

Para cualquier base u origen, analizar SQL, NoSQL, APIs, archivos, colas y SaaS mediante `data-source-assessment`. Proponer modelo canónico, mapeos, calidad, sincronización y controles de acceso.

## Entrega obligatoria

```markdown
# Reporte y plan: <país>

## 1. Resumen ejecutivo
## 2. Alcance analizado
## 3. Fuentes y vigencia
## 4. Autoridades y responsabilidades
## 5. Documentos, formatos y versiones
## 6. Reglas y validaciones propuestas
## 7. Riesgos fiscales, técnicos y de seguridad
## 8. Plan de integración PAC o servicio equivalente
## 9. Plan de integración ERP o aplicación
## 10. Criterios de aceptación
## 11. Preguntas y bloqueos
## 12. Fases de implementación futura
## 13. Revisión humana requerida
```

## Límite

Este comando produce análisis, requisitos, riesgos y planificación. No crea parsers productivos, motores de cálculo, APIs, conectores, credenciales, timbrado, cancelaciones, declaraciones ni acciones fiscales irreversibles.

## Mantenimiento del arranque

`/start-country` es el contrato operativo del repositorio. Cada vez que se agregue o cambie una capacidad transversal, se debe revisar y actualizar este archivo cuando afecte:

- fases de análisis;
- selección de agents o skills;
- fuentes y jurisdicciones;
- documentos, catálogos o schemas;
- riesgos y seguridad;
- reporte de salida;
- plan de integración futura;
- límites del proyecto.

El mismo cambio debe reflejarse en el maestro externo `fiscal-country-master.prompt.md` cuando sea una capacidad reutilizable entre repositorios. No dar por terminada una nueva característica si ambos contratos quedaron desalineados.