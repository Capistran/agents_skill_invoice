# Matriz de capacidades y herramientas

Este documento sirve para planificar una posible implementación futura. No autoriza construir las capacidades.

| Capacidad | Usuario principal | Resultado de análisis | Herramienta futura requerida | Prioridad |
| --- | --- | --- | --- | --- |
| fuentes y cambios | fiscal, dirección | ficha, cambio, vigencia, impacto | monitor de fuentes y snapshots | P0 |
| revisión de documento | fiscal, pequeño negocio | hechos, campos, riesgos y preguntas | parser seguro y visor | P0 |
| reglas versionadas | fiscal, desarrollador | regla, fuente, severidad y pruebas | repositorio de reglas | P0 |
| catálogos y schemas | desarrollador, QA | diferencias de versión y compatibilidad | registro de artefactos | P0 |
| riesgo de cálculo | fiscal, dirección | factores críticos y bloqueos | motor de evaluación futura | P0 |
| revisión humana | fiscal, dirección | aprobado, rechazado o pendiente | workflow de revisión y auditoría | P0 |
| PAC o certificador | desarrollador, contador | contrato, estados, errores y riesgos | adaptador por proveedor | P1 |
| ERP o aplicación | desarrollador, dirección | eventos, API, permisos y aceptación | API/event bus y conectores | P1 |
| pagos y cancelación | contador, desarrollador | estados y evidencia requerida | adaptadores de consulta | P1 |
| seguridad y privacidad | todos | amenazas, controles y retención | IAM, secretos, cifrado y logs | P0 |
| observabilidad | operador, dirección | salud, latencia, errores y fuentes caídas | métricas, alertas y runbooks | P1 |
| aprendizaje y ayuda | pequeño negocio | explicación, glosario y checklist | interfaz guiada y base de conocimiento | P1 |
| sandbox y endpoint | desarrollador, fiscal | operaciones, estados, errores y evidencias | contrato y adaptador por servicio | P1 |
| ERP y datos | desarrollador, DBA | mapeo, calidad y fuente de verdad | conectores, CDC, ETL o eventos | P1 |

## Herramientas que necesitaría un desarrollador

### Conocimiento y evidencia

- registro versionado de fuentes;
- almacenamiento de documentos y hashes;
- comparación de versiones y diff;
- catálogo de autoridades, documentos, impuestos y vigencias;
- buscador de conocimiento con filtros de jurisdicción.

### Análisis documental

- parser XML/JSON/PDF aislado;
- validación XSD o schema;
- detección de firma, certificado y metadatos;
- extracción de conceptos, impuestos y relaciones;
- protección contra documentos maliciosos.

### Reglas y calidad

- repositorio de reglas con vigencia;
- evaluación reproducible y explicación de resultados;
- fixtures anonimizados;
- regresión normativa;
- pruebas de redondeo, fechas, moneda y documentos relacionados.

### Integraciones

- adaptadores independientes por PAC, certificador, autoridad o proveedor;
- API y eventos para ERP;
- idempotencia, reintentos y correlación;
- sandbox y datos sintéticos;
- auditoría y recuperación.

### Orígenes de datos

El análisis debe contemplar al menos PostgreSQL, SQL Server, MySQL/MariaDB, Oracle, SQLite, SAP HANA, Db2, MongoDB, DynamoDB, Cosmos DB, Redis, Elasticsearch/OpenSearch, REST, SOAP, GraphQL, SFTP, CSV, Excel, colas, warehouses y SaaS. La selección final depende del ERP y del caso.

### Seguridad

- autenticación y autorización por organización;
- segregación de datos por cuenta;
- gestión de secretos y certificados;
- cifrado, retención y borrado;
- límites de uso y protección contra abuso;
- registro de acciones sensibles.