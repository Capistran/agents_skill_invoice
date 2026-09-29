---
name: mx-pac-integration
description: Diseña y revisa la integración con un Proveedor Autorizado de Certificación para timbrado, consulta, cancelación y recuperación de CFDI mexicanos.
---

# Integración con PAC

## Antes de integrar

- Confirmar el servicio, contrato, ambiente, límites, costos y SLA del PAC.
- Identificar qué valida el PAC y qué sigue siendo responsabilidad de la aplicación.
- Revisar autenticación, certificados, secretos, idempotencia y trazabilidad.
- Confirmar formatos de solicitud, respuesta, errores, UUID, sellos y acuses.
- Definir retención y protección de XML, credenciales y datos personales.

## Flujos

- timbrado: solicitud, respuesta, UUID, XML certificado y acuse;
- consulta: estado, fecha de consulta y evidencia de respuesta;
- cancelación: solicitud, motivo, sustituto, aceptación y estado final;
- recuperación: reintentos, duplicados, conciliación y atención de errores.

## Regla crítica

El PAC presta un servicio de certificación o consulta; su respuesta no reemplaza el análisis fiscal de la operación ni la revisión de la vigencia normativa.

Nunca colocar credenciales o certificados en archivos versionados. Implementar un adaptador por PAC y no acoplar las reglas fiscales al proveedor.