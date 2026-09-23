# Arquitectura inicial

## Capas de análisis

1. **Fuentes**: referencias oficiales, fecha de consulta, vigencia y tipo de documento.
2. **Conocimiento jurisdiccional**: conceptos, obligaciones, autoridades y particularidades de cada país.
3. **Reglas de análisis**: criterios para detectar impacto, cambios y preguntas pendientes.
4. **Agentes**: flujos especializados que investigan, comparan, explican y preparan planes.
5. **Revisión humana**: aprobación de conclusiones antes de considerar una implementación futura.

## Flujo de un cambio normativo

```text
Fuente oficial
    -> ficha de fuente
    -> extracción de cambios
    -> clasificación por jurisdicción e impuesto
    -> análisis de impacto
    -> revisión humana
    -> plan de implementación posible
```

## Contrato mínimo de una conclusión

Toda conclusión debe incluir:

- jurisdicción;
- impuesto o materia;
- fecha de publicación y fecha de vigencia, cuando existan;
- hecho normativo observado;
- impacto potencial;
- supuestos y límites;
- fuente primaria con URL o identificador;
- nivel de confianza;
- revisión requerida.

## Límite actual

El repositorio no implementa parsers productivos, motores de cálculo, APIs, integraciones con PAC/ERP ni automatizaciones fiscales. Puede describirlos mediante contratos, requisitos, riesgos, criterios de aceptación y un plan por fases.

## Posible implementación futura

Una decisión separada podría autorizar posteriormente ingestión de fuentes, almacenamiento estructurado, pruebas de regresión normativa e integraciones. Esa decisión debe incluir alcance, responsables, fuentes verificadas, seguridad, revisión fiscal y criterios de salida.

## Producto multiusuario previsto

La plataforma futura puede ofrecer experiencias distintas sobre el mismo conocimiento: desarrollador, contador, dirección y pequeño negocio. El plan gratuito debe limitarse a análisis con fuentes públicas y datos sintéticos o anonimizados; PAC, ERP, presentación de declaraciones y acciones irreversibles requieren un alcance separado.