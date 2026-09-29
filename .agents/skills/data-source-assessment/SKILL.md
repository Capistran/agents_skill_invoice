---
name: data-source-assessment
description: Evalúa cualquier origen de datos SQL o NoSQL para planificar integración fiscal, modelado, extracción, calidad, seguridad y trazabilidad.
---

# Evaluación de origen de datos

## Familias a considerar

### SQL

- PostgreSQL;
- SQL Server;
- MySQL/MariaDB;
- Oracle;
- SQLite;
- SAP HANA;
- IBM Db2.

### NoSQL

- MongoDB;
- DynamoDB;
- Cosmos DB;
- Redis, solo cuando el uso sea cache/eventos y no fuente definitiva;
- Elasticsearch/OpenSearch, solo cuando el índice no sustituya la fuente transaccional.

### Otros orígenes

- REST, SOAP, GraphQL;
- SFTP, CSV, Excel y archivos XML/JSON;
- colas y eventos;
- data warehouse o lakehouse;
- plataformas SaaS y marketplaces.

## Analizar

- tecnología, versión, hosting y propietario;
- esquema, tablas, colecciones, claves y relaciones;
- fuente de verdad por dato fiscal;
- calidad, duplicados, nulos y conflictos;
- fechas, zona horaria, moneda y precisión;
- volumen, frecuencia, latencia y cambios de esquema;
- CDC, timestamps, cursores, paginación o snapshots;
- permisos mínimos, cifrado, secretos y datos personales;
- retención, respaldo y auditoría.

## Entrega

- ficha del origen;
- inventario de entidades y campos;
- matriz de mapeo al modelo fiscal canónico;
- estrategia de extracción y sincronización futura;
- riesgos, supuestos y datos faltantes;
- pruebas de calidad y criterios de aceptación.

No solicitar ni almacenar contraseñas reales. No ejecutar consultas destructivas ni asumir que una conexión de lectura implica autorización fiscal.