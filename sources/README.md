# Fuentes

Las fichas de esta carpeta registran fuentes utilizadas por los agentes. Una ficha no sustituye el documento oficial.

## Organización por país

```text
sources/
├── mx/
├── sv/
├── gt/
├── pa/
├── co/
├── br/
├── ar/
├── pe/
└── cl/
```

Cada país mantiene un `README.md` y un `official-sources.json`. Los estados `portal_oficial_*` indican que se registró un portal de autoridad; no significan que todas sus páginas o reglas ya hayan sido revisadas.

## Campos mínimos

- `id`
- `jurisdiction`
- `title`
- `authority`
- `type`
- `published_at`
- `effective_at`
- `consulted_at`
- `url`
- `status`
- `notes`

## Catálogo de México

El catálogo operativo inicial está en [`mx_sources.json`](mx_sources.json). Se puede ejecutar con:

```powershell
python -m tools.fiscal_changes collect --catalog sources/mx_sources.json
```

El comando consulta únicamente las fuentes marcadas como `enabled`, guarda una huella SHA-256 por fuente y genera `reports/mx-latest.json`. Los estados significan:

- `new`: primera consulta registrada;
- `changed`: la huella difiere de la consulta anterior;
- `unchanged`: no cambió el contenido recibido;
- `error`: no fue posible consultar la fuente.

Un estado `changed` no es todavía una conclusión fiscal: requiere revisar el documento oficial, sus fechas y su impacto.