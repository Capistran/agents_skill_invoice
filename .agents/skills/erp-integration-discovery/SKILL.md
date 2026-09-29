---
name: erp-integration-discovery
description: Analiza un ERP o aplicación empresarial para planificar integración fiscal, documentos, eventos, usuarios, permisos y trazabilidad sin construir conectores productivos.
---

# Descubrimiento de ERP

## Entrada esperada

- nombre y versión del ERP;
- módulos activos: ventas, compras, inventario, tesorería, nómina, contabilidad;
- API, exportaciones, webhooks, colas o acceso a base de datos;
- ejemplos anonimizados;
- sistema de origen de cada dato;
- responsables funcionales y técnicos.

## Analizar

- ciclo de vida de venta, compra, pago, devolución, cancelación y nómina;
- correspondencia entre operación real y documento fiscal;
- identificadores, claves, folios, UUID o equivalentes locales;
- estados, eventos, reintentos y conciliación;
- datos maestros: clientes, proveedores, productos, servicios, impuestos y monedas;
- permisos, segregación, auditoría y retención;
- diferencias entre API, exportación y lectura directa de base;
- impacto de cambios normativos en procesos y reportes.

## Entrega

- mapa de sistemas y responsables;
- mapa origen-destino de datos;
- modelo canónico propuesto;
- contratos de eventos o API;
- estrategia de sincronización e idempotencia;
- riesgos de calidad y privacidad;
- plan de pruebas y migración futura.

No modificar el ERP, ejecutar SQL destructivo ni crear integraciones productivas desde este skill.