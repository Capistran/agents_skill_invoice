---
name: integration-discovery
description: Analiza un endpoint sandbox, API o servicio de pruebas de una autoridad, PAC, certificador u OSE/PSE y prepara un plan de integración sin ejecutar operaciones productivas.
---

# Descubrimiento de integración

## Entrada esperada

- documentación del endpoint;
- URL de sandbox, nunca secretos en el repositorio;
- método de autenticación descrito;
- ejemplos sintéticos de solicitud y respuesta;
- operaciones disponibles;
- límites, errores, versiones y ambiente.

## Analizar

1. Identificar autoridad, proveedor, país, documento y ambiente.
2. Clasificar endpoint REST, SOAP, SFTP, AS2, cola, portal u otro protocolo.
3. Documentar autenticación, certificados, tokens, firma, scopes y rotación.
4. Inventariar operaciones, métodos, headers, payloads, respuestas y estados.
5. Identificar idempotencia, correlación, reintentos, timeouts, rate limits y paginación.
6. Separar validación técnica, respuesta del servicio y conclusión fiscal.
7. Revisar datos personales, secretos, XML/JSON no confiable y riesgos de prompt injection.
8. Proponer contrato de integración, pruebas sintéticas, observabilidad y plan por fases.

## Entrega

- ficha del servicio;
- matriz operación/entrada/salida/estado/error;
- requisitos de autenticación;
- mapa de evidencias y auditoría;
- casos de prueba sandbox;
- riesgos y bloqueos;
- plan futuro de implementación.

No ejecutar timbrado, cancelación, declaración, envío real ni modificar datos externos. No guardar credenciales, certificados ni tokens.