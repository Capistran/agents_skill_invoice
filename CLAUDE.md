# Agentes fiscales

## Propósito

Este repositorio ayuda a analizar cambios fiscales en México y, posteriormente, en otras jurisdicciones de Latinoamérica. El sistema produce análisis y planes para una posible implementación posterior; no implementa sistemas productivos ni automatiza decisiones fiscales.

El país activo para el trabajo actual es México. Los demás países se mantienen como referencia diferida y requieren activación explícita.

## Reglas de trabajo

- Responder en español salvo que el usuario pida otro idioma.
- No presentar asesoría fiscal definitiva sin indicar jurisdicción, vigencia y fuente primaria.
- Priorizar fuentes oficiales: Diario Oficial de la Federación, SAT, Secretaría de Hacienda, leyes, reglamentos y reglas misceláneas vigentes.
- Registrar la fecha de consulta y la fecha de vigencia de cada fuente.
- Separar explícitamente hechos, supuestos, cálculos y conclusiones.
- No inventar artículos, tasas, fechas, obligaciones ni enlaces.
- Cuando falte información, formular la pregunta mínima necesaria antes de concluir.
- Tratar datos de contribuyentes como confidenciales; no incluir secretos ni datos personales en archivos versionados.
- Limitar los skills a investigación, análisis, diseño, planificación, riesgos, criterios de aceptación y recomendaciones.
- No crear ni modificar parsers productivos, motores de cálculo, APIs, integraciones PAC, conexiones a ERP o automatizaciones como parte del flujo normal.
- Toda implementación futura requiere una decisión explícita, alcance separado, revisión fiscal y revisión de seguridad.
- Cada capacidad nueva o cambio transversal debe actualizar `/start-country` y, cuando aplique, el maestro externo para mantener el flujo de arranque alineado.
- Para endpoints sandbox, ERP u orígenes SQL/NoSQL usar los skills transversales de descubrimiento; no pedir secretos ni ejecutar cambios externos.
- Diseñar las capacidades para desarrolladores, contadores, directores y pequeños negocios, con lenguaje y controles apropiados para cada perfil.
- El acceso gratuito solo puede ofrecer análisis con fuentes públicas y datos sintéticos o anonimizados; no acciones fiscales irreversibles.

## Convenciones del repositorio

- `jurisdictions/` contiene conocimiento específico por país o jurisdicción.
- `sources/` contiene fichas y referencias de fuentes, no copias completas de legislación salvo que se decida documentarlo expresamente.
- `decisions/` registra decisiones de diseño y criterios que afecten a varios agentes.
- `docs/` contiene arquitectura, flujos y criterios de calidad.
- `.claude/commands/` contiene comandos reutilizables para Claude Code.
- `.claude/agents/` contiene roles especializados para trabajo paralelo.
- `.claude/skills/` contiene análisis CFDI especializados y reutilizables.

## Antes de cerrar un análisis o plan

1. Verificar fuentes primarias y su vigencia.
2. Identificar la jurisdicción y el tipo de impuesto involucrado.
3. Añadir o actualizar una ficha de fuente si se usó material nuevo.
4. Explicar incertidumbres y casos límite.
5. Ejecutar únicamente validaciones del análisis o de los artefactos documentales.
6. Registrar qué queda pendiente para una posible implementación.

## CFDI mexicano

Para analizar XML de CFDI mexicano, iniciar con `mx-cfdi-common` y seleccionar la especialización por tipo de comprobante o complemento. El catálogo y las tareas iniciales están en `docs/cfdi-workplan.md`. No confundir validación técnica del XML con conclusión fiscal.

## Roles para trabajo paralelo

La coordinación y las dependencias están documentadas en `docs/team-workflow.md`. Los agentes especializados no sustituyen la revisión humana fiscal ni de seguridad.