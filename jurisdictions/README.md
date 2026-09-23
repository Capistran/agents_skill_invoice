# Jurisdicciones

Cada jurisdicción debe tener su propio directorio y reglas locales. No mezclar conceptos, tasas o calendarios entre países sin una capa explícita de normalización.

Los skills de Claude Code siguen además un namespace por país en `.claude/skills/`, por ejemplo `mx-cfdi-factura`. El directorio de jurisdicción contiene conocimiento y documentación; el skill contiene el flujo reutilizable que lo aplica.

Formato previsto:

```text
jurisdictions/<codigo>/
├── CLAUDE.md
├── README.md
├── authorities.md
├── taxes/
└── workflows/
```

## Jurisdicciones disponibles

- `mx`: México, conocimiento inicial de CFDI.
- `sv`: El Salvador, perfil de análisis inicial.
- `gt`: Guatemala, perfil de análisis FEL.
- `pa`: Panamá, perfil de análisis de factura electrónica.
- `co`: Colombia, perfil de análisis DIAN.
- `br`: Brasil, perfil de análisis por documento y ámbito.
- `ar`: Argentina, perfil de análisis ARCA y comprobantes.
- `pe`: Perú, perfil de análisis SUNAT y CPE.
- `cl`: Chile, perfil de análisis SII y DTE.

Estos perfiles son artefactos de análisis y planificación. La existencia de un directorio no implica que sus reglas fiscales estén verificadas o implementadas.