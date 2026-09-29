---
name: mx-cfdi-app-integration
description: Integra el análisis fiscal de CFDI en una aplicación contable, ERP, nómina o facturación, con contratos, eventos, permisos, auditoría y revisión humana.
---

# Integración con aplicaciones

## Diseñar

- contrato de entrada para XML, UUID, metadatos y contexto de operación;
- resultado de análisis con hechos, reglas ejecutadas, hallazgos, fuente y confianza;
- estados de procesamiento, revisión, aprobación y rechazo;
- eventos para CFDI recibido, cambio de catálogo, cambio normativo y respuesta de PAC;
- correlación entre CFDI, operación contable, pago, cliente, proveedor y usuario;
- permisos por función y protección de datos personales.

## Reglas de arquitectura

- Mantener el XML original inmutable y separar extracción, validación e interpretación.
- Hacer idempotente la recepción por UUID y hash.
- No bloquear automáticamente una operación por una advertencia sin política aprobada.
- Conservar quién aprobó una excepción, cuándo y con qué evidencia.
- Permitir reprocesar con una nueva versión de reglas sin perder el resultado anterior.

## Entrega

Contrato de API o eventos, matriz de estados, estrategia de errores, auditoría, permisos y plan de despliegue gradual.