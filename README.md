# Agentes fiscales

Repositorio para construir agentes que detecten, expliquen y planifiquen cambios fiscales en México, con una evolución prevista hacia otras jurisdicciones de Latinoamérica.

## Enfoque inicial

El proyecto se limita a análisis y planificación. Cada conclusión, regla propuesta o requisito debe poder rastrearse hasta una fuente, una fecha de consulta y una jurisdicción. La implementación de software queda fuera de alcance y solo se documenta como plan posible.

El alcance activo actual es México. La matriz de agentes, skills y entregables de implementación futura está en [docs/mx-implementation-scope.md](docs/mx-implementation-scope.md). Los demás países permanecen diferidos como referencia.

## Estructura

```text
.
├── .claude/commands/       # Flujos reutilizables para Claude Code
├── .claude/skills/         # Skills fiscales con namespace por país (mx-*)
├── decisions/              # Decisiones de arquitectura y producto
├── docs/                    # Diseño del sistema y criterios de calidad
├── jurisdictions/          # Conocimiento fiscal por país
│   └── mx/                 # México: impuestos, autoridades y fuentes
├── sources/                 # Catálogos y fichas de fuentes
├── tools/                   # Utilidades auxiliares de análisis, no producción
└── tests/                   # Pruebas de utilidades documentales
```

## Producto previsto

El alcance de usuarios, capacidades, herramientas para desarrolladores y plan gratuito está documentado en:

- [docs/product-scope.md](docs/product-scope.md)
- [docs/capability-matrix.md](docs/capability-matrix.md)
- [docs/access-model.md](docs/access-model.md)

## Principios

- Trazabilidad sobre velocidad.
- Fuentes primarias sobre resúmenes secundarios.
- Separación entre norma, interpretación y acción.
- Diseño multi-jurisdicción desde el inicio.
- Revisión humana para conclusiones de alto impacto.

## Flujo operativo de análisis

1. Seleccionar país, materia y tipo de documento.
2. Consultar y registrar fuentes oficiales.
3. Aplicar los skills jurisdiccionales correspondientes.
4. Producir hechos, interpretación, riesgos, preguntas y plan de implementación posible.
5. Pasar el resultado a revisión fiscal humana.

Para iniciar una jurisdicción completa usar [`/start-country`](.claude/commands/start-country.md). El comando entrega un reporte de análisis y un plan posible para PAC, autoridad, ERP o aplicación.

Para una revisión puntual de JSON o XML, usar `document-validation` junto con el skill de la jurisdicción y del tipo de documento. No se requiere desarrollo para un análisis individual; la implementación de validaciones repetibles o de alto volumen queda como plan futuro.